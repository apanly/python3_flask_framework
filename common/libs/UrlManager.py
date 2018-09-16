# -*- coding: utf-8 -*-
from application import app
from common.libs.DateUtil import getCurrentTime

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s"%( getCurrentTime(  "%Y%m%d%H%M%I" ) )
        path =  "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl( path )

    @staticmethod
    def buildCdnPic(bucket,path,params,mode = 2):
        qiniu_config = app.config['QINIU']
        url = qiniu_config['domain'][ bucket ] + path
        weight = params['w'] if 'w' in params else 0
        height = params['h'] if 'h' in params else 0
        if weight and height:
            url += "?imageView2/{0}/w/{1}/h/{2}/interlace/1".format( mode,weight,height )
        elif weight:
            url += "?imageView2/{0}/w/{1}".format( mode,weight )
        elif height:
            url += "?imageView2/{0}/h/{1}".format( mode,height )
        return url