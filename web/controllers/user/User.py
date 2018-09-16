# -*- coding: utf-8 -*-
from application import app
from flask import Blueprint,jsonify,make_response,request,redirect,g
from common.libs.Helper import ops_render


import json,smtplib
import common.libs.Helper
from  common.models.User import ( User )
from common.libs.UrlManager import ( UrlManager )

route_user = Blueprint('user_page', __name__)

@route_user.route("/login",methods = [ "GET","POST" ])
def Login( ):
    if request.method == "GET":

        if g.current_user:
            return  redirect( UrlManager.buildUrl("/") )
        return ops_render("user/login.html")

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    email = req['email'] if 'email' in req else ''
    pwd = req['pwd'] if 'pwd' in req else ''

    if  email is None or len( email ) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的邮箱~~"
        return jsonify( resp )

    if  pwd is None or len( pwd ) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的邮箱密码~~"
        return jsonify(resp)

    user_info = User.query.filter_by( email = email ).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "你好，未注册的邮箱，请找系统管理员先注册用户~~"
        return jsonify(resp)

    try:
        at_idx = email.index( "@" )
        smtpObj = smtplib.SMTP_SSL( "smtp." + email[ (at_idx +1): ],465 )
        smtpObj.set_debuglevel(1)
        smtpObj.login(email, pwd)
        smtpObj.close()
    except Exception:
        resp['code'] = -1
        resp['msg'] = "登录失败,请核对邮箱和密码是否对应~~"
        return jsonify(resp)
    response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~'}))
    response.set_cookie( app.config['AUTH_COOKIE_NAME'], '%s#%s' % ( common.libs.Helper.user_auth_code(user_info), user_info.id),  60 * 60 * 24 * 120)  # 保存120天
    return response

@route_user.route("/logout")
def LogOut(  ):
    response = make_response( redirect( UrlManager.buildUrl( "/user/login" ) ) )
    response.delete_cookie( app.config['AUTH_COOKIE_NAME'] )
    return response

