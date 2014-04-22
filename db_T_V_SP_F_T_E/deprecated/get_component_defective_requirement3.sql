DELIMITER $$

USE `erp`$$

DROP FUNCTION IF EXISTS `get_component_defective_requirement3`$$

CREATE DEFINER=`root`@`%` FUNCTION `get_component_defective_requirement3`(comp_id VARCHAR(255),origin_req INT,_useDefective INT) RETURNS INT(11)
BEGIN
    DECLARE total INT;
    IF _useDefective = 0 THEN
        SET total = CEIL(
	(SELECT AVG(defective_rate) FROM ent_item WHERE ent_item.number = comp_id GROUP BY ent_item.number) * origin_req);
	IF total IS NULL THEN 
	    RETURN 0;
	ELSE
	    RETURN total;
	END IF;
    ELSEIF _useDefective = 1 THEN 
	RETURN 0;
    END IF;
END$$

DELIMITER ;