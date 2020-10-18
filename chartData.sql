-- --------------------------------------------------------
-- 호스트:                          223.194.46.212
-- 서버 버전:                        10.4.6-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 테이블 cidb.inventory2009 구조 내보내기
CREATE TABLE IF NOT EXISTS `inventory2009` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bsnscd` varchar(255) DEFAULT NULL,
  `measures` varchar(255) DEFAULT NULL,
  `yyyymmdd` varchar(255) DEFAULT NULL,
  `inv_init` int(11) DEFAULT NULL,
  `inv_close` int(11) DEFAULT NULL,
  `inv_input` int(11) DEFAULT NULL,
  `inv_output` int(11) DEFAULT NULL,
  `inv_rate` float DEFAULT NULL,
  `invrate_predict` float DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=361 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- 내보낼 데이터가 선택되어 있지 않습니다.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
