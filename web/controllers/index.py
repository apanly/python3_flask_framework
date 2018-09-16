# -*- coding: utf-8 -*-
from flask import Blueprint,g
import subprocess,os
from common.libs.Helper import ops_render

route_index = Blueprint('index_page', __name__)

@route_index.route("/")
def index():
    cpu_temp = 0
    gpu_temp = 0
    file_path = "/sys/class/thermal/thermal_zone0/temp"
    file_gpu_path = "/opt/vc/bin/vcgencmd measure_temp"
    if os.path.exists( file_path ):
        tempFile = open( file_path )
        cpu_temp = tempFile.read()
        tempFile.close()

    if os.path.exists( file_gpu_path ):
        cpu_temp = float(cpu_temp)/1000
        ret_code,gpu_temp = subprocess.getstatusoutput( file_gpu_path )
        gpu_temp = gpu_temp.replace('temp=', '').replace('\'C', '')
        gpu_temp =  float(gpu_temp)
    return ops_render( "index/index.html",{ "cpu":cpu_temp,"gpu":gpu_temp }  )