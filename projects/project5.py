#!/usr/bin/env python3
"""
# Author : Khalid Maina.
# Date : 18/12/2020.
...................................
Script that checks the health of os.
...................................
"""
import shutil
import psutil
import socket

def check_cpu_usage():
    """Checks that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_disk_usage(disk):
    """Checks that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_available_memory():
    """Checks available memory in linux-instance, in byte"""
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500

def main():
    if check_cpu_usage():
        error_message = "C.P.U usage is over 80%"
        print(error_message)
    elif not check_disk_usage('/'):
        error_message = "available disk space is less than 20%"
        print(error_message)
    elif not check_available_memory():
        error_message = "available memory is less than 500MB"
        print(error_message)
    else:
        print('[+] os is in good health')

if __name__ == "__main__":
    main()
