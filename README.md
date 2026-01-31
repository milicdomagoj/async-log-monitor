# Async Log Monitor

Asynchronous Python application for real-time monitoring of Linux log files.  
The tool tracks multiple log files concurrently, detects critical events, and reports them in a clean and production-ready way.

---

## Features

- Asynchronous monitoring of multiple log files using `asyncio`
- Real-time detection of log levels:
  - `ERROR`
  - `WARNING`
  - `CRITICAL`
- Colored terminal output for better readability
- Timestamped log entries
- Centralized error logging to a separate output file
- Configuration via external `config.json`
- Graceful shutdown (CTRL+C) without stack traces
- Fully compatible with Python 3.12+

---

## Technologies Used

- **Python 3.12**
- **asyncio** – asynchronous task management
- **JSON** – configuration handling
- **Linux filesystem**
- **Git & GitHub**

---

## Project Structure

async-log-monitor/

├── reader_async_multi.py # Main async log monitoring application

├── reader_async_one.py # Async single-file example

├── reader_basic.py # Synchronous prototype (learning step)

├── config.json # Application configuration

├── detected_errors.log # Output file for detected issues

├── .gitignore

└── README.md


---

## Configuration (`config.json`)

All runtime configuration is handled externally via `config.json`:

json
{
  "files_to_watch": [
    "syslog.log",
    "auth.log"
  ],
  "keywords": [
    "ERROR",
    "WARNING",
    "CRITICAL"
  ],
  "poll_interval": 0.2,
  "output_file": "detected_errors.log"
}

Configuration Options
files_to_watch – list of log files to monitor
keywords – log levels that trigger detection
poll_interval – how often files are checked (seconds)
output_file – file where detected issues are stored

---

## Running the Application
Activate your virtual environment (if used):
source venv/bin/activate


Run the log monitor:
python3 reader_async_multi.py

---

## Testing the Monitor
In a separate terminal, append log entries:
echo "ERROR Disk failure detected" >> syslog.log
echo "WARNING Low disk space" >> auth.log

---

Detected events will:
Appear instantly in the terminal (with colors)
Be written to detected_errors.log

---

## Graceful Shutdown

Stop the application safely using:
CTRL + C
The application shuts down cleanly without stack traces or errors.

---

## Learning Goals & Motivation

This project was created to:
Practice asynchronous programming in Python
Understand event loops and non-blocking I/O
Work with Linux-style log monitoring
Build a production-oriented CLI tool
Prepare for junior / student Python developer roles

---

## Possible Improvements

Log rotation support
Directory-based log discovery
Alerting (Slack / Email / Webhooks)
Interactive TUI (terminal UI)
Running as a Linux system service

---

## Author

Domagoj Milić
GitHub: https://github.com/milicdomagoj

