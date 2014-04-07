function getMenus(callBack){
	$.ajax({
    	type : 'GET',
    	url : erp_api_service.EntMenu[0] + "?callback=?",
    	dataType : 'json',
    	cache : false,
    	async : true,
    	success : function(data) {
    		if (data && data.objects) {
    			var menu_obj_list = data.objects;
    			var menus=bridge_map.get_user_info("user_menus");
    			if(menus)
    				menu_data=changeMenusToTree(menu_obj_list,menus.split(";"));
    			else
    				menu_data=menu_data;
    			//global_model.menu_tree_data = menu_data;
    			callBack(menu_data);
    		} else {
    			tipOnce("提示", "获取菜单失败,请重试。", 10000);
    		}
    	},
    	error : function(XMLHttpRequest) {
    		tipOnce("提示", "获取菜单失败,请重试。", 10000);
    	}
    });
}
function  changeMenusToTree(menu_obj_list,ids)
{
	var res=[];
	var tree=new Object();
	var map=new Object();
	for(var i in menu_obj_list)
	{
		var node=menu_obj_list[i];
		map[node.id]=node;
	}
	for(var _i in ids)
	{
		var j=ids[_i];
		if(map[j]&&map[j].parrent_id)
		{
			var p=map[j].parrent_id;
			if(!tree[p])
			{
				tree[p]={text:map[p].menu_name,isexpand: false,children:[]};
			}
			tree[p].children.push({url:map[j].menu_url,text:map[j].menu_name});
		}
	}
	for(var n in tree)
	{
		res.push(tree[n]);
	}
	return res;
}
var menu_data =
[
    {
        text: '物料管理', isexpand: false, children: [
         // { url: "../tab/item_add.html", text: "部品添加" },
          { url: "../tab/item_edit.html", text: "部品编辑" },
          { url: "../tab/material_edit.html", text: "材料管理" },
          { url: "../tab/technology_edit.html", text: "工序管理" },
          { url: "../tab/item_tree_show.html", text: "bom修改" }
        ]
    },
    {
        text: '机种管理', isexpand: false, children: [
          { url: "../tab/machine_edit.html", text: "机种编辑" }
        ]
    },
	  { 
    	text: '库存管理', isexpand: false, children: [ 
	   { url: "../tab/storage_location.html",text: "仓库位置" }, 
	   { url: "../tab/storage_io.html", text: "出库入库" }, 
	   { url:"../tab/storage_query.html", text: "库存查询" }
	  ] 
    },
    {
        text: '订单处理', isexpand: false, children: [
          { url: "../tab/order_edit.html", text: "订单添加/修改/删除" }
          ,{ url: "../tab/order_analysis.html", text: "订单分析" }
          ,{ url: "../tab/order_has_question.html", text: "错误订单" }
          ,{ url: "../tab/order_can_lead.html", text: "可发货订单" }
         // ,{ url: "../tab/item.html", text: "结果查询" }
        ]
    },
   /*
	 * { text: '生产跟踪', isexpand: false, children: [ { url: "../tab/item.html",
	 * text: "自定义查询" }, { url: "../tab/item.html", text: "在窗口显示" }, { url:
	 * "../tab/item.html", text: "配合表格" } ] }
	 */
    {
        text: '投料跟踪', isexpand: false, children: [
          { url: "../tab/test.html", text: "投料test" },
          { url: "../tab/feeding.html", text: "投料单管理" },
          { url: "../tab/feeding_on_analysis.html", text: "投料(依据分析结果)"},
          { url: "../tab/feeding_tracking.html", text: "投料单状态查询" },
          { url: "../tab/feeding_status_update.html", text: "投料单状态修改" },
          { url: "../tab/feeding_warehouse.html", text: "投料单入库" },
        ]
    },
];