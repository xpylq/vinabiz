drop database if exists vinabiz;
create database vinabiz CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
use vinabiz;
DROP TABLE IF EXISTS `vinabiz_company`;
CREATE TABLE `vinabiz_company` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `guid` VARCHAR(256) NOT NULL COMMENT 'guid',
  `url` VARCHAR(256) NOT NULL COMMENT 'url',
  `official_name` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN ĐĂNG KÝ DOANH NGHIỆP',
  `trading_name` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN ĐĂNG KÝ DOANH NGHIỆP',
  `business_code` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN ĐĂNG KÝ DOANH NGHIỆP',
  `date_range` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN ĐĂNG KÝ DOANH NGHIỆP',
  `tax_authorities_manage` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN ĐĂNG KÝ DOANH NGHIỆP',
  `date_of_commencement_of_operation` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN ĐĂNG KÝ DOANH NGHIỆP',
  `status` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN ĐĂNG KÝ DOANH NGHIỆP',
  `office_address` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `phone1` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `fax` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `email` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `website` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `representative` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `phone2` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `representative_address` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `manager` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `phone_director` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `address_director` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `accountant` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `phone_accounting` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `account_address` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN LIÊN HỆ',
  `main_job` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN NGÀNH NGHỀ, LĨNH VỰC HOẠT ĐỘNG',
  `economic_field` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN NGÀNH NGHỀ, LĨNH VỰC HOẠT ĐỘNG',
  `type_of_economic` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN NGÀNH NGHỀ, LĨNH VỰC HOẠT ĐỘNG',
  `type_of_organization` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN NGÀNH NGHỀ, LĨNH VỰC HOẠT ĐỘNG',
  `class_chapters` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN NGÀNH NGHỀ, LĨNH VỰC HOẠT ĐỘNG',
  `item_type` VARCHAR(256) NOT NULL DEFAULT '' COMMENT 'THÔNG TIN NGÀNH NGHỀ, LĨNH VỰC HOẠT ĐỘNG',
   UNIQUE `idx_guid` (`guid`),
   UNIQUE  `idx_url` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司信息';