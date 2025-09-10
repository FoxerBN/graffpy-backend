from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .store_hourly_data import store_hourly_data
from .store_weekly_data import store_weekly_data

scheduler = BackgroundScheduler()


def start_scheduler():
    # Hourly data storage (every hour at :30)
    scheduler.add_job(
        func=store_hourly_data,
        trigger=CronTrigger(minute=30),
        id='hourly_data_storage',
        name='Store hourly system data',
        replace_existing=True
    )

    # Weekly data storage (every day at 23:55)
    scheduler.add_job(
        func=store_weekly_data,
        trigger=CronTrigger(hour=23, minute=55),
        id='weekly_data_storage',
        name='Store weekly stats and clear daily data',
        replace_existing=True
    )

    scheduler.start()
    print("✅ Scheduler started - hourly data storage job added (runs at :30)")
    print("✅ Scheduler started - weekly data storage job added (runs at 23:55)")


def shutdown_scheduler():
    scheduler.shutdown()
