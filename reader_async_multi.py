import asyncio
import json
from datetime import datetime


class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"


def load_config():
    with open("config.json") as f:
        return json.load(f)


async def follow_async(file_path, keywords, output_file, interval):
    try:
        with open(file_path, "r") as f:
            f.seek(0, 2)

            while True:
                line = f.readline()

                if not line:
                    await asyncio.sleep(interval)
                    continue

                stripped = line.strip()

                color = Colors.CYAN

                if any(k in stripped for k in keywords):
                    if "ERROR" in stripped or "CRITICAL" in stripped:
                        color = Colors.RED
                    elif "WARNING" in stripped:
                        color = Colors.YELLOW

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print(f"{color}[{timestamp}] [{file_path}] {stripped}{Colors.RESET}")

                for keyword in keywords:
                    if keyword in stripped:
                        with open(output_file, "a") as log_f:
                            log_f.write(f"{timestamp} - {file_path} - {stripped}\n")
                        break

    except asyncio.CancelledError:
        return


async def main():
    config = load_config()

    tasks = [
        asyncio.create_task(
            follow_async(
                file_path,
                config["keywords"],
                config["output_file"],
                config["poll_interval"]
            )
        )
        for file_path in config["files_to_watch"]
    ]

    try:
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        print("\nShutting down... (CTRL+C)")

        for t in tasks:
            t.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutdown complete.")
