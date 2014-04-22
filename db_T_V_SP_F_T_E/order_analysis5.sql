DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `order_analysis5`$$

CREATE DEFINER=`root`@`%` PROCEDURE `order_analysis5`(IN _useExpand INT,IN _useActualStorage INT,IN _useFutureStorage INT)
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
    INSERT INTO temporary_order_filter SELECT order_id,item_number,COUNT FROM v_order_filter_extract;
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
        SET _defectRequirement = (SELECT get_component_defective_requirement2(_componentID,_orderRequirement));
        SET _actualStorage = (SELECT get_component_actual_storage2(_c,_useActualStorage));
        SET _futureStorage = (SELECT get_component_future_storage2(_c,_useFutureStorage));
        IF _orderRequirement >= 0 THEN
            SET _usedStorage = (SELECT get_component_used_storage4(_useExpand,_c));
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
            CALL order_disassemble5(_useActualStorage,_useFutureStorage,_orderID,_componentID,_p,_c,
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
END$$

DELIMITER ;