DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `p_feeding_status_init`$$

CREATE DEFINER=`root`@`%` PROCEDURE `p_feeding_status_init`(IN _feeding_id INT)
BEGIN
    DECLARE _tie_id INT;
    DECLARE _tie_t_id INT;
    DECLARE _tie_t_name VARCHAR(255);
    DECLARE _tie_t_rank INT;
    DECLARE _tie_t_info VARCHAR(255);
    DECLARE _now DATETIME;
    DECLARE _tmp_int INT;
    DECLARE _found BOOLEAN DEFAULT TRUE;
    DECLARE _feeding_item VARCHAR(255);
    DECLARE _feeding_count VARCHAR(255);
    DECLARE _feeding_tag INT(11);
    DECLARE p_cursor CURSOR FOR 
    SELECT id,technology_id,technology_info,technology_rank FROM ent_rel_technology_item_equipment 
    WHERE item_number = _feeding_item AND (d_time>NOW() OR d_time IS NULL)
    ORDER BY technology_rank;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET _found=FALSE;
    
    SELECT item_number,feeding_count INTO _feeding_item,_feeding_count FROM `ent_feeding` WHERE id=_feeding_id AND (d_time IS NULL OR d_time >NOW());
    SELECT COUNT(*) INTO _feeding_tag FROM `ent_feeding_status` WHERE feeding_id=_feeding_id AND (d_time IS NULL OR d_time >NOW());
    IF _feeding_tag >0 THEN
	DELETE FROM ent_feeding_status WHERE feeding_id=_feeding_id AND (d_time IS NULL OR d_time >NOW());
    END IF;
    IF _feeding_item IS NOT NULL AND _feeding_count >0  THEN
	    SET _now=NOW();
	    SET _tmp_int = (SELECT COUNT(id) FROM ent_rel_storage_item 
	    WHERE item_number = _feeding_item AND actual_count IS NULL AND future_count IS NOT NULL AND (d_time IS NULL OR d_time >NOW()));
	   # if _tmp_int = 1 then
		#update ent_rel_storage_item set future_count = future_count+_feeding_count 
		#where item_number = _feeding_item AND actual_count IS NULL AND future_count IS NOT NULL;
	    IF _tmp_int < 1 THEN
		INSERT INTO ent_rel_storage_item (item_number,future_count,`type`,i_time,u_time) 
		VALUES (_feeding_item,_feeding_count,'在生产',_now,_now);
	    END IF;
	    #update ent_feeding set storage_mark = 0 where id = _feeding_id;
	    
	    SELECT feeding_check_update_future_count_by_item(_feeding_item);
	    
	    INSERT INTO ent_feeding_status (item_number,feeding_id,step_name,step_rank,step_status,i_time,u_time) 
	    VALUES (_feeding_item,_feeding_id,'投料',0,1,_now,_now);
	    OPEN p_cursor;
	    FETCH p_cursor INTO _tie_id,_tie_t_id,_tie_t_name,_tie_t_rank;
	    WHILE _found DO
		INSERT INTO ent_feeding_status (item_number,feeding_id,step_tie_id,step_name,step_rank,step_status,i_time,u_time) 
		VALUES (_feeding_item,_feeding_id,_tie_id,_tie_t_name,_tie_t_rank,0,_now,_now);
		FETCH p_cursor INTO _tie_id,_tie_t_id,_tie_t_name,_tie_t_rank;
	    END WHILE ;
	    #INSERT INTO ent_feeding_status (item_number,feeding_id,step_name,step_rank,step_status,i_time,u_time) 
	    #VALUES (_feeding_item,_feeding_id,'入库',_tie_t_rank+2,0,_now,_now);
	    CLOSE p_cursor;
	    TRUNCATE tmp_order_analysis;
	END IF;
END$$

DELIMITER ;