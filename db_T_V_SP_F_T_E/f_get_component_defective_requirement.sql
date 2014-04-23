DELIMITER $$

USE `erp`$$

DROP FUNCTION IF EXISTS `f_get_component_defective_requirement`$$

CREATE DEFINER=`root`@`%` FUNCTION `f_get_component_defective_requirement`(comp_id VARCHAR(255),origin_req INT) RETURNS INT(11)
BEGIN
     DECLARE total INT;
     IF comp_id IS NOT NULL THEN
          SET total =  CEIL((SELECT f_get_component_defective_rate(comp_id)) * origin_req);
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