#!/usr/bin/env python3

import time
import subprocess
import logging

# Logging configuration: defines log format and output file.
logging.basicConfig(
    filename='/var/log/DB_restart.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

SERVICE_NAME = "mariadb"
CHECK_INTERVAL = 60  # seconds


def check_service_status():
    """
    Checks whether the MariaDB service is active.
    Returns: "active", "inactive", "failed", or None if an error occurs.
    """
    try:
        result = subprocess.run(
            ['systemctl', 'is-active', SERVICE_NAME],
            capture_output=True, text=True, check=False
        )
        return result.stdout.strip()
    except Exception as e:
        logging.error("Error while checking service status: %s", e)
        return None


def restart_service():
    """
    Restarts the MariaDB service and logs the result.
    """
    try:
        logging.info("Attempting to restart MariaDB service...")
        result = subprocess.run(
            ['systemctl', 'restart', SERVICE_NAME],
            capture_output=True, text=True, check=False
        )
        if result.returncode == 0:
            logging.info("Service restarted successfully.")
        else:
            logging.error("Service restart error: %s", result.stderr)
    except Exception as e:
        logging.error("Exception during service restart: %s", e)


def main():
    """
    Main loop: checks the service.
    If service is not active, it triggers a restart.
    """
    while True:
        status = check_service_status()
        if status != "active":
            logging.warning(f"Service status is '{status}'. Restarting...")
            restart_service()
        time.sleep(CHECK_INTERVAL)


if __name__ == '__main__':
    main()
