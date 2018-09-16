# -*- coding: utf-8 -*-

from application import app
from flask import Flask,request,redirect,g

from common.models.User import ( User )
import common.libs.Helper
from common.libs.UrlManager import ( UrlManager )
import re

@app.before_request
def before_request():
    ignore_urls  = app.config['IGNORE_URLS']
    ignore_check_login_urls  = app.config['IGNORE_CHECK_LOGIN_URLS']
    method = request.method.lower()
    path = request.path

    #如果是静态文件就不要查询用户信息了
    pattern = re.compile('%s' % "|".join( ignore_check_login_urls ) )
    if pattern.match( path ):
        return

    #多查询一次数据也没有什么问题
    user_info = check_login()
    g.current_user = None
    if user_info:
        g.current_user = user_info

    #将忽略数组换成字符串

    pattern = re.compile('%s' % "|".join( ignore_urls ) )
    if pattern.match( path ):
        return

    if not user_info :
        return redirect( UrlManager.buildUrl( "/user/login" ) )

    return


@app.after_request
def after_request( response ):
    return response


def check_login( ):
        cookies = request.cookies
        auth_cookie = cookies[ app.config['AUTH_COOKIE_NAME'] ] if app.config['AUTH_COOKIE_NAME'] in cookies else None
        if auth_cookie is None:
            return False

        auth_info = auth_cookie.split( "#" )
        if len( auth_info ) != 2:
            return False

        try:
            user_info = User.query.filter_by( id = auth_info[1] ).first()
        except Exception:
            return False

        if user_info is None:
            return False

        if common.libs.Helper.user_auth_code( user_info ) != auth_info[ 0 ]:
            return False

        return user_info