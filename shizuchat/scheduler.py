# scheduler.py
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import config

TIME_ZONE = pytz.timezone(config.TIME_ZONE)
scheduler = AsyncIOScheduler(timezone=TIME_ZONE)
