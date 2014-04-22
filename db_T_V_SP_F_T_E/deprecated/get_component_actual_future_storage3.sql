DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `get_component_actual_future_storage3`$$

CREATE DEFINER=`root`@`%` PROCEDURE `get_component_actual_future_storage3`(
IN comp_id VARCHAR(255), IN _useActualStorage INT,IN _useFutureStorage INT, OUT actualStorage INT,OUT futureStorage INT)
BEGIN
	IF _useActualStorage = 0 AND _useFutureStorage = 0 THEN
		SELECT SUM(actual_count),SUM(future_count) INTO actualStorage,futureStorage 
		FROM ent_rel_storage_item WHERE item_number = comp_id GROUP BY item_number;
	ELSEIF _useActualStorage = 0 AND _useFutureStorage = 1 THEN
		SELECT SUM(actual_count),0 INTO actualStorage,futureStorage 
		FROM ent_rel_storage_item WHERE item_number = comp_id GROUP BY item_number;
	ELSEIF _useActualStorage = 1 AND _useFutureStorage = 0 THEN
		SELECT 0,SUM(future_count) INTO actualStorage,futureStorage 
		FROM ent_rel_storage_item WHERE item_number = comp_id GROUP BY item_number;
	END IF;
	IF actualStorage IS NULL THEN 
		SET actualStorage = 0;
	END IF;
	IF futureStorage IS NULL THEN 
		SET futureStorage = 0;
	END IF;
END$$

DELIMITER ;