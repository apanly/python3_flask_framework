#!/bin/sh

sync(){
    cmd="cd /data/www/pi3Robot/  ;  git fetch --all ; git reset --hard origin/master"
    echo "\033[32m"$cmd
    eval $cmd
    return 0
}

reload() {
    cmd="export ops_config='production' && /data/www/python3/bin/uwsgi --reload /data/www/logs/pirobot.pid"
    echo "\033[32m"$cmd
    eval $cmd
    return 0
}

case "$1" in
    sync)
        sync
        ;;
    start)
        ;;
    stop)
        ;;
    reload)
        reload
        ;;
    *)
        echo "Usage: sh release.sh {sync|start|stop|reload}" >&2
        exit 3
        ;;
esac