# Linux Service Monitor & Auto Restart

## Overview
A Bash script that monitors a Linux service and automatically restarts it if it goes down.

## Features
- Monitor service status
- Auto restart
- Logging
- Timestamped events

## Technologies
- Bash
- Linux
- systemd
- AWS EC2

## Usage

chmod +x ServerRestart.sh

./ServerRestart.sh

## Sample Log

[2026-07-15 09:00:00] SUCCESS: nginx is running perfectly.

[2026-07-15 09:15:23] WARNING: nginx is DOWN!! Attempting to restart...

[2026-07-15 09:15:24] SUCCESS: nginx restarted and fixed automatically!

## Future Improvements
- Cron automation
- Multiple service support
