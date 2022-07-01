# Script to check disk usage and cpu usage

import shutil
import psutil


def disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = (du.free / du.total) * 100
    return free > 20  # Disk space should be more than 20%


def cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75  # CPU usage should be less than 75%


if not disk_usage("/") or not cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")
