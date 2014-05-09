DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `sp_analysis_update_halfStorage2`$$

CREATE DEFINER=`root`@`%` PROCEDURE `sp_analysis_update_halfStorage2`()
BEGIN
    DECLARE _id INT(11);
    DECLARE _c VARCHAR(255);
    DECLARE _halfStorage INT(11);
    DECLARE _found BOOLEAN DEFAULT TRUE;
    DECLARE p_cursor CURSOR FOR SELECT DISTINCT(c) FROM tmp_order_analysis2;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET _found=FALSE;
    
    OPEN p_cursor;
    FETCH p_cursor INTO _c;
    WHILE _found DO
        SET _halfStorage = (SELECT f_get_component_half_storage(_c));
        UPDATE tmp_order_analysis2 SET halfStorage = _halfStorage WHERE c = _c;
        FETCH p_cursor INTO _c;
    END WHILE ;
    CLOSE p_cursor;
END$$

DELIMITER ;