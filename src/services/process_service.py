import psutil
import time
import random
from src.config.tinydb_config import daily_data_table
from tinydb import Query

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
    time.sleep(2)
    net2 = psutil.net_io_counters()

    download_speed = (net2.bytes_recv - net1.bytes_recv) / 1024  # KB/s
    upload_speed = (net2.bytes_sent - net1.bytes_sent) / 1024    # KB/s

    # Store daily data with unique identifier
    current_time = time.time()
    data_entry = {
        "timestamp": current_time,
        "unique_id": f"{current_time}_{random.randint(1000, 9999)}",  # Ensure uniqueness
        "cpu_percent": round(cpu_percent, 1),
        "ram_percent": round(ram_percent, 1),
        "cpu_temp": round(cpu_temp, 1) if cpu_temp is not None else None,
        "download_speed_kbs": round(download_speed, 1),
        "upload_speed_kbs": round(upload_speed, 1)
    }

    try:
        # Use upsert to avoid duplicate ID issues
        Query_obj = Query()
        daily_data_table.upsert(data_entry, Query_obj.unique_id == data_entry["unique_id"])
    except Exception as e:
        print(f"Warning: Failed to store data in database: {e}")
        # Try simple insert as fallback
        try:
            daily_data_table.insert(data_entry)
        except Exception as e2:
            print(f"Warning: Fallback insert also failed: {e2}")

    return {
        "cpu": f"{cpu_percent}%",
        "ram": f"{ram_percent}%,{ram_used_gb:.1f}/{ram_total_gb:.1f} GB",
        "disk": f"{disk_free_gb:.1f}/{disk_total_gb:.1f}",
        "cpu_temp": f"{cpu_temp:.1f}°C" if cpu_temp is not None else "N/A",
        "net": f"↓ {download_speed:.1f} KB/s ↑ {upload_speed:.1f} KB/s"
    }