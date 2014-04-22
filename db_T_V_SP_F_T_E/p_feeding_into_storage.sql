DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `p_feeding_into_storage`$$

CREATE DEFINER=`root`@`%` PROCEDURE `p_feeding_into_storage`(IN _feeding_id INT)
BEGIN
    DECLARE _item_number VARCHAR(255);
    DECLARE _feeding_count INT;
    #declare _now datetime;
    
    SELECT item_number,feeding_count INTO _item_number,_feeding_count FROM ent_feeding WHERE id = _feeding_id;
    #set _now=now();
    #update ent_feeding_status set d_time = _now where feeding_id = _feeding_id;
    #update ent_feeding set d_time = _now where id = _feeding_id;
    #update ent_feeding set ent_feeding.`storage_mark`=1 where id = _feeding_id;
    IF _feeding_count IS NOT  NULL AND  _feeding_count>0 THEN 
	SELECT feeding_check_update_future_count_by_item(_item_number);
    END IF;
    TRUNCATE tmp_order_analysis;
END$$

DELIMITER ;