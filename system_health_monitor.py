import subprocess
import logging


logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_cpu_usage():
    cpu_usage = float(subprocess.check_output("grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'", shell=True))
    if cpu_usage > CPU_THRESHOLD:
        logging.info(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    mem_info = subprocess.check_output("free | grep Mem | awk '{print $3/$2 * 100.0}'", shell=True)
    memory_usage = float(mem_info)
    if memory_usage > MEMORY_THRESHOLD:
        logging.info(f'High memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk_usage():
    disk_info = subprocess.check_output("df / | grep / | awk '{print $5}'", shell=True)
    disk_usage = float(disk_info.decode('utf-8').strip().replace('%', ''))
    if disk_usage > DISK_THRESHOLD:
        logging.info(f'High disk usage detected: {disk_usage}%')
    return disk_usage

def check_running_processes():
    processes = subprocess.check_output("ps -eo pid,comm,user", shell=True).decode('utf-8').strip().split('\n')
    logging.info(f'Running processes: {processes}')
    return processes

def main():
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_usage()
    processes = check_running_processes()

    print(f'CPU Usage: {cpu_usage}%')
    print(f'Memory Usage: {memory_usage}%')
    print(f'Disk Usage: {disk_usage}%')
    print(f'Running Processes: {len(processes) - 1}')  

if __name__ == '__main__':
    main()
