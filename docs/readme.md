MiniPC拥有服务
==========
#### 安装的服务
* 操作系统
    * ubuntu 18.04
* 常用用户
    * 用户：vincent
* Nginx
    * sudo /etc/init.d/nginx start | stop | restart
* php-fpm
    * sudo /etc/init.d/php7.2-fpm start | stop | restart
* mysql
    * sudo /etc/init.d/mysql start | stop | restart
    * root 密码：空
    * www 密码：123456

* Nas存储
    * 软件：nextcloud（php）
    * 源码路径：/data/www/nextcloud
    * 存储内容位置：/data/nextcloud_data

* 家庭媒体
    * 软件：plex
    * 源码路径：/data/www/nextcloud
    * 服务操作命令
        * sudo service plexmediaserver status | stop | restart

* Git服务
    * 软件：gogs
    * 源码路径：/data/www/gogs
    * 仓库存储位置：/data/gogs-repositories
    * 启动 ：nohup /data/www/gogs/gogs web > /tmp/gogs.log &


* Python 家控服务
    * 环境
        * python3.6
        * sudo apt-get install libmysqlclient-dev
        * pip3 install virtualenv
        * virtualenv --no-setuptools  --no-pip --no-wheel  -p /usr/bin/python3.6 /data/www/python3

* 公司VPN
    * 公司内网：cd /data/soft/openvpn/guowei_company && sudo openvpn --config /data/soft/openvpn/guowei_company/complete.ovpn --daemon
    * 公司阿里云：cd /data/soft/openvpn/guowei_aliyun && sudo openvpn --config /data/soft/openvpn/guowei_aliyun/complete.ovpn --daemon

* DNS服务
    * 软件：bind9
    * 服务命令
        * sudo /etc/init.d/bind9 start | stop | restart
    * [域名配置文件:位置/etc/bind](./bind9)

* 备份数据库
    * mysqldump -uroot -p gogs > /data/www/backup/gogs.sql
    * mysqldump -uroot -p nextcloud > /data/www/backup/nextcloud.sql
    * mysqldump -uroot -p pi3Robot > /data/www/backup/pi3Robot.sql

* shadowsocks
    * [ss 命令行客户端配置](./shadowsocks)
    * [命令行模式如何FQ](./shadowsocks)

* 蓝牙
    * sudo apt-get install pulseaudio pulseaudio-module-bluetooth
    * 参考资料
        * http://ju.outofmemory.cn/entry/262181
        * https://bbs.hassbian.com/thread-1341-1-1.html
        * https://www.jb51.net/LINUXjishu/379648.html
* text2Sound(tts)
    * sudo aptitude install espeak libespeak-dev gespeaker -y
    * espeak -vzh "你好"




