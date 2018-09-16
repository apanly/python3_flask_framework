;
var common_ops = {
    init:function(){
       this.eventBind();
       this.setMenuHighLight();
    },
    eventBind:function(){

    },
    setMenuHighLight:function(){
        if( $(".top_nav_wrap .menu_wrap li.menu").length < 1 ){
            return;
        }

        var pathname = window.location.pathname;
        var nav_name = "default";

        if(  pathname.indexOf("/ent/") > -1  ){
            nav_name = "ent";
        }
        if( nav_name == null ){
            return;
        }
        $(".top_nav_wrap .menu_wrap li.menu_" + nav_name ).addClass("active");
    },
    buildUrl:function( path ,params ){
        var url = "" + path;
        var _paramUrl = "";
        if(  params ){
            _paramUrl = Object.keys( params ).map( function( k ){
                return [ encodeURIComponent( k ),encodeURIComponent( params[ k ] ) ].join("=");
            }).join("&");
            _paramUrl = "?" + _paramUrl;
        }
        return url + _paramUrl;
    },
    buildCdnPic:function( bucket,path,params ){
        var url = "http://cdn." + bucket + ".54php.cn" + path;
        var weight = 0;
        var height = 0;
        if( params && params.hasOwnProperty('w') ){
            weight = params['w'];
        }

        if( params && params.hasOwnProperty('h') ){
            height = params['h'];
        }

        if( weight && height ){
            url = url + "?imageView2/2/w/" + weight + "/h/" + height +  "/interlace/1";
        }else if( weight ){
            url = url + "?imageView2/2/w/" + weight;
        }else if( height ){
            url = url + "?imageView2/2/h/" + height;
        }
        return url;
    },
    alert:function( msg ,cb ){
        layer.alert( msg,{
            yes:function( index ){
                if( typeof cb == "function" ){
                    cb();
                }
                layer.close( index );
            }
        });
    },
    confirm:function( msg,callback ){
        callback = ( callback != undefined )?callback: { 'ok':null, 'cancel':null };
        layer.confirm( msg , {
            btn: ['确定','取消'] //按钮
        }, function( index ){
            //确定事件
            if( typeof callback.ok == "function" ){
                callback.ok();
            }
            layer.close( index );
        }, function( index ){
            //取消事件
            if( typeof callback.cancel == "function" ){
                callback.cancel();
            }
            layer.close( index );
        });
    },
    tip:function( msg,target ){
        layer.tips( msg, target, {
            tips: [ 3, '#e5004f']
        });
        $('html, body').animate({
            scrollTop: target.offset().top - 10
        }, 100);
    }
};

$(document).ready(function () {
    common_ops.init();
});


// 对Date的扩展，将 Date 转化为指定格式的String
// 月(M)、日(d)、小时(h)、分(m)、秒(s)、季度(q) 可以用 1-2 个占位符，
// 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字)
// 例子：
// (new Date()).Format("yyyy-MM-dd hh:mm:ss.S") ==> 2006-07-02 08:09:04.423
// (new Date()).Format("yyyy-M-d h:m:s.S")      ==> 2006-7-2 8:9:4.18
Date.prototype.Format = function(fmt)
{ //author: meizz
    var o = {
        "M+" : this.getMonth()+1,                 //月份
        "d+" : this.getDate(),                    //日
        "h+" : this.getHours(),                   //小时
        "m+" : this.getMinutes(),                 //分
        "s+" : this.getSeconds(),                 //秒
        "q+" : Math.floor((this.getMonth()+3)/3), //季度
        "S"  : this.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt))
        fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
    for(var k in o)
        if(new RegExp("("+ k +")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
    return fmt;
};
