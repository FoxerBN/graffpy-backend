import time
from src.config.tinydb_config import db, weekly_stats_table,daily_data_table, Query


def generate_weekly_stats():
    try:
        all_daily_data = daily_data_table.all()

        if not all_daily_data:
            return {"message": "No data available"}

        # Extract values
        cpu_temps = [entry['cpu_temp'] for entry in all_daily_data if entry['cpu_temp'] is not None]
        cpu_percents = [entry['cpu_percent'] for entry in all_daily_data]
        ram_percents = [entry['ram_percent'] for entry in all_daily_data]

        stats = {
            "maxCpuTemp": str(max(cpu_temps)) if cpu_temps else "N/A",
            "avgCpuTemp": str(round(sum(cpu_temps) / len(cpu_temps), 1)) if cpu_temps else "N/A",
            "minCpuTemp": str(min(cpu_temps)) if cpu_temps else "N/A",
            "maxCpuPercent": str(max(cpu_percents)),
            "avgCpuPercent": str(round(sum(cpu_percents) / len(cpu_percents), 1)),
            "minCpuPercent": str(min(cpu_percents)),
            "maxRamPercent": str(max(ram_percents)),
            "avgRamPercent": str(round(sum(ram_percents) / len(ram_percents), 1)),
            "minRamPercent": str(min(ram_percents))
        }

        weekly_stats_table.insert(stats)
        return stats

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}