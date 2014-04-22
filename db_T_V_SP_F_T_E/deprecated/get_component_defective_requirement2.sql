DELIMITER $$

USE `erp`$$

DROP FUNCTION IF EXISTS `get_component_defective_requirement2`$$

CREATE DEFINER=`root`@`%` FUNCTION `get_component_defective_requirement2`(comp_id VARCHAR(255),origin_req INT) RETURNS INT(11)
BEGIN
     DECLARE total INT;
     IF comp_id IS NOT NULL THEN
          SET total =  CEIL((SELECT get_component_defective_rate2(comp_id)) * origin_req);
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