import time
from datetime import datetime
from src.services.weekly_service import generate_weekly_stats
from src.config.tinydb_config import daily_data_table, weekly_stats_table


def store_weekly_data():
    """Function called by APScheduler every day at 23:55"""
    try:
        # Get all daily records
        daily_records = daily_data_table.all()

        if len(daily_records) == 0:
            print("❌ No daily data available")
            return

        print(f"✅ Found {len(daily_records)} daily records, generating weekly stats...")

        # Generate and store weekly stats
        stats = generate_weekly_stats()

        if "error" not in stats:
            print(f"✅ Weekly stats stored at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            # Clear daily data for next day
            daily_data_table.truncate()
            print("✅ Daily data cleared for next day")

            # Keep only last 7 weekly records
            weekly_records = weekly_stats_table.all()
            if len(weekly_records) > 7:
                # Remove oldest records, keep only 7
                weekly_stats_table.truncate()
                for record in weekly_records[-7:]:
                    weekly_stats_table.insert(record)
                print(f"✅ Weekly stats trimmed to 7 records")
        else:
            print(f"❌ Error generating weekly stats: {stats['error']}")

    except Exception as e:
        print(f"❌ Error in store_weekly_data: {e}")
