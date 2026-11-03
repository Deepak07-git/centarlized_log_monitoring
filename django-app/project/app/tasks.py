from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events

from .services import process_and_store_logs


def start_scheduler():
    """Schedule deterministic rule-based log processing."""
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(
        process_and_store_logs,
        trigger=IntervalTrigger(minutes=1),
        id="process_and_store_logs",
        max_instances=1,
        replace_existing=True,
    )
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started. Monitoring logs with rule-based threat detection.")
