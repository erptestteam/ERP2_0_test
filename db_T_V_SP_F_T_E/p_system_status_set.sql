DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `p_system_status_set`$$

CREATE DEFINER=`root`@`%` PROCEDURE `p_system_status_set`()
BEGIN
    DECLARE _sys_status CHAR(20) DEFAULT '000000001';
    DECLARE _id INT;
    DECLARE _number VARCHAR(255);
    DECLARE _batch_number VARCHAR(255);
    DECLARE _type VARCHAR(255);
    DECLARE _note_date DATETIME;
    DECLARE _item_number DATE;
    DECLARE _count INT;
    DECLARE _status INT;
    DECLARE _found BOOLEAN DEFAULT TRUE;
    DECLARE p_cursor CURSOR FOR SELECT id,number,batch_number,TYPE,note_date,item_number,COUNT,STATUS FROM ent_order;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET _found=FALSE;
    
    OPEN p_cursor;
    FETCH p_cursor INTO _id,_number,_batch_number,_type,_note_date,_item_number,_count,_status;
    WHILE _found DO
        UPDATE ent_order SET sys_status = _sys_status WHERE id = _id;
    END WHILE ;
    CLOSE p_cursor;
    END$$

DELIMITER ;