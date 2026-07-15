#  Log Cleaner Script

A Bash automation script that identifies log files older than a specified number of days and automatically removes them to free up disk space. The script also records every cleanup operation in a log file with timestamps for auditing and troubleshooting.

---

#  Problem Statement

Linux servers continuously generate application and system log files. Over time, these logs consume valuable disk space, which can lead to storage issues and affect system performance if not managed properly.

Manually identifying and deleting outdated log files is repetitive, time-consuming, and prone to human error.

The objective of this project is to automate the cleanup of old log files using a Bash script.

---

#  Solution

This Bash script performs the following tasks:

* Validates that the target log directory exists.
* Searches for log files older than **30 days**.
* Counts the number of old log files.
* Deletes all matching files automatically.
* Records every operation with timestamps in a log file.
* Exits gracefully if the target directory does not exist.

This automation helps maintain disk space and reduces manual maintenance.

---

#  Features

*  Directory validation
*  Automatic log cleanup
*  Deletes files older than 30 days
*  Timestamp-based logging
*  Counts files before deletion
*  Lightweight Bash implementation
*  Easy to customize for different directories and retention periods

---

#  Technologies Used

* Linux
* Bash Scripting
* find Command
* File System Management
* AWS EC2 (Test Environment)

---

#  Source Code

```text
logclean.sh
```

The complete source code is available in this repository.

---

#  Project Structure

```text
02-log-cleaner/
│
├── logclean.sh
├── README.md
└── screenshots/
```

---

#  Usage Instructions

### 1. Clone the repository

```bash
git clone https://github.com/SurendraMatsa/Linux-DevOps-Lab-Projects.git
```

### 2. Navigate to the project

```bash
cd Linux-DevOps-Lab-Projects/LogCleanerScript
```

### 3. Give execute permission

```bash
chmod +x logcleanScript.sh
```

### 4. Run the script

```bash
./logcleanScript.sh
```

---

#  Sample Output

### Case 1 — No Old Files Found

```
[2026-07-15 10:20:15] INFO: Starting log cleanup process for /tmp/app-logs...
[2026-07-15 10:20:15] SUCCESS: No files older than 30 days found. Nothing to delete.
```

---

### Case 2 — Old Files Deleted Successfully

```
[2026-07-15 10:25:42] INFO: Starting log cleanup process for /tmp/app-logs...
[2026-07-15 10:25:42] INFO: Found 5 files older than 30 days. Deleting...
[2026-07-15 10:25:43] SUCCESS: Successfully deleted 5 old files.
```

---

### Case 3 — Directory Does Not Exist

```
[2026-07-15 10:30:08] ERROR: Target directory /tmp/app-logs does not exist.
```

---

#  Log File

The script stores execution logs in:

```text
/tmp/app-logs/logclean.log
```

View the log file:

```bash
cat /tmp/app-logs/logclean.log
```

Monitor logs in real time:

```bash
tail -f /tmp/app-logs/logclean.log
```

---

#  Configuration

Change the target directory:

```bash
DIRECTORY="/tmp/app-logs"
```

Change the log retention period:

```bash
-mtime +30
```

Examples:

Delete files older than **7 days**

```bash
-mtime +7
```

Delete files older than **15 days**

```bash
-mtime +15
```

Delete files older than **90 days**

```bash
-mtime +90
```

---

#  Key Learnings

Through this project, I learned:

* Writing Bash automation scripts
* Using the `find` command for file management
* Understanding the `-mtime` option
* Deleting files safely with `-exec`
* Validating directories before execution
* Logging script execution with timestamps
* Automating routine Linux administration tasks
* Organizing projects using Git and GitHub

---

#  Future Improvements

* Support multiple directories
* Accept directory and retention period as command-line arguments
* Generate cleanup reports
* Compress old log files before deletion
* Email or Slack notifications
* Schedule automatic execution using Cron
* Exclude specific file types or directories
* Add configurable log retention through a configuration file

---

#  Author

**Surendra**

Learning Linux, AWS Cloud, and DevOps by building real-world automation projects.

---

 If you found this project useful, feel free to give it a star!
