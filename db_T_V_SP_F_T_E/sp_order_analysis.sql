DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `sp_order_analysis`$$

CREATE DEFINER=`root`@`%` PROCEDURE `sp_order_analysis`(IN _mergeOrder INT,IN _useExpand INT,IN _useActualStorage INT,IN _useFutureStorage INT)
BEGIN
    DECLARE _orderID INT(11);
    DECLARE _componentID VARCHAR(255);
    DECLARE _orderRequirement INT(11);
    DECLARE _p VARCHAR(255);
    DECLARE _c VARCHAR(255);
    DECLARE _defectRequirement INT(11);
    DECLARE _actualStorage INT(11);
    DECLARE _futureStorage INT(11);
    DECLARE _usedStorage INT(11);
    DECLARE _fromStorage INT(11);
    DECLARE _fromProduct INT(11);
    DECLARE _found BOOLEAN DEFAULT TRUE;
    DECLARE p_cursor CURSOR FOR SELECT order_id,item_number,COUNT FROM `temporary_order_filter`;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET _found=FALSE;
    
    #drop TABLE if EXISTS temporary_order_filter;
    #create temporary table temporary_order_filter as select order_id,item_number,COUNT  from `v_order_filter_extract`;
    TRUNCATE temporary_order_filter;
    IF _mergeOrder = 0 THEN
        INSERT INTO temporary_order_filter SELECT order_id,item_number,COUNT FROM v_order_filter_extract;
    ELSEIF _mergeOrder =1 THEN
        INSERT INTO temporary_order_filter SELECT NULL,item_number,g_count FROM 
        (SELECT NULL,item_number,SUM(COUNT) AS g_count,MIN(order_lead_time) AS g_lead_time 
        FROM v_order_filter_extract AS p1 GROUP BY item_number) AS p2
        ORDER BY g_lead_time;
        #select null,item_number,sum(count) from v_order_filter_extract group by item_number;
    END IF;
    IF _useExpand = 0 THEN
        TRUNCATE tmp_order_analysis;
    ELSEIF _useExpand = 1 THEN
        TRUNCATE tmp_order_analysis2;
    END IF;
    OPEN p_cursor;
    FETCH p_cursor INTO _orderID,_componentID,_orderRequirement;
    WHILE _found DO
        SET _p = NULL;
        SET _c = _componentID;
        SET _defectRequirement = (SELECT f_get_component_defective_requirement(_componentID,_orderRequirement));
        SET _actualStorage = (SELECT f_get_component_actual_storage(_c,_useActualStorage));
        SET _futureStorage = (SELECT f_get_component_future_storage(_c,_useFutureStorage));
        IF _orderRequirement >= 0 THEN
            SET _usedStorage = (SELECT f_get_component_used_storage(_useExpand,_c));
            IF _orderRequirement <= (_actualStorage + _futureStorage - _usedStorage) THEN
                SET _fromStorage = _orderRequirement;
                SET _fromProduct = 0;
            ELSE
                SET _fromStorage = _actualStorage + _futureStorage - _usedStorage;
                SET _fromProduct = _orderRequirement - _actualStorage - _futureStorage + _usedStorage;
            END IF;
        END IF;
        IF _useExpand = 0 THEN
            INSERT INTO tmp_order_analysis(orderID,componentID,p,c,orderRequirement,splitRequirement,otherRequirement,defectRequirement,
            actualStorage,futureStorage,usedStorage,fromStorage,fromProduct) 
            VALUES (_orderID,_componentID,_p,_c,_orderRequirement,0,0,_defectRequirement,
            _actualStorage,_futureStorage,_usedStorage,_fromStorage,_fromProduct);
            CALL sp_order_disassemble(_useActualStorage,_useFutureStorage,_orderID,_componentID,_p,_c,
            _orderRequirement,0,0,_defectRequirement,_actualStorage,_futureStorage,_usedStorage,_fromStorage,_fromProduct);
        ELSEIF _useExpand = 1 THEN
            INSERT INTO tmp_order_analysis2(orderID,componentID,p,c,orderRequirement,splitRequirement,otherRequirement,defectRequirement,
            actualStorage,futureStorage,usedStorage,fromStorage,fromProduct) 
            VALUES (_orderID,_componentID,_p,_c,_orderRequirement,0,0,_defectRequirement,
            _actualStorage,_futureStorage,_usedStorage,_fromStorage,_fromProduct);
        END IF;
        FETCH p_cursor INTO _orderID,_componentID,_orderRequirement;
    END WHILE ;
    CLOSE p_cursor;
    IF _useExpand = 0 THEN
         CALL sp_analysis_update_halfStorage();
    ELSEIF _useExpand = 1 THEN
         CALL sp_analysis_update_halfStorage2();
    END IF;
END$$

DELIMITER ;