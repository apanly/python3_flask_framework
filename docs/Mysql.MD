# 数据库变更历史
## 2018-05-16

       CREATE DATABASE `flask_framework` DEFAULT CHARACTER SET = `utf8mb4`;
       
       CREATE TABLE `user` (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
          `name` varchar(20) NOT NULL DEFAULT '' COMMENT '用户名',
          `email` varchar(50) NOT NULL DEFAULT '' COMMENT '邮箱地址也是登录用户名',
          `salt` varchar(64) NOT NULL DEFAULT '' COMMENT '随机码',
          `update_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
          `create_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '插入时间',
          PRIMARY KEY (`id`),
          KEY `idx_email` (`email`)
       ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
       
       INSERT INTO `user` (`id`, `name`, `email`, `salt`, `update_time`, `create_time`) VALUES
	(1, '郭威', 'apanly@163.com', 'HRD60OnSkN4dpCDH', '2018-05-16 23:50:43', '2018-05-16 23:50:43');

