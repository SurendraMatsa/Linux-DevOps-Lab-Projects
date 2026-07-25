# Linux Backup Automation using Python

## Overview

This project automates the process of creating compressed backups of Linux directories using Python. It validates the source directory, creates the backup destination if required, generates a timestamped archive, and maintains execution logs for successful and failed backup operations.

The project demonstrates how Python can automate routine backup tasks commonly performed by Linux System Administrators and DevOps Engineers.

---

## Features

- Verify whether the source directory exists
- Automatically create the backup destination directory if it does not exist
- Generate timestamped backup archives
- Compress backups into `.tar.gz` format
- Execute Linux `tar` command using Python
- Log successful backup operations
- Log backup failures with error details
- Basic exception handling

---

## Technologies Used

- Python 3
- Linux
- subprocess
- os
- datetime
- sys

---

## Folder Structure

```
Backup-Automation/
│
├── backup_project.py
├── README.md
└── screenshots/
    ├── screenshot1.png
    └── screenshot2.png
```

---

## How It Works

```
Start
   │
   ▼
Receive Source & Backup Directory
   │
   ▼
Validate Source Directory
   │
   ├── Not Found → Log Error → Exit
   │
   ▼
Check Backup Directory
   │
   ├── Doesn't Exist → Create Directory
   │
   ▼
Generate Timestamp
   │
   ▼
Create .tar.gz Archive
   │
   ▼
Log Success
   │
   ▼
Backup Completed
```

---

## Prerequisites

- Linux Operating System
- Python 3
- tar utility installed

---

## Usage

Run the script using:

```bash
python3 final_backup_project.py <source_directory> <backup_directory>
```

### Example

```bash
python3 final_backup_project.py /home/ec2-user/project /home/ec2-user/backups
```

---

## Example Output

```
Archiving /home/ec2-user/project into /home/ec2-user/backups/backup_project_20260725_203015.tar.gz...

SUCCESS: Folder backed up and zipped perfectly!

Check logs at:
/tmp/backup_execution.log
```

---

## Output Files

Example backup:

```
/home/ec2-user/backups/
└── backup_project_20260725_203015.tar.gz
```

Log file:

```
/tmp/backup_execution.log
```

---

## Linux Commands Used

- tar

---

## Python Concepts Used

- Functions
- File Handling
- Exception Handling
- Command-line Arguments
- subprocess Module
- os Module
- datetime Module

---

## Logging

The script automatically records every execution.

Successful backup example:

```
[2026-07-25 20:30:15] SUCCESS: Backup created successfully at /home/ec2-user/backups/backup_project_20260725_203015.tar.gz
```

Failure example:

```
[2026-07-25 20:35:42] ERROR: Source directory '/home/ec2-user/demo' not found!
```

## Learning Outcomes

This project helped me understand:

- Linux backup automation using Python
- Executing Linux commands with `subprocess`
- Archive creation using the `tar` utility
- Error handling and execution logging
- Working with timestamps and file paths
- Automating repetitive Linux administration tasks commonly used in DevOps environments

---