DELIMITER $$

USE `erp`$$

DROP FUNCTION IF EXISTS `f_get_component_defective_rate`$$

CREATE DEFINER=`root`@`%` FUNCTION `f_get_component_defective_rate`(comp_id VARCHAR(255)) RETURNS FLOAT(4,4)
BEGIN
    DECLARE rate FLOAT;
    IF comp_id IS NOT NULL THEN
        SET rate =  (SELECT AVG(defective_rate) FROM ent_item WHERE ent_item.number=comp_id GROUP BY ent_item.number);
        IF rate IS NULL THEN
            RETURN 0;
        ELSE 
            RETURN rate;
        END IF;
    ELSE
        RETURN 0;
    END IF;
    END$$

DELIMITER ;