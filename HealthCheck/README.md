# Project - 5 :

## Project: Linux System Health Monitoring Script

A Python-based Linux system monitoring script that checks the health of a Linux server by monitoring **Disk Usage** and **CPU Usage**. The script logs the health status with timestamps and alerts when resource utilization crosses a predefined threshold.

---

## Features

- Monitor Disk Usage of the root filesystem
- Monitor CPU Usage
- Configurable usage threshold (default: 80%)
- Automatic log file creation
- Logs every execution with timestamp
- Displays HEALTHY or CRITICAL ALERT status
- Exception handling for command execution and parsing errors
- Designed to run manually or through Cron Jobs

---

## Technologies Used

- Python 3
- Linux
- Bash Commands
- subprocess module
- datetime module
- OS module

---

## Linux Commands Used

### Disk Usage

```bash
df /
awk
sed
```

### CPU Usage

```bash
vmstat
tail
awk
```

---

## Project Structure

```
Linux-DevOps-Lab-Projects/
│
├── HealthCheck/
│   ├── HealthCheckScript.py
│   ├── screenshots/
│   │   ├── screenshot1.jpg
│   │   └── screenshot2.jpg
│   └── README.md

```

---

## How It Works

1. Checks current disk usage.
2. Checks current CPU usage.
3. Compares both values with the configured threshold.
4. If usage exceeds the threshold:
   - Displays a warning.
   - Logs a **CRITICAL ALERT**.
5. Otherwise:
   - Displays a healthy status.
   - Logs a **HEALTHY** message.

---

## Log File

Logs are stored in:

```bash
/tmp/health_check_logs.log
```

Example:

```
2026-07-27 11:42:18 | HEALTHY | Disk: 22.0% | CPU: 3.10%
2026-07-27 11:48:01 | CRITICAL ALERT | Disk: 84.0% | CPU: 91.75%
```

---

## Run the Script

Clone the repository

```bash
git clone https://github.com/SurendraMatsa/Linux-DevOps-Lab-Projects

Navigate to the project

```bash
cd Linux-DevOps-Lab-Projects/HealthCheck
```

Run

```bash
python3 HealthCheckScript.py
```

---

## Sample Output

Healthy

```
Disk Usage : 22.0%
CPU Usage  : 4.12%

System is healthy.
Log written successfully.
```

Critical

```
Disk Usage : 87.0%
CPU Usage  : 92.54%

WARNING! Server resources crossed the threshold.
Log written successfully.
```

---

## Skills Demonstrated

- Linux Administration
- Python Automation
- Linux Process Monitoring
- System Health Monitoring
- Bash Commands
- Exception Handling
- Log Management
- Automation Scripting
- DevOps Fundamentals

---


## Learning Outcome

This project helped me understand how to:

- Execute Linux commands from Python
- Automate server health monitoring
- Parse command-line output
- Handle exceptions effectively
- Generate structured log files
- Build practical DevOps automation scripts

---

## Author

**Surendra**

If you found this project useful, consider giving the repository a star.