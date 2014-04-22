DELIMITER $$

USE `erp`$$

DROP FUNCTION IF EXISTS `get_component_actual_storage2`$$

CREATE DEFINER=`root`@`%` FUNCTION `get_component_actual_storage2`(comp_id VARCHAR(255), _useActualStorage INT) RETURNS INT(11)
BEGIN
    DECLARE total INT;
    IF _useActualStorage = 0 THEN
        IF comp_id IS NOT NULL THEN
            SET total = (SELECT SUM(actual_count) FROM ent_rel_storage_item WHERE item_number=comp_id  AND(d_time IS NULL OR d_time>NOW()) GROUP BY item_number);
            IF total IS NULL THEN
                RETURN 0;
            ELSE 
                RETURN total;
            END IF;
        ELSE
            RETURN 0;
        END IF;
    END IF;
    IF _useActualStorage = 1 THEN 
        RETURN 0;
    END IF;
    END$$

DELIMITER ;