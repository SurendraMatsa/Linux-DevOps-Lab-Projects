# Service Monitor & Auto-Restart Script

A simple Bash automation script that continuously checks whether a Linux service is running. If the service is found to be down, the script automatically attempts to restart it and records every event in a log file with timestamps.

---

##  Problem Statement

In Linux servers, critical services such as **Nginx**, **Apache**, or **MySQL** may unexpectedly stop due to crashes, configuration issues, or resource exhaustion.

Manually checking the status of these services is time-consuming and increases downtime.

The objective of this project is to automate service monitoring and recovery using a Bash script.

---

##  Solution

This Bash script performs the following tasks:

- Checks whether a specified Linux service is running.
- Detects if the service has stopped.
- Attempts to restart the service automatically.
- Verifies whether the restart was successful.
- Logs all activities with timestamps.
- Reports if manual intervention is required.

This reduces service downtime and eliminates the need for constant manual monitoring.

---

##  Features

-  Service status monitoring
-  Automatic service restart
-  Timestamp-based logging
-  Success and failure detection
-  Simple and lightweight Bash implementation
-  Easy to customize for any systemd service

---

##  Technologies Used

- Linux
- Bash Scripting
- systemd (`systemctl`)
- AWS EC2 (Test Environment)

---

##  Source Code

```bash
ServerRestart.sh
```

The complete source code is available in this repository.

---

##  Project Structure

```
01-service-monitor/
│
├── ServerRestart.sh
├── README.md
└── screenshots/
```

---

##  Usage Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/linux-devops-lab.git
```

### 2. Navigate to the project

```bash
cd linux-devops-lab/01-service-monitor
```

### 3. Give execute permission

```bash
chmod +x ServerRestart.sh
```

### 4. Run the script

```bash
./ServerRestart.sh
```

---

##  Sample Output

### Case 1 — Service is Running

```
[2026-07-15 10:05:12] SUCCESS: nginx is running perfectly.
```

---

### Case 2 — Service Stopped

```
[2026-07-15 10:10:25] WARNING: nginx is DOWN!! Attempting to restart...
[2026-07-15 10:10:27] SUCCESS: nginx restarted and fixed automatically!
```

---

### Case 3 — Restart Failed

```
[2026-07-15 10:15:41] WARNING: nginx is DOWN!! Attempting to restart...
[2026-07-15 10:15:42] CRITICAL: nginx restart FAILED! Needs manual intervention.
```

---

##  Log File

The script stores all logs in:

```
/tmp/service_monitor.log
```

View logs using:

```bash
cat /tmp/service_monitor.log
```

Or monitor logs in real time:

```bash
tail -f /tmp/service_monitor.log
```

---

##  Configuration

Change the monitored service by modifying:

```bash
SERVICE="nginx"
```

Examples:

```bash
SERVICE="httpd"
```

```bash
SERVICE="sshd"
```

```bash
SERVICE="docker"
```

---

##  Key Learnings

Through this project, I learned:

- Writing production-style Bash scripts
- Using Linux conditional statements (`if-else`)
- Working with Linux services using `systemctl`
- Automating repetitive system administration tasks
- Implementing timestamp-based logging
- Using exit status and service verification
- Improving troubleshooting and debugging skills
- Organizing Bash projects using Git and GitHub

---

##  Future Improvements

- Monitor multiple services simultaneously
- Email notifications on service failures
- Slack or Microsoft Teams alerts
- Cron job integration for periodic monitoring
- Health check using HTTP requests
- CPU and memory monitoring
- CloudWatch integration for AWS environments
- Configurable service list using a configuration file

---

##  Author

**Surendra**

Learning Linux, AWS Cloud, and DevOps by building real-world automation projects.

---

 If you found this project useful, feel free to give it a star!
