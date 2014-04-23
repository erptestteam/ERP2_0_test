DELIMITER $$

USE `erp`$$

DROP FUNCTION IF EXISTS `f_order_sys_status_get`$$

CREATE DEFINER=`root`@`%` FUNCTION `f_order_sys_status_get`(_id INT ,_number VARCHAR(255),_batch_number VARCHAR(255),_type VARCHAR(255),
_node_date DATETIME,_item_number VARCHAR(255), _order_lead_time DATE, _count INT, _status INT,d_time DATETIME) RETURNS CHAR(20) CHARSET utf8
BEGIN
    DECLARE _get1 INT;
    DECLARE _get2 INT;
    DECLARE _get3 INT;
    DECLARE _get4 INT;
    DECLARE _get5 INT;
    DECLARE _get6 INT;
    DECLARE _get7 INT;
    #DECLARE _get8 INT;
    #DECLARE _get9 INT;
    DECLARE _new_sys_status CHAR(20);
    DECLARE _tmp_int INT;
    DECLARE _tmp_now DATETIME;
    
    SET _new_sys_status = NULL;
    SET _tmp_now=NOW();
    SET _get1='0';SET _get2='0';SET _get3='0';SET _get4='0';SET _get5='0';SET _get6='0';SET _get7='0';#SET _get8='0';SET _get9='0';
        #订单状态值错误
            IF (_status = 0) OR (_status IS NULL) THEN 
                SET _get1='1';
            END IF;
        #订单信息不合法(错误、缺失)
	    IF (_count IS NULL) OR (_count<=0)OR (_number IS NULL)  OR(_order_lead_time IS NULL)OR (_batch_number IS NULL) OR (_item_number IS NULL) THEN 
	        SET _get2='1';
	    END IF;
	#部品不存在
	    SET _tmp_int=(SELECT COUNT(id) FROM ent_item WHERE number=_item_number);
	    IF _tmp_int=0 THEN 
	        SET _get3='1';
	    END IF;
	#纳期已超时订单
	    IF (_order_lead_time<=_tmp_now) THEN
		SET _get4='1';
	    END IF;
	#已分析
	    SET _tmp_int=(SELECT COUNT(tmp_order_filter.`order_id`) FROM tmp_order_filter WHERE tmp_order_filter.`order_id`=_id);
	    IF _tmp_int>0 THEN	        
	        SET _get5='1';
	    END IF;
	#已删除订单
	    IF (d_time IS NOT NULL) AND (d_time<_tmp_now)THEN
	        SET _get6='1';
	    END IF;
	#IF _check7='0' AND _tmp_int=1 THEN
	    SET _get7='1';
	#END IF;
	SET _new_sys_status = CONCAT(_get7,_get6,_get5,_get4,_get3,_get2,_get1);
	RETURN _new_sys_status;
END$$

DELIMITER ;