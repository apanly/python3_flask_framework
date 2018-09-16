编程浪子pi3Robot控制系统
=================================
## QuickStart
* Python3
* pip install -r requirements.txt

## 启动
* 启动web服务
    * export ops_config="local|production" && python manage.py runserver
* 启动Job
    * export ops_config="local|production" && python manage.py runjob -m test



## 相关文档
* [Flask参考文档](./docs/flask.md)

## 问题处理
* 安装 MySQL-python ，结果出错 ImportError: No module named 'ConfigParser'

        在 Python 3.x 版本后，ConfigParser.py 已经更名为 configparser.py 所以出错！
        解决方法：pip install mysqlclient