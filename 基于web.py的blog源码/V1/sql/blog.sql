/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50540
Source Host           : localhost:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50540
File Encoding         : 65001

Date: 2016-03-21 14:39:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for entries
-- ----------------------------
DROP TABLE IF EXISTS `entries`;
CREATE TABLE `entries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text,
  `content` text,
  `posted_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of entries
-- ----------------------------
INSERT INTO `entries` VALUES ('1', '这是一个测试', '这是博客的第一个内容\r\n\r\n添加内容', '2016-03-21 06:28:16');
INSERT INTO `entries` VALUES ('2', '这是第二个', '这是第二个内容\r\n添加内容', '2016-03-21 06:33:31');
