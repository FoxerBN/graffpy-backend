import time
from src.services.process_service import get_system_stats
from src.config.tinydb_config import daily_data_table


def store_hourly_data():
    """Function called by APScheduler every hour"""
    try:
        stats = get_system_stats()

        current_time = time.time()
        data_entry = {
            "timestamp": current_time,
            "cpu": stats["cpu"],
            "ram": stats["ram"],
            "cpu_temp": stats["cpu_temp"],
            "net": stats["net"],
            "disk": stats["disk"]
        }

        daily_data_table.insert(data_entry)
        print(f"✅ Hourly data stored at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        print(f"❌ Error storing hourly data: {e}")
