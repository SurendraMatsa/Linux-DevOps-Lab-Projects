#!/bin/bash

DIRECTORY="/tmp/app-logs"
LOG_FILE="/tmp/app-logs/logclean.log"
TIME=$(date "+%Y-%m-%d %H:%M:%S")

echo "[$TIME] INFO: Starting log cleanup process for $DIRECTORY..." >> "$LOG_FILE"

# Validate the directory
if [ ! -d "$DIRECTORY" ]; then
    echo "[$TIME] ERROR: Target directory $DIRECTORY does not exist." >> "$LOG_FILE"
    exit 1
fi

# Count old log files
OLD_FILE_COUNT=$(find "$DIRECTORY" -type f -mtime +30 | wc -l)

if [ "$OLD_FILE_COUNT" -eq 0 ]; then
    echo "[$TIME] SUCCESS: No files older than 30 days found. Nothing to delete." >> "$LOG_FILE"
else
    echo "[$TIME] INFO: Found $OLD_FILE_COUNT files older than 30 days. Deleting..." >> "$LOG_FILE"

    find "$DIRECTORY" -type f -mtime +30 -exec rm {} \;

    echo "[$TIME] SUCCESS: Successfully deleted $OLD_FILE_COUNT old files." >> "$LOG_FILE"
fi
