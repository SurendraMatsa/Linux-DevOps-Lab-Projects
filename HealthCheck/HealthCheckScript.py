import os
import subprocess
import datetime

# Configuration
LOG_FILE = "/tmp/health_check_logs.log"
THRESHOLD = 80.0

# Create log file if it doesn't exist
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "a").close()


def get_disk_usage():
    """Returns disk usage percentage of root filesystem."""
    command = "df / | awk 'NR==2 {gsub(/%/, \"\", $5); print $5}'"

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        check=True
    )

    return float(result.stdout.strip())


def get_cpu_usage():
    """Returns CPU usage percentage."""
    command = "vmstat 1 2 | tail -1 | awk '{print 100-$15}'"

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        check=True
    )

    return round(float(result.stdout.strip()), 2)


def monitor_system():
    """Checks system health and logs the result."""

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        disk_usage = get_disk_usage()
        cpu_usage = get_cpu_usage()

        print(f"Disk Usage : {disk_usage}%")
        print(f"CPU Usage  : {cpu_usage}%")

        if disk_usage >= THRESHOLD or cpu_usage >= THRESHOLD:
            status = "CRITICAL ALERT"
            print("\nWARNING! Server resources crossed the threshold.")
        else:
            status = "HEALTHY"
            print("\nSystem is healthy.")

        log_message = (
            f"{timestamp} | {status} | "
            f"Disk: {disk_usage}% | CPU: {cpu_usage}%\n"
        )

        with open(LOG_FILE, "a") as file:
            file.write(log_message)

        print(f"Log written successfully to: {LOG_FILE}")

    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")

    except ValueError as e:
        print(f"Unable to parse command output: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    monitor_system()