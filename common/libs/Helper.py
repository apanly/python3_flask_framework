# -*- coding: utf-8 -*-
from __future__ import division
import hashlib,os,re,tempfile,datetime
from flask import render_template,g

'''
自定义分页类
'''
def iPagination( params ):
    import math

    ret = {
        "is_prev":1,
        "is_next":1,
        "from" :0 ,
        "end":0,
        "current":0,
        "total_pages":0,
        "page_size" : 0,
        "total" : 0,
        "url":params['url']
    }

    total = int( params['total'] )
    page_size = int( params['page_size'] )
    page = int( params['page'] )
    display = int( params['display'] )
    total_pages = int( math.ceil( total / page_size ) )
    total_pages = total_pages if total_pages > 0 else 1
    if page <= 1:
        ret['is_prev'] = 0

    if page >= total_pages:
        ret['is_next'] = 0

    semi = int( math.ceil( display / 2 ) )

    if page - semi > 0 :
        ret['from'] = page - semi
    else:
        ret['from'] = 1

    if page + semi <= total_pages :
        ret['end'] = page + semi
    else:
        ret['end'] = total_pages

    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['total'] = total
    ret['range'] = range( ret['from'],ret['end'] + 1 )
    return ret

'''
用户信息加密
'''
def user_auth_code(user_info):
    m = hashlib.md5()
    str = "%s-%s-%s-%s" % (user_info.id, user_info.email, user_info.salt,user_info.name)
    m.update(str.encode("utf-8"))
    return m.hexdigest()

'''
快速获取对象列表中的某个字段
selectFilterObj
'''

def selectFilterObj( obj,field ):
    ret = []
    for item in obj:
        if not hasattr(item, field ):
            break
        if getattr( item,field )  in ret:
            continue
        ret.append( getattr( item,field ) )
    return ret


def ops_render(  template, context = {} ):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template( template , **context)

'''
根据id字段获取一个dict出来
'''
def getDictFilterField( db_model,select_field,key_field,id_list ):
    ret = {}
    in_field = "%s__in"%select_field
    kwargs = {}
    kwargs[ in_field ] = id_list
    list = db_model.query.filter( **kwargs ).all()
    if not list:
        return ret

    for item in list:
        if not hasattr(item, key_field ):
            break
        ret[ getattr( item,key_field ) ] = item

    return ret


'''
写入文件
'''

def writeFile( file_path = None,data = None ):
    with open( file_path , 'wb') as f:
        f.write( data )