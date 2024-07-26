import psutil
import logging

logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0  
DISK_THRESHOLD = 80.0  

def monitor_cpu():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'CPU usage is high: {usage}%')

def monitor_memory():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        logging.warning(f'Memory usage is high: {memory.percent}%')

def monitor_disk():
    disk = psutil.disk_usage('C:\\')
    if disk.percent > DISK_THRESHOLD:
        logging.warning(f'Disk space usage is high: {disk.percent}%')

def main():
    monitor_cpu()
    monitor_memory()
    monitor_disk()

if __name__ == '__main__':
    main()
