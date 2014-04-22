DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `order_analysis3`$$

CREATE DEFINER=`root`@`%` PROCEDURE `order_analysis3`(
IN _useActualStorage INT,IN _useFutureStorage INT,IN _useDefective INT)
BEGIN
    DECLARE _orderID INT(11);
    DECLARE _componentID VARCHAR(255);
    DECLARE _orderRequirement INT(11);
    DECLARE _defectRequirement INT(11);
    DECLARE _actualStorage INT(11);
    DECLARE _futureStorage INT(11);
    DECLARE _found BOOLEAN DEFAULT TRUE;
    DECLARE p_cursor CURSOR FOR SELECT orderID,componentid,number FROM orders_filter_extract3;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET _found=FALSE;
    
    TRUNCATE TABLE tmp_order_analysis;
    OPEN p_cursor;
    FETCH p_cursor INTO _orderID,_componentID,_orderRequirement;
    WHILE _found DO
        SET _defectRequirement = (SELECT get_component_defective_requirement3(_componentID,_orderRequirement,_useDefective));
        CALL get_component_actual_future_storage3(_componentID,_useActualStorage,_useFutureStorage,_actualStorage,_futureStorage);
        INSERT INTO tmp_order_analysis(orderID,componentID,p,c,
        orderRequirement,splitRequirement,otherRequirement,defectRequirement,
        actualStorage,futureStorage,fromStorage,fromProduct) 
        VALUES (_orderID,_componentID,NULL,_componentID,
        _orderRequirement,0,0,_defectRequirement,_actualStorage,_futureStorage,0,0);
        CALL order_disassemble3(_useActualStorage,_useFutureStorage,_useDefective,_orderID,_componentID,NULL,_componentID,
        _orderRequirement,0,0,_defectRequirement,_actualStorage,_futureStorage,0,0);
        FETCH p_cursor INTO _orderID,_componentID,_orderRequirement;
    END WHILE ;
    CLOSE p_cursor;
END$$

DELIMITER ;