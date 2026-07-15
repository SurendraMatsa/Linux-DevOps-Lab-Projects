#!/bin/bash

#====================================================
#Task: Service Monitor & Auto-Restart Script
#Author: Surendra
#====================================================

SERVER="nginx"
LOG_FILE="/tmp/service_monitor.log"

# Current Timestamp for logging
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Check if the service is active or not
STATUS=$(systemctl is-active $SERVER)

if [ "$STATUS" = "active" ]; then
    echo "[$TIMESTAMP] SUCCESS: $SERVER is running perfectly." >> $LOG_FILE
else
    echo "[$TIMESTAMP] WARNING: $SERVER is DOWN!! Attempting to restart..." >> $LOG_FILE
    
    # Attempting to restart the service using sudo
    sudo systemctl restart $SERVER
    
    # Re-checking the status after restart attempt
    NEW_STATUS=$(systemctl is-active $SERVER)
    
    if [ "$NEW_STATUS" = "active" ]; then
        echo "[$TIMESTAMP] SUCCESS: $SERVER restarted and fixed automatically!" >> $LOG_FILE
    else
        echo "[$TIMESTAMP] CRITICAL: $SERVER restart FAILED! Needs manual intervention." >> $LOG_FILE
    fi
fi