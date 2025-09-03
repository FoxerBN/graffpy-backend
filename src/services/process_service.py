import psutil
import time

def get_system_stats():
    # CPU %
    cpu_percent = psutil.cpu_percent(interval=1)

    # RAM
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_used_gb = ram.used / (1024 ** 3)
    ram_total_gb = ram.total / (1024 ** 3)

    # Disk
    disk = psutil.disk_usage('/')
    disk_free_gb = disk.free / (1024 ** 3)
    disk_total_gb = disk.total / (1024 ** 3)

    # CPU temperature
    temps = psutil.sensors_temperatures()
    cpu_temp = None
    if temps:
        for name, entries in temps.items():
            if any(key in name for key in ["coretemp", "k10temp", "cpu_thermal", "acpitz"]):
                cpu_temp = entries[0].current
                break

    # Internet speed
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()

    download_speed = (net2.bytes_recv - net1.bytes_recv) / 1024  # KB/s
    upload_speed = (net2.bytes_sent - net1.bytes_sent) / 1024    # KB/s

    return {
        "cpu": f"{cpu_percent}%",
        "ram": f"{ram_used_gb:.1f}/{ram_total_gb:.1f} GB ({ram_percent}%)",
        "disk": f"{disk_free_gb:.1f}/{disk_total_gb:.1f} GB free",
        "cpu_temp": f"{cpu_temp:.1f}°C" if cpu_temp is not None else "N/A",
        "net": f"↓ {download_speed:.1f} KB/s ↑ {upload_speed:.1f} KB/s"
    }