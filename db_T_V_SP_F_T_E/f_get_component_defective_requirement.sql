DELIMITER $$

USE `erp`$$

DROP FUNCTION IF EXISTS `f_get_component_future_storage`$$

CREATE DEFINER=`root`@`%` FUNCTION `f_get_component_future_storage`(comp_id VARCHAR(255), _useFutureStorage INT) RETURNS INT(11)
BEGIN
    DECLARE total INT;
    IF _useFutureStorage = 0 THEN
        IF comp_id IS NOT NULL THEN
            SET total = (SELECT SUM(future_count) FROM ent_rel_storage_item WHERE item_number=comp_id AND (d_time IS NULL OR d_time>NOW()) GROUP BY item_number);
            IF total IS NULL THEN
                RETURN 0;
            ELSE 
                RETURN total;
            END IF;
        ELSE
            RETURN 0;
        END IF;
    END IF;
    IF _useFutureStorage = 1 THEN 
        RETURN 0;
    END IF;
    END$$

DELIMITER ;