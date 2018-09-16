;
//引入Plupload 、qiniu.js后
var qiniu_upload_ops = {
    init:function( callback ){
        callback = ( callback != undefined )?callback: { 'success':null, 'error':null };

        var uploader = Qiniu.uploader({
        runtimes: 'html5,flash,html4',    //上传模式,依次退化
        browse_button: 'avatar',       //上传选择的点选按钮，**必需**
        uptoken_url: '/qiniu/token',            //Ajax请求upToken的Url，**强烈建议设置**（服务端提供）
        domain: 'http://qiniu-plupload.qiniudn.com/',   //bucket 域名，下载资源时用到，**必需**
        get_new_uptoken: true,  //设置上传文件的时候是否每次都重新获取新的token
        max_file_size: '100mb',           //最大文件体积限制
        flash_swf_url: 'js/plupload/Moxie.swf',  //引入flash,相对路径
        max_retries: 3,                   //上传失败最大重试次数
        dragdrop: true,                   //开启可拖曳上传
        chunk_size: '2mb',                //分块上传时，每片的体积
        auto_start: true, //选择文件后自动上传，若关闭需要自己绑定事件触发上传
        filters: {
          mime_types : [
            {title : "Image files", extensions: "jpg,jpeg,png"}
          ]
        },
        init: {
            'FilesAdded': function(up, files) {
                plupload.each(files, function(file) {
                    // 文件添加进队列后,处理相关的事情
                });
            },
            'BeforeUpload': function(up, file) {
                // 每个文件上传前,处理相关的事情
            },
            'UploadProgress': function(up, file) {
                // 每个文件上传时,处理相关的事情
            },
            'FileUploaded': function(up, file, info) {
                if( typeof callback.success == "function" ){
                    var res = jQuery.parseJSON( info.response );
                    callback.success( res );
                }
            },
            'Error': function(up, err, errTip) {
                //上传出错时,处理相关的事情
                if( typeof callback.error == "function" ){
                    callback.error( err );
                }
            },
            'UploadComplete': function() {
                //队列文件处理完毕后,处理相关的事情
            },
            'Key': function(up, file) {
                // 若想在前端对每个文件的key进行个性化处理，可以配置该函数
                // 该配置必须要在 unique_names: false , save_key: false 时才生效
                var file_name = file.name;
                var index1 = file_name.lastIndexOf(".");
                var index2 = file_name.length;
                var suffix = file_name.substring(index1+1,index2);
                var timestamp = new Date().getTime();
                var qiniu_file_key =  "pirobot/" + ( new Date() ).Format("yyyyMMdd") + "/" + timestamp + "." + suffix;
                return qiniu_file_key;
            }
        }
    });
    }
};
