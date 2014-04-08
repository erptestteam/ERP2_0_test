#记录总数：
SELECT * FROM ent_item;
#1594

#部品在ent——item中，单没有在full——rel中记录展开关系
SELECT * FROM tmp_item_full_rel GROUP BY(t);
#219
SELECT DISTINCT(t) FROM tmp_item_full_rel t;
#219

#item not in full_rel
SELECT * FROM ent_item WHERE number NOT IN (SELECT t FROM tmp_item_full_rel);
#1375

#清空表filter
TRUNCATE tmp_order_filter;

#导入所有订单到filter
INSERT INTO tmp_order_filter (id,number,batch_number,TYPE,note_date,item_number,order_lead_time,COUNT,STATUS) 
SELECT id,number,batch_number,TYPE,note_date,item_number,order_lead_time,COUNT,STATUS FROM ent_order;
#2681

#订单在filter中，订单要求的部品不在ent_item中的订单（定义为新品？）
SELECT * FROM tmp_order_filter WHERE item_number NOT IN (SELECT number FROM ent_item);
#142

#订单在filter中，订单要求的部品不在full_rel中的订单
SELECT * FROM tmp_order_filter WHERE item_number NOT IN (SELECT t FROM tmp_item_full_rel);
#1810

#analysis 结果数目
SELECT * FROM tmp_order_analysis;
#5328

#analysis 中展开仅有订单要求的部品一级的记录
SELECT * FROM tmp_order_analysis WHERE p IS NULL AND n_full_rel = 0;
#1810

#analysis 中订单要求的部品是item中已存在的
SELECT * FROM tmp_order_analysis WHERE p IS NULL AND c IN (SELECT number FROM ent_item);
#2539

#analysis 中订单要求的部品不是item中已存在的
SELECT * FROM tmp_order_analysis WHERE p IS NULL AND c NOT IN (SELECT number FROM ent_item);
#142

#analysis 中订单级部品应该展开的层数总和
SELECT SUM(n_full_rel) FROM tmp_order_analysis WHERE p IS NULL;
#2647

#另外订单即部品数量为1810，即是订单数量
#2647+1810=5328.结果展开层数应该正确。
#至于left join缺少一千多的原因，应该是因为，full_rel中，并不包含需要展开的部品本身
#而这一数量应该为上述结果的1810，即在filter中，但在full_rel中无展开关系记录；