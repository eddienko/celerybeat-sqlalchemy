#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#=============================================================================
#     FileName: addtask
#         Desc:
#       Author: ge.jin
#        Email: ge.jin@woqutech.com
#     HomePage: wwww.woqutech.com
#      Version: 0.0.1
#   LastChange: 5/3/16 9:33 AM
#      History:
#=============================================================================
'''

from celery import Celery, current_app

app = Celery('celerybeat-sqlalchemy')
app.config_from_object('settings')
from model import PeriodicTask, CrontabSchedule, IntervalSchedule,  get_session
print current_app.conf.CELERYBEAT_MAX_LOOP_INTERVAL
session = get_session()
cs = CrontabSchedule(minute='*/5')
iss = IntervalSchedule(every=30, period='seconds')
session.add(cs)
# pt = PeriodicTask(name="sdisfsdffaf124asf", task="task_hello",  crontab=cs, interval=iss, args='[]', kwargs='{}')
pt = PeriodicTask(name="sd124asf", task="task_hello", interval=iss, args='[]', kwargs='{}')
session.add(pt)
session.flush()
