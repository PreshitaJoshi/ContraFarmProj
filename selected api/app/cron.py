
from apscheduler.schedulers.background import BackgroundScheduler
import time
from app.models import*
from app.views import*

def start():
  schedule=BackgroundScheduler(timezone="Asia/Kolkata")
  
  job=schedule.add_job(datafromsensor,'interval',seconds=60,id="check_id",replace_existing=True)
  schedule.start()
  print(job)

