from src.config.tinydb_config import weekly_stats_table

def get_seven_days_data():
    try:
        all_records = weekly_stats_table.all()
        return all_records
    except Exception as e:
        return {"error": str(e)}
