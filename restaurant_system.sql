/*
 Navicat MySQL Data Transfer

 Source Server         : mini
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : restaurant_system

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 07/02/2023 12:39:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer`  (
  `C_id` int(0) NOT NULL AUTO_INCREMENT,
  `C_password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `C_name` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `C_sex` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '男' COMMENT '顾客性别',
  `C_phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `C_address` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`C_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '顾客' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES (1, '123456', '客人1号', '男', '12345678910', '地址1');

-- ----------------------------
-- Table structure for food_table
-- ----------------------------
DROP TABLE IF EXISTS `food_table`;
CREATE TABLE `food_table`  (
  `T_id` int(0) NOT NULL AUTO_INCREMENT,
  `T_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `T_content` int(0) NOT NULL,
  `T_status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '空' COMMENT '餐桌状态',
  PRIMARY KEY (`T_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '餐桌' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of food_table
-- ----------------------------
INSERT INTO `food_table` VALUES (1, '1号雅座', 4, '空');
INSERT INTO `food_table` VALUES (3, '外卖', 999, '空');

-- ----------------------------
-- Table structure for group_menus_content
-- ----------------------------
DROP TABLE IF EXISTS `group_menus_content`;
CREATE TABLE `group_menus_content`  (
  `Men_M_id` int(0) NULL DEFAULT NULL,
  `M_id` int(0) NULL DEFAULT NULL,
  INDEX `FK_Relationship_1`(`M_id`) USING BTREE,
  INDEX `FK_Relationship_3`(`Men_M_id`) USING BTREE,
  CONSTRAINT `FK_Relationship_1` FOREIGN KEY (`M_id`) REFERENCES `menus2` (`M_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Relationship_3` FOREIGN KEY (`Men_M_id`) REFERENCES `menus2` (`M_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '套餐内容' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of group_menus_content
-- ----------------------------
INSERT INTO `group_menus_content` VALUES (5, 1);
INSERT INTO `group_menus_content` VALUES (5, 2);
INSERT INTO `group_menus_content` VALUES (6, 1);
INSERT INTO `group_menus_content` VALUES (6, 3);
INSERT INTO `group_menus_content` VALUES (6, 2);

-- ----------------------------
-- Table structure for menus2
-- ----------------------------
DROP TABLE IF EXISTS `menus2`;
CREATE TABLE `menus2`  (
  `M_id` int(0) NOT NULL AUTO_INCREMENT,
  `M_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `M_original_price` float NOT NULL,
  `M_discount` float NOT NULL,
  `M_class` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '饭菜分类',
  `M_sum_number` int(0) NULL DEFAULT 0,
  PRIMARY KEY (`M_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '菜谱' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of menus2
-- ----------------------------
INSERT INTO `menus2` VALUES (1, '米饭', 2.5, 1, '主食', 0);
INSERT INTO `menus2` VALUES (2, '鱼香肉丝', 5.5, 1, '荤菜', 0);
INSERT INTO `menus2` VALUES (3, '炒豆芽', 3.5, 1, '素菜', 1);
INSERT INTO `menus2` VALUES (4, '面条', 2.5, 1, '主食', 0);
INSERT INTO `menus2` VALUES (5, '套餐1', 7, 1, '主食', 1);
INSERT INTO `menus2` VALUES (6, '套餐2', 5, 1, '主食', 1);

-- ----------------------------
-- Table structure for order_menus
-- ----------------------------
DROP TABLE IF EXISTS `order_menus`;
CREATE TABLE `order_menus`  (
  `O_id` int(0) NULL DEFAULT NULL,
  `M_id` int(0) NULL DEFAULT NULL,
  INDEX `FK_Relationship_4`(`O_id`) USING BTREE,
  INDEX `FK_Relationship_5`(`M_id`) USING BTREE,
  CONSTRAINT `FK_Relationship_4` FOREIGN KEY (`O_id`) REFERENCES `ordering` (`O_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Relationship_5` FOREIGN KEY (`M_id`) REFERENCES `menus2` (`M_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '订单内容' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order_menus
-- ----------------------------
INSERT INTO `order_menus` VALUES (1, 5);
INSERT INTO `order_menus` VALUES (1, 3);

-- ----------------------------
-- Table structure for ordering
-- ----------------------------
DROP TABLE IF EXISTS `ordering`;
CREATE TABLE `ordering`  (
  `O_id` int(0) NOT NULL AUTO_INCREMENT,
  `C_id` int(0) NOT NULL,
  `T_id` int(0) NULL DEFAULT NULL,
  `R_id` int(0) NULL DEFAULT NULL,
  `O_time` datetime(0) NOT NULL,
  `O_commit` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `O_delete_status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `O_make_status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `O_eat_status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`O_id`) USING BTREE,
  INDEX `FK_Relationship_6`(`C_id`) USING BTREE,
  INDEX `FK_Relationship_7`(`R_id`) USING BTREE,
  INDEX `FK_Relationship_8`(`T_id`) USING BTREE,
  CONSTRAINT `FK_Relationship_6` FOREIGN KEY (`C_id`) REFERENCES `customer` (`C_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Relationship_7` FOREIGN KEY (`R_id`) REFERENCES `rider` (`R_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Relationship_8` FOREIGN KEY (`T_id`) REFERENCES `food_table` (`T_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '订单' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of ordering
-- ----------------------------
INSERT INTO `ordering` VALUES (1, 1, 1, 1, '2022-12-06 04:24:14', '无', '无法撤销', '制作完成', '已完成');

-- ----------------------------
-- Table structure for rider
-- ----------------------------
DROP TABLE IF EXISTS `rider`;
CREATE TABLE `rider`  (
  `R_id` int(0) NOT NULL AUTO_INCREMENT,
  `R_password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `R_name` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `R_sex` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `R_phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `R_health_status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`R_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '外卖员' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rider
-- ----------------------------
INSERT INTO `rider` VALUES (0, '0', '0', '0', '0', '0');
INSERT INTO `rider` VALUES (1, '123456', '骑手1号', '男', '11111111111', '健康');

-- ----------------------------
-- Table structure for waiter
-- ----------------------------
DROP TABLE IF EXISTS `waiter`;
CREATE TABLE `waiter`  (
  `W_id` int(0) NOT NULL AUTO_INCREMENT,
  `W_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `W_sex` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `W_age` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '员工年龄',
  `W_phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `W_work_status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '在岗',
  `W_health_status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '健康',
  PRIMARY KEY (`W_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '服务员' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of waiter
-- ----------------------------
INSERT INTO `waiter` VALUES (1, '店员1号', '男', '21', '11122233311', '在岗', '健康');

-- ----------------------------
-- View structure for count
-- ----------------------------
DROP VIEW IF EXISTS `count`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `count` AS select `order_menus`.`M_id` AS `M_id`,count(`order_menus`.`M_id`) AS `count(order_menus.M_id)` from `order_menus` group by `order_menus`.`M_id`;

-- ----------------------------
-- View structure for menus
-- ----------------------------
DROP VIEW IF EXISTS `menus`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `menus` AS select `menus2`.`M_id` AS `M_id`,`menus2`.`M_name` AS `M_name`,`menus2`.`M_original_price` AS `M_original_price`,`menus2`.`M_discount` AS `M_discount`,(`menus2`.`M_original_price` * `menus2`.`M_discount`) AS `M_present_price`,`menus2`.`M_class` AS `M_class`,`menus2`.`M_sum_number` AS `M_sum_number` from `menus2`;

-- ----------------------------
-- View structure for 套餐
-- ----------------------------
DROP VIEW IF EXISTS `套餐`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `套餐` AS select `menus`.`M_id` AS `M_id`,`menus`.`M_name` AS `M_name`,`menus`.`M_original_price` AS `M_original_price`,`menus`.`M_discount` AS `M_discount`,`menus`.`M_present_price` AS `M_present_price`,`menus`.`M_class` AS `M_class`,`menus`.`M_sum_number` AS `M_sum_number` from `menus` where `menus`.`M_id` in (select `group_menus_content`.`Men_M_id` AS `Men_M_id` from `group_menus_content` group by `group_menus_content`.`Men_M_id`);

-- ----------------------------
-- View structure for 套餐菜单
-- ----------------------------
DROP VIEW IF EXISTS `套餐菜单`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `套餐菜单` AS select `group_menus_content`.`Men_M_id` AS `Men_M_id`,`menus`.`M_id` AS `M_id`,`menus`.`M_name` AS `M_name`,`menus`.`M_original_price` AS `M_original_price`,`menus`.`M_discount` AS `M_discount`,`menus`.`M_present_price` AS `M_present_price`,`menus`.`M_class` AS `M_class` from (`group_menus_content` join `menus` on((`group_menus_content`.`M_id` = `menus`.`M_id`)));

-- ----------------------------
-- View structure for 快递订单
-- ----------------------------
DROP VIEW IF EXISTS `快递订单`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `快递订单` AS select `ordering`.`O_id` AS `O_id`,`ordering`.`O_time` AS `O_time`,`customer`.`C_address` AS `C_address`,`customer`.`C_name` AS `C_name`,`customer`.`C_phone` AS `C_phone`,`ordering`.`O_commit` AS `O_commit`,`ordering`.`O_delete_status` AS `O_delete_status`,`ordering`.`O_make_status` AS `O_make_status`,`ordering`.`O_eat_status` AS `O_eat_status`,`ordering`.`R_id` AS `R_id`,`rider`.`R_name` AS `R_name`,`ordering`.`T_id` AS `T_id` from ((`ordering` join `customer` on((`ordering`.`C_id` = `customer`.`C_id`))) join `rider` on((`ordering`.`R_id` = `rider`.`R_id`))) where (`ordering`.`T_id` = 3);



-- ----------------------------
-- View structure for 统计2
-- ----------------------------
DROP VIEW IF EXISTS `统计2`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `统计2` AS select `menus2`.`M_id` AS `M_id`,`menus2`.`M_name` AS `M_name`,`menus2`.`M_original_price` AS `M_original_price`,`menus2`.`M_sum_number` AS `M_sum_number`,(`menus2`.`M_original_price` * `menus2`.`M_sum_number`) AS `M_sum_price` from `menus2`;

-- ----------------------------
-- View structure for 总毛利润
-- ----------------------------
DROP VIEW IF EXISTS `总毛利润`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `总毛利润` AS select sum(`统计2`.`M_sum_price`) AS `gross_profit` from `统计2`;

-- ----------------------------
-- View structure for 菜谱
-- ----------------------------
DROP VIEW IF EXISTS `菜谱`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `菜谱` AS select `menus`.`M_id` AS `M_id`,`menus`.`M_name` AS `M_name`,`menus`.`M_original_price` AS `M_original_price`,`menus`.`M_discount` AS `M_discount`,`menus`.`M_present_price` AS `M_present_price`,`menus`.`M_class` AS `M_class`,`menus`.`M_sum_number` AS `M_sum_number` from (`menus` left join `group_menus_content` on((`menus`.`M_id` = `group_menus_content`.`Men_M_id`))) where (`group_menus_content`.`Men_M_id` is null);

-- ----------------------------
-- View structure for 订单
-- ----------------------------
DROP VIEW IF EXISTS `订单`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `订单` AS select `ordering`.`O_id` AS `O_id`,`ordering`.`O_time` AS `O_time`,`ordering`.`O_commit` AS `O_commit`,`ordering`.`O_delete_status` AS `O_delete_status`,`ordering`.`O_make_status` AS `O_make_status`,`ordering`.`O_eat_status` AS `O_eat_status` from `ordering`;

-- ----------------------------
-- View structure for 订单总价
-- ----------------------------
DROP VIEW IF EXISTS `订单总价`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `订单总价` AS select `order_menus`.`O_id` AS `O_id`,sum(`menus`.`M_present_price`) AS `sum(menus.M_present_price)` from (`order_menus` join `menus` on((`order_menus`.`M_id` = `menus`.`M_id`))) group by `order_menus`.`O_id`;

-- ----------------------------
-- View structure for 订单2
-- ----------------------------
DROP VIEW IF EXISTS `订单2`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `订单2` AS select `ordering`.`O_id` AS `O_id`,`ordering`.`O_time` AS `O_time`,`customer`.`C_name` AS `C_name`,`customer`.`C_phone` AS `C_phone`,`food_table`.`T_name` AS `T_name`,`food_table`.`T_status` AS `T_status`,`ordering`.`O_delete_status` AS `O_delete_status`,`ordering`.`O_commit` AS `O_commit`,`ordering`.`O_make_status` AS `O_make_status`,`rider`.`R_name` AS `R_name`,`rider`.`R_phone` AS `R_phone`,`ordering`.`O_eat_status` AS `O_eat_status`,`订单总价`.`sum(menus.M_present_price)` AS `sum(menus.M_present_price)` from ((((`ordering` join `customer` on((`ordering`.`C_id` = `customer`.`C_id`))) join `food_table` on((`ordering`.`T_id` = `food_table`.`T_id`))) join `rider` on((`ordering`.`R_id` = `rider`.`R_id`))) join `订单总价` on((`ordering`.`O_id` = `订单总价`.`O_id`)));

-- ----------------------------
-- View structure for 统计1
-- ----------------------------
DROP VIEW IF EXISTS `统计1`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `统计1` AS select `订单2`.`O_id` AS `O_id`,`订单2`.`O_time` AS `O_time`,`订单2`.`sum(menus.M_present_price)` AS `M_sum_profit`,`订单2`.`O_make_status` AS `O_make_status` from `订单2`;

-- ----------------------------
-- View structure for 订单3
-- ----------------------------
DROP VIEW IF EXISTS `订单3`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `订单3` AS select `ordering`.`O_id` AS `O_id`,`ordering`.`O_time` AS `O_time`,`customer`.`C_phone` AS `C_phone`,`food_table`.`T_name` AS `T_name`,`food_table`.`T_status` AS `T_status`,`ordering`.`O_delete_status` AS `O_delete_status`,`ordering`.`O_commit` AS `O_commit`,`ordering`.`O_make_status` AS `O_make_status`,`rider`.`R_name` AS `R_name`,`rider`.`R_phone` AS `R_phone`,`ordering`.`O_eat_status` AS `O_eat_status`,`订单总价`.`sum(menus.M_present_price)` AS `sum(menus.M_present_price)`,`customer`.`C_id` AS `C_id` from ((((`ordering` join `customer` on((`ordering`.`C_id` = `customer`.`C_id`))) join `food_table` on((`ordering`.`T_id` = `food_table`.`T_id`))) join `rider` on((`ordering`.`R_id` = `rider`.`R_id`))) join `订单总价` on((`ordering`.`O_id` = `订单总价`.`O_id`)));

-- ----------------------------
-- View structure for 订单菜谱
-- ----------------------------
DROP VIEW IF EXISTS `订单菜谱`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `订单菜谱` AS select `ordering`.`O_id` AS `O_id`,`menus`.`M_name` AS `M_name`,`menus`.`M_original_price` AS `M_original_price`,`menus`.`M_discount` AS `M_discount`,`menus`.`M_present_price` AS `M_present_price` from ((`ordering` join `order_menus` on((`order_menus`.`O_id` = `ordering`.`O_id`))) join `menus` on((`order_menus`.`M_id` = `menus`.`M_id`)));

SET FOREIGN_KEY_CHECKS = 1;
