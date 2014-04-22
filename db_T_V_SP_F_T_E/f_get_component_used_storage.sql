DELIMITER $$

USE `erp`$$

DROP FUNCTION IF EXISTS `f_get_component_used_storage`$$

CREATE DEFINER=`root`@`%` FUNCTION `f_get_component_used_storage`(_useExpand INT,comp_id VARCHAR(255)) RETURNS INT(11)
BEGIN
    DECLARE total INT;
    IF comp_id IS NOT NULL THEN
        IF _useExpand = 0 THEN
            SET total = (SELECT SUM(fromStorage) FROM tmp_order_analysis WHERE c = comp_id GROUP BY c);
        ELSEIF _useExpand = 1 THEN
            SET total = (SELECT SUM(fromStorage) FROM tmp_order_analysis2 WHERE c = comp_id GROUP BY c);
        END IF;
        IF total IS NULL THEN
            RETURN 0;
        ELSE 
            RETURN total;
        END IF;
    ELSE
        RETURN 0;
    END IF;
END$$

DELIMITER ;