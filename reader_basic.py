import time

def follow(file_path):
    with open(file_path, "r") as f:
        f.seek(0, 2)

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.2)
                continue
            print("NEW LINE:", line.strip())

if __name__ == "__main__":
    follow("syslog.log")
