from celery.schedules import crontab
from celery.task import periodic_task
from .models.user import User

@periodic_task(run_every=crontab(hour=00, minute=28))
def every_monday_morning():
    users = User.objects.all()
    for user in users:
        user.total_drunk_today = user.total_water_per_day
        user.save()