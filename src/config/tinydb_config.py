import os
from tinydb import TinyDB, Query

db_dir = 'database'
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Correct path to database folder
db = TinyDB('database/db.json')
weekly_db = TinyDB('database/weekly_stats.json')

daily_data_table = db.table('daily_data')
weekly_stats_table = weekly_db.table('weekly_stats')

Query = Query