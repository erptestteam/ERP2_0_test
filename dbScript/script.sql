TRUNCATE tmp_order_filter;
INSERT INTO tmp_order_filter (id,number,batch_number,TYPE,note_date,item_number,order_lead_time,COUNT,STATUS) 
SELECT id,number,batch_number,TYPE,note_date,item_number,order_lead_time,COUNT,STATUS FROM ent_order
#WHERE item_number IN (SELECT DISTINCT(t) FROM tmp_item_full_rel)
#LIMIT 0,100
;

CALL order_analysis3(0,0,1);
#call order_analysis2(0,1);

SELECT id,orderid,componentid,p,c,n_full_rel,nl_full_rel,l_full_rel FROM tmp_order_analysis;
DELETE FROM tmp_order_filter WHERE item_number !='1C723C-74500';
SELECT * FROM tmp_order_analysis WHERE c = '26331-080002';
SELECT * FROM ent_item WHERE number ='26331-080002';
