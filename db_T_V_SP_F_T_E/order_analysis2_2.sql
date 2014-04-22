DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `order_analysis2_2`$$

CREATE DEFINER=`root`@`%` PROCEDURE `order_analysis2_2`(IN _useActualStorage INT,IN _useFutureStorage INT)
BEGIN
    DECLARE _orderID INT(11);
    DECLARE _componentID VARCHAR(255);
    DECLARE _orderRequirement INT(11);
    DECLARE _p VARCHAR(255);
    DECLARE _c VARCHAR(255);
    DECLARE _defectRequirement INT(11);
    DECLARE _actualStorage INT(11);
    DECLARE _futureStorage INT(11);
    DECLARE _found BOOLEAN DEFAULT TRUE;
    #DECLARE p_cursor CURSOR FOR SELECT orderID,componentid,number FROM orders_filter_extract2;
    DECLARE p_cursor CURSOR FOR SELECT order_id,item_number,COUNT FROM v_order_filter_extract;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET _found=FALSE;
    
    TRUNCATE TABLE tmp_order_analysis;
    #SET max_sp_recursion_depth=20;
    OPEN p_cursor;
    FETCH p_cursor INTO _orderID,_componentID,_orderRequirement;
    WHILE _found DO
        SET _p = NULL;
        SET _c = _componentID;
        SET _defectRequirement = (SELECT get_component_defective_requirement2(_componentID,_orderRequirement));
        SET _actualStorage = (SELECT get_component_actual_storage2(_c,_useActualStorage));
        SET _futureStorage = (SELECT get_component_future_storage2(_c,_useFutureStorage));
        INSERT INTO tmp_order_analysis(orderID,componentID,p,c,orderRequirement,splitRequirement,otherRequirement,defectRequirement,
        actualStorage,futureStorage,fromStorage,fromProduct) 
        VALUES (_orderID,_componentID,_p,_c,_orderRequirement,0,0,_defectRequirement,
        _actualStorage,_futureStorage,0,0);
        CALL top_component_disassemble2_2(_useActualStorage,_useFutureStorage,_orderID,_componentID,_p,_c,
        _orderRequirement,0,0,_defectRequirement,_actualStorage,_futureStorage,0,0);
        FETCH p_cursor INTO _orderID,_componentID,_orderRequirement;
    END WHILE ;
    CLOSE p_cursor;
END$$

DELIMITER ;