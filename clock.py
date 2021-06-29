from apscheduler.schedulers.blocking import BlockingScheduler
from telegramConnect import runScheduler, job_function
import datetime

#get IST
tzIST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

#Schedule the message
sched = BlockingScheduler()

# Schedule job_function to be called every day
# sched.add_job(runScheduler, 'interval', seconds=10)
sched.add_job(runScheduler, 'cron', day_of_week='mon-fri', hour=3, minute=35, timezone=tzIST)

#log scheduler
sched.add_job(job_function, 'interval', minutes=1)

def job_function():
    print("Scheduling working check (" + str(datetime.datetime.now()) +"): Success ")

sched.start()