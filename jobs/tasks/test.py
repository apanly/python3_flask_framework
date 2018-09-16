# -*- coding: utf-8 -*-
from application import  app

'''
python manage.py runjob -m test
'''

class JobTask():
    def __init__(self):
        pass

    def run(self, params):
        app.logger.info( params )