# -*- coding: utf-8 -*-
SERVER_PORT = 8889
DEBUG = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
SQLALCHEMY_ECHO = False
SECRET_KEY = 'ZoDWffA2deeVOzii'

SEO = {
    'title':'Python3 + Flask 框架'
}


##
AUTH_COOKIE_NAME = "54php_cn_framework"


##过滤url
IGNORE_URLS = [
    "^/user/login",
    "^/user/logout",
    "^/api",
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

HTTP_TIMEOUT = 5