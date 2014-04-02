Procude of Getting Order Status
===============================
*update @ 2014-04-02 19:30*

| 订单记录表：ent_order
| 订单记录表中关于订单项状态的属性：ent_order.status
| 与订单相关的记录表：
| 部品记录表	ent_item
| 订单分析筛选记录表	tmp_order_filter
| 订单分析结果记录表	tmp_order_analysis

Definition lists: 

what 
  Definition lists associate a term with 
  a definition. 

how 
  The term is a one-line phrase, and the 
  definition is one or more paragraphs or 
  body elements, indented relative to the 
  term. Blank lines are not allowed 
  between term and definition.

订单的可以有的状态情况:

未定义:0 
  订单项状态为0或者为NULL或者为空字符串
已发货：等待买家确认——11X 
  订单项状态为“已发货”
已发货：买家确认不合格——12X 
  订单项状态为“买家确认失败”
已发货：买家确认完成——190X 
  订单项状态为“买家确认完成”
未发货：(过期，部品不存在)——1XX 
  订单项状态大于等于100，且订单项中要求的部品在部品记录表中不存在，或当前日期大于等于订单项纳期
未发货：未分析——20X 
  订单项状态大于等于200，且订单项编号不存在于订单分析筛选记录表中。
未发货：在分析——22X 
  订单项状态大于等于220，且订单项编号已存在于订单分析筛选记录表中。
未发货：空分析——24X 
  订单项状态大于等于240，且订单编号存在于订单分析筛选记录表，且不存在于订单记录表中。
未发货：已投料——3XX（或者叫“预期可发货”） 
  订单项状态大于等于300，对所有订单项状态大于等于200的记录调用order_analysis2(0,0)过程，在不展开订单项部品的状态下，筛选fromProdct为0的订单项。
