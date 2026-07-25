# Linux User Onboarding Automation

A Python automation script that simplifies Linux user onboarding by automating user creation, password configuration, project workspace creation, and permission management.

---

## Project Objective

System administrators and DevOps engineers often perform repetitive user onboarding tasks manually. This project automates the entire onboarding process using Python and Linux system commands.

---

## Features

- Verify whether the user already exists
- Create a new Linux user
- Create the user's home directory
- Set the user's password securely
- Create a dedicated project directory
- Generate a welcome file
- Assign correct ownership and permissions
- Basic error handling

---

## Technologies Used

- Python 3
- Linux
- subprocess
- os
- sys

---

## Folder Structure

```
OnboardingUser/
│
├── onboard_user.py
├── screenshots/
│   ├── screenshot1.png
│   └── screenshot2.png
└── README.md
```

---

## How It Works

```
Start
  │
  ▼
Receive Username & Password
  │
  ▼
Check Existing User
  │
  ├── Exists → Exit
  │
  ▼
Create Linux User
  │
  ▼
Configure Password
  │
  ▼
Create Project Folder
  │
  ▼
Generate Welcome File
  │
  ▼
Assign Ownership
  │
  ▼
Success
```

---

## Prerequisites

- Linux
- Python 3
- sudo privileges

---

## Run the Project

```bash
sudo python3 onboard_user.py <username> <password>
```

Example

```bash
sudo python3 onboard_user.py devuser Password123
```

---

## Output

```
Starting onboarding process for user: devuser
Creating user account...
User account created successfully.
Setting password...
Password configured successfully.
Creating project directory...
Welcome file generated successfully.
Ownership transferred.
SUCCESS: Onboarding completed.
```

---

## Files Created

```
/home/devuser

/tmp/devuser_project

/tmp/devuser_project/welcome.txt
```

---

## Linux Commands Used

- id
- useradd
- chpasswd
- chown

---

## Python Concepts Used

- Functions
- Exception Handling
- subprocess
- File Handling
- Command-line Arguments
- os Module

---

## Learning Outcomes

This project helped me understand how Python can automate Linux system administration tasks commonly performed in DevOps environments.
