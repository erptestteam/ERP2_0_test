DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `p_feeding_delete`$$

CREATE DEFINER=`root`@`%` PROCEDURE `p_feeding_delete`(IN _feeding_id INT)
BEGIN
    DECLARE _item_number VARCHAR(255);
    DECLARE _feeding_count INT;
    DECLARE _now DATETIME;
    
    SELECT item_number,feeding_count INTO _item_number,_feeding_count FROM ent_feeding WHERE id = _feeding_id AND (ent_feeding.`d_time` IS  NULL OR ent_feeding.`d_time`>NOW());   
    SET _now=NOW();
    UPDATE ent_feeding_status SET d_time = _now WHERE feeding_id = _feeding_id;
    UPDATE ent_feeding SET d_time = _now WHERE id = _feeding_id;
    IF _feeding_count IS NOT  NULL AND  _feeding_count>0 THEN 
	SELECT feeding_check_update_future_count_by_item(_item_number);
    END IF;
    TRUNCATE tmp_order_analysis;
END$$

DELIMITER ;