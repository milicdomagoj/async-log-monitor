import asyncio

async def follow_async(file_path):
    with open(file_path, "r") as f:
        f.seek(0, 2)

        while True:
            line = f.readline()

            if not line:
                await asyncio.sleep(0.2)
                continue
            print("ASYNC NEW LINE:", line.strip())

async def main():
    await follow_async("syslog.log")

if __name__ == "__main__":
    asyncio.run(main())
