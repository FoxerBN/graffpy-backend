import psutil

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

    return {
        "cpu": f"{cpu_percent}%",
        "ram": f"{ram_used_gb:.1f}/{ram_total_gb:.1f} GB ({ram_percent}%)",
        "disk": f"{disk_free_gb:.1f}/{disk_total_gb:.1f} GB free"
    }
