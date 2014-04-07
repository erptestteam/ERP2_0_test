var materia_data=[];
var entity_edit_model  = {
    manager: null,
    child_manager:null,
    menu:null,
    url_index:0,
    url:erp_api_service.VOrderFilterExtract,
    top_menu:null,
    checked_record:[],
    default_pages_size:15,//默认页面大小
    pages_size:[10, 15, 30,50,100],//定义分页时 页面的大小级别
    dispaly_columns: [
          { display: '序号', name: 'order_id', width: 50, type: 'int' },
          {
              display: '订单号', name: 'number', width: 100,
              editor: { type: 'text', height: 60 }
          },
          {
              display: '批号', name: 'batch_number', width: 50,
              editor: { type: 'text' }
          },
          {
              display: '类型', name: 'type',  align: 'center', width: 80,
              editor: { type: 'text', height: 60 }
          },
          {
              display: '部品', name: 'item_number',  align: 'center',
              editor: { type: 'text', height: 60 }
          },
          {
              display: '订单量', name: 'count',   align: 'center',type:'int' ,width: 60,
              editor: { type: 'int', height: 60 }
          },
          {
              display: '纳期', name: 'order_lead_time', type: 'date', format: 'yyyy年MM月dd',  align: 'center',
              editor: { type: 'date',format: 'yyyy-MM-dd'}
          }
     ]
    	
};
$(function () {
	
	  $(f_initGrid);
});

function f_initGrid() {
	//添加顶层菜单栏
	$("#top_menu").ligerMenuBar({ items: [
	                                     /* { text: '文件',
	                                    	  menu: 
	                                    	  { width: 120, items:
	                                    		  [
	                                    		   { text: '保存', click: function(){} },
	                                    		   { text: '列存为', click: function(){} },
	                                    		   { line: true },
	                                    		   { text: '关闭', click: function(){} }
	                                    		   ]
	                                    	  } 
	                                      }*/
	                                      ]
	});
	 //鼠标右键
	entity_edit_model.menu = $.ligerMenu({ top: 100, left: 100, width: 120, items:
	        [
	        /*{ text: '增加', click: function(){},icon:'add' },
	        { text: '修改', click: function(){},disable:true },
	        { line: true },
	        { text: '查看', click: function(){} },
	        { text: '关闭', click: function(){} }*/
	        ]
	        });
	  $("#contextmenu").bind("contextmenu", function (e)
	   {
		  	entity_edit_model .menu.show({ top: e.pageY, left: e.pageX });
		    return false;
		});
	  		$.ligerDefaults.Filter.operators['string'] =
	  		$.ligerDefaults.Filter.operators['text'] =["like" , "equal", "notequal", "startwith", "endwith" ];
	  		$.ligerDefaults.Filter.operators['int'] =["equal", "notequal"];
        entity_edit_model .manager = $("#order_filter_grid").ligerGrid(ERPUtils.get_default_grid_option_for_url({
        	toolbar: { 
        		items: [
        		        {
        		        	text: '增加', click: function () {
        		        		var order_import_grid= $("#order_import_grid").ligerGrid(ERPUtils.get_default_grid_option_for_url(
        		        				{
        		        					toolbar: { 
        		        						items: [ 
        		        						         { text: '高级自定义查询', click: function(){
        		        						        	 order_import_grid.showFilter("#order_import_grid_filter");
        		        						         		}, icon: 'search2'
        		        						         	},
        		        						         	 { line: true },
        		        					                    { text: '选中导入到分析列表',click:function(){
        		        					                    	if(order_import_grid.checked_record&&order_import_grid.checked_record.length>0)
        		        					                    	{
        		        					                    		if(confirm('确定导入到分析列表'+order_import_grid.checked_record.join(',')+'?'))
        		        					                    		{
        		        					                    			var errors=[];
        		        					                    			var rights=[];
        		        					                    			if(order_import_grid.checked_record&&order_import_grid.checked_record.length>0)
        		        					                    			{
        		        					                    				for(var i in order_import_grid.checked_record)
        		        					                    				{
        		        					                    					if(!ERPUtils.importOrderToFilterById(order_import_grid.checked_record[i]))
        		        					                    						errors.push(order_import_grid.checked_record[i]);
        		        					                    					else
        		        					                    						rights.push(order_import_grid.checked_record[i]);
        		        					                    				}
        		        					                    				if(errors.length>0)
        		        					                    					tipOnce("提示", Util.formatString("[{0}]导入失败", errors.join(",")), 10000);
        		        					                    				else
        		        					                    					tipOnce("提示", Util.formatString("[{0}]导入成功", rights.join(",")), 5000);
        		        					                    				order_import_grid.checked_record=[];
        		        					                    				order_import_grid.reload();
        		        					                    			}
        		        					                    		}
        		        					                    		else
        		        					                    		{
        		        					                    			tipOnce("提示", "取消导入。", 5000);
        		        					                    		}
        		        					                    	}
        		        					                    	else
        		        					                    	{
        		        					                    		tipOnce("提示", "请选择后导入。", 5000);
        		        					                    	}
        		        					                    }, img: '../lib/ligerUI/ligerUI/skins/icons/plus.gif' }
        		        						        ]
        		        					},
        		        					url:erp_api_service.VOrder[0],
        		        			        urlFilter:function(){
        		        			        	var op=arguments[1].options;
        		        			        	var ps=[];
        		        			        	//console_info(op);
        		        			        	var url=op.url+"?callback=?&sys_status__regex=.00000.";
        		        			        	if(op.parms&&op.parms.where)
        		        			        	{
        		        			        		var filter=JSON.parse(op.parms.where);
        		        			        		if(filter&&filter!="")
        		        			        			url+="&"+change_ligerui_filter_to_python(filter);
        		        			        	}
        		        			        	console_info(url);
        		        			        	return url;
        		        			        	
        		        			        },
        		        		        	columns: [
        		        		        	          { display: '序号', name: 'id', width: 50, type: 'int' },
        		        		        	          {
        		        		        	              display: '订单号', name: 'number', width: 100,
        		        		        	              editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	              display: '批号', name: 'batch_number', width: 50,
        		        		        	              editor: { type: 'text' }
        		        		        	          },
        		        		        	          {
        		        		        	              display: '类型', name: 'type',  align: 'center', width: 80,
        		        		        	              editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	              display: '部品', name: 'item_number',  align: 'center', width: 150,
        		        		        	              editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	              display: '订单量', name: 'count',   align: 'center',type:'int' ,width: 60,
        		        		        	              editor: { type: 'int', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	              display: '纳期', name: 'order_lead_time', type: 'date', format: 'yyyy年MM月dd',  align: 'center', width: 100,
        		        		        	              editor: { type: 'date',format: 'yyyy-MM-dd'}
        		        		        	          }
        		        		        	     ]
        		        				}
        		        			));
        		        		//$.ligerui.win.top = true;
	                				var order_import_div=$.ligerDialog.open({
	                					title:"选中要导入分析的订单",isResize:true,showMax:true,target: $("#order_import_div"),height: 500,width:null ,
	                					buttons:[ 
	                					          { text: '确定', onclick: function (item, dialog) { alert(item.text); } },
	                				              { text: '取消', onclick: function (item, dialog) { dialog.close(); } }
	                						]
	                					});
        		        		//entity_edit_model.manager.addEditRow();
        		        	}, icon: 'add'
        		        },
        		        { text: '删除',click:function()
        		        	{
        		        		if(entity_edit_model.checked_record&&entity_edit_model.checked_record.length>0)
        		        		{
        		        			if(confirm('确定删除'+entity_edit_model.checked_record.join(',')+'?'))
        		        			{
        		        			// console_info(entity_edit_model.checked_record.join(','));
        		        				var errors=[];
        		        				var rights=[];
        		        				dialogWait("正在删除，稍后......",
        		        							function(){
        		        								for(var i in entity_edit_model.checked_record)
        		        									{
        		        										if(!ERPUtils.deleteEntityById(entity_edit_model.checked_record[i],erp_api_service.TmpOrderFilter[0]))
        		        										{
        		        											errors.push(entity_edit_model.checked_record[i]);
        		        											//tipOnce("提示", Util.formatString("[{0}]删除失败", entity_edit_model.checked_record[i]),200);

        		        										}
        		        										else
        		        										{
        		        											rights.push(entity_edit_model.checked_record[i]);
        		        											//tipOnce("提示", Util.formatString("[{0}]删除成功", entity_edit_model.checked_record[i]),200);
        		        										}
        		        									}
        	        		        				},null,
        	        		        				function(){
        	        		        					if(errors.length>0)
        	        		        						tipOnce("提示", Util.formatString("[{0}]删除失败", errors.join(",")));
        	        		        					else
        	        		        						tipOnce("提示", Util.formatString("[{0}]删除成功", rights.join(",")), 5000);
        	        		        					entity_edit_model.manager.reload();
        	        		        					entity_edit_model.checked_record=[];
        	        		        				},null);
        		        				}
        		        				else
        		        				{
        		        					tipOnce("提示", "删除取消。", 5000);
        		        				}
        		        			}
        		        			else
        		        			{
        		        				tipOnce("提示", "请选择后删除。", 5000);
        		        			}
        		        	}, img: '../lib/ligerUI/ligerUI/skins/icons/delete.gif' },
        		        { line: true },
        		        { text: '高级自定义查询', click: function(){
        		        	entity_edit_model.manager.showFilter("#order_filter_grid_filter");
        		        }, icon: 'search2'},
        		        { line: true },
        		        {
        		        	text: '分析', click: function () {
        		        		dialogWait("正在分析，稍后......",function(){
        		        			bridge_map.super_api(Util.formatString(erp_api_sql.procedure_order_analysis4,0,0,0))
        		        		},null,function(){
        		        			tipOnce("分析成功", "点击查看分析结果查看分析信息");
        		        		});
        		        	}, icon: 'process'
        		        },
        		        {
        		        	text: '查看分析结果', click: function () {
        		        		$("#order_analysis_grid").ligerGrid(ERPUtils.get_default_grid_option_for_url(
        		        				{
        		        					url:erp_api_service.VOrderAnalysis[0],
        		        		        	columns: [
        		        		        	          { display: '订单ID', name: 'order_id', width: 50, type: 'int' },
        		        		        	          {
        		        		        	              display: '订单号', name: 'order_number', width: 70,
        		        		        	              editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	              display: '订单批号', name: 'order_batch_number', width: 50,
        		        		        	              editor: { type: 'text' }
        		        		        	          },
        		        		        	          /*{
        		        		        	              display: '类型', name: 'type',  align: 'center', width: 80,
        		        		        	              editor: { type: 'text', height: 60 }
        		        		        	          },*/
        		        		        	          {
        		        		        	              display: '顶部品', name: 't',  align: 'center',width: 100,
        		        		        	              editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	              display: '订单量', name: 'order_count',   align: 'center',type:'int' ,width: 50,
        		        		        	              editor: { type: 'int', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	        	  display: '父部品', name: 'p',  align: 'center',width: 100,
        		        		        	        	  editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	        	  display: '子部品', name: 'c',  align: 'center',width: 100,
        		        		        	        	  editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	        	  display: '数量', name: 'n',  align: 'center',width: 50,
        		        		        	        	  editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	              display: '订单需量', name: 'order_need',   align: 'center',type:'int' ,width: 50,
        		        		        	              editor: { type: 'int', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	        	  display: '库存数量', name: 'storage',  align: 'center',width: 50,
        		        		        	        	  editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	        	  display: '已投数量', name: 'future_count',  align: 'center',width: 50,
        		        		        	        	  editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	        	  display: '需要生产', name: 'from_product',  align: 'center',width: 50,
        		        		        	        	  editor: { type: 'text', height: 60 }
        		        		        	          },
        		        		        	          {
        		        		        	              display: '纳期', name: 'order_lead_time', type: 'date', format: 'yyyy年MM月dd',  align: 'center',width: 100,
        		        		        	              editor: { type: 'date',format: 'yyyy-MM-dd'}
        		        		        	          }
        		        		        	     ]
        		        				}
        		        			));
	                				var order_analysis_div=$.ligerDialog.open({ target: $("#order_analysis_div"),height: 500,width:null });
        		        	}, icon: 'attibutes'
        		        },
        		        { line: true }
        		     ]
        	},
        	onCheckAllRow:function(checked)
        	{
        		 for (var rowid in this.records)
        		{
        			if(checked)
        				addChecked(this.records[rowid]['order_id']);
        			else
        				removeChecked(this.records[rowid]['order_id']);
        		}
        	},
        	onCheckRow: function(checked, data)
        	{
        		 if (checked) 
        			 addChecked(data.order_id);
        		 else removeChecked(data.order_id);
        	},
        	isChecked: function(rowdata)
        	{
        		 if (findChecked(rowdata.order_id) == -1)
        			   return false;
        		return true;
        	},
        	url:entity_edit_model.url[entity_edit_model.url_index],
        	columns:entity_edit_model.dispaly_columns
        }));
}
function beginEdit_child(rowid) {
    entity_edit_model.child_manager.beginEdit(rowid);
}
function cancelEdit_child(rowid) {
    entity_edit_model.child_manager.cancelEdit(rowid);
}
function endEdit_child(rowid) {
    entity_edit_model.child_manager.endEdit(rowid);
}
function deleteRow_child(rowid,not_confirm) {
    if (not_confirm||confirm('确定删除?')) {
        var row = entity_edit_model .child_manager.getRow(rowid);
        if (row&&row.id)
        {
           var  param = {
               url: entity_edit_model.child_url[entity_edit_model.child_url_index] + row.id + "/",
                method: "DELETE"
           };
           var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
           entity_edit_model .child_manager.reload();
           if (res != null && res.status > 199 && res.status < 300) {
        	   if(!not_confirm)
        		   tipOnce("提示", "删除成功", 5000);
           }
           else {
        	   if(!not_confirm)
        		   tipOnce("提示", Util.formatString("修改失败，请重试[失败码:{0}]", res ? res.status : null), 10000)
           }
        }
        
    }
}
function beginEdit(rowid) {
    entity_edit_model .manager.beginEdit(rowid);
}
function cancelEdit(rowid) {
    entity_edit_model .manager.cancelEdit(rowid);
}
function endEdit(rowid) {
    entity_edit_model .manager.endEdit(rowid);
}
function findChecked(id)
{
    for(var i =0;i<entity_edit_model .checked_record.length;i++)
    {
        if(entity_edit_model .checked_record[i] == id) return i;
    }
    return -1;
}
function addChecked(id)
{
    if(findChecked(id) == -1)
    	entity_edit_model .checked_record.push(id);
}
function removeChecked(id)
{
    var i = findChecked(id);
    if(i==-1) 
    	return;
    entity_edit_model .checked_record.splice(i,1);
}
