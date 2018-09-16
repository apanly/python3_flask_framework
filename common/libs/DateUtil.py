# -*- coding: utf-8 -*-
from __future__ import division
import datetime

def getCurrentTime( fmt =  "%Y-%m-%d %H:%M:%I",date = None ):
    if date is None:
        date = datetime.datetime.now()
    return date.strftime( fmt )

def getDateBefore(day=1):
    return datetime.date.today() - datetime.timedelta( days=day )

