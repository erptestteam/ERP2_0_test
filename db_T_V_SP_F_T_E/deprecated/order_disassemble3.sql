DELIMITER $$

USE `erp`$$

DROP PROCEDURE IF EXISTS `order_disassemble3`$$

CREATE DEFINER=`root`@`%` PROCEDURE `order_disassemble3`(IN _useActualStorage INT,IN _useFutureStorage INT,IN _useDefective INT,
IN _orderID INT(11), IN _componentID VARCHAR(255),IN _p VARCHAR(255),IN _c VARCHAR(255),
IN _orderRequirement INT(11),IN _splitRequirement INT(11),IN _otherRequirement INT(11),IN _defectRequirement INT(11),
IN _actualStorage INT(11),IN _futureStorage INT(11),IN _fromStorage INT(11), IN _fromProduct INT(11))
BEGIN
    DECLARE allRequirement INT;
    DECLARE _usedStorage INT;
    DECLARE parrentLevel INT;
    DECLARE shortValue INT;
    DECLARE _sub_p VARCHAR(255);
    DECLARE _sub_c VARCHAR(255);
    DECLARE _sub_n INT;
    DECLARE _sub_ns INT;
    DECLARE _sub_l INT;
    DECLARE _sub_c_split_req INT;
    DECLARE _sub_c_usedStorage INT;
    DECLARE _sub_c_actual_storage INT;
    DECLARE _sub_c_future_storage INT;
    DECLARE _sub_c_from_storage INT;
    DECLARE _sub_c_from_product INT;
    DECLARE _found BOOLEAN DEFAULT TRUE;
    DECLARE p_cursor CURSOR FOR SELECT p,c,n,n1,l FROM tmp_item_full_rel WHERE t = _componentID;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET _found = FALSE;
    
    SET allRequirement = _orderRequirement + _splitRequirement + _otherRequirement + _defectRequirement;
    SET parrentLevel = 0;
    SET shortValue = allRequirement;
    IF shortValue > 0 THEN
        SET _usedStorage = (SELECT get_component_used_storage3(_c));
        IF shortValue <= (_actualStorage + _futureStorage - _usedStorage) THEN
            UPDATE tmp_order_analysis SET usedStorage = _usedStorage,
            fromStorage = shortValue, 
            fromProduct = 0 WHERE orderID = _orderID;
            SET shortValue = 0;
        ELSE
            SET shortValue = shortValue - (_actualStorage + _futureStorage - _usedStorage);
            UPDATE tmp_order_analysis SET usedStorage = _usedStorage, 
            fromStorage = (_actualStorage + _futureStorage - _usedStorage),
            fromProduct = shortValue WHERE orderID = _orderID;
        END IF;
    END IF;
    UPDATE tmp_order_analysis SET n_full_rel = (SELECT COUNT(id) FROM tmp_item_full_rel WHERE t = _componentID) 
    WHERE orderID = _orderID;
    IF _found THEN
        OPEN p_cursor;
        FETCH p_cursor INTO _sub_p,_sub_c,_sub_n,_sub_ns,_sub_l;
        WHILE _found DO
            SET _sub_c_split_req = _sub_ns * shortValue;
            SET _sub_c_usedStorage = (SELECT get_component_used_storage3(_sub_c));
            CALL get_component_actual_future_storage3
                (_sub_c,_useActualStorage,_useFutureStorage,_sub_c_actual_storage,_sub_c_future_storage);
            IF _sub_c_split_req <= (_sub_c_actual_storage + _sub_c_future_storage - _sub_c_usedStorage) THEN
                SET _sub_c_from_storage = _sub_c_split_req;
                SET _sub_c_from_product = 0;
            ELSE
                SET _sub_c_from_storage = _sub_c_actual_storage + _sub_c_future_storage - _sub_c_usedStorage;
                SET _sub_c_from_product = _sub_c_split_req - _sub_c_from_storage;
            END IF;
            INSERT INTO tmp_order_analysis (orderID,componentID,p,c,
            orderRequirement,splitRequirement,otherRequirement,defectRequirement,
            actualStorage,futureStorage,usedStorage,fromStorage,fromProduct,
            n_full_rel,nl_full_rel,l_full_rel)
            VALUES (_orderID,_componentID,_sub_p,_sub_c,
            0,_sub_c_split_req,0,(SELECT get_component_defective_requirement3(_sub_c,_sub_c_split_req,_useDefective)),
            _sub_c_actual_storage,_sub_c_future_storage,_sub_c_usedStorage,_sub_c_from_storage,_sub_c_from_product,
            _sub_n,_sub_ns,_sub_l);
            FETCH p_cursor INTO _sub_p,_sub_c,_sub_n,_sub_ns,_sub_l;
        END WHILE;
        CLOSE p_cursor;
    END IF;
END$$

DELIMITER ;