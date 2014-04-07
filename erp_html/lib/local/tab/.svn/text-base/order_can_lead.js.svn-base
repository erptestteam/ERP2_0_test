var materia_data=[];
var entity_edit_model  = {
    manager: null,
    grid_div:'#order_can_lead',
    filter_div:'#order_can_lead_filter',
    key:'id',
    menu:null,
    url_index:0,
    url:erp_api_service.VOrderAnalysis2,
    top_menu:null,
    checked_record:[],
    default_pages_size:15,//默认页面大小
    pages_size:[10, 15, 30,50,100],//定义分页时 页面的大小级别
    width:'95%',
    dispaly_columns: [
          { display: '序号', name: 'order_id', width: 50, type: 'int' },
          {
              display: '订单号', name: 'order_number', width: 100,
              editor: { type: 'text', height: 60 }
          },
          {
              display: '批号', name: 'order_batch_number', width: 50,
              editor: { type: 'text' }
          },
          {
              display: '部品', name: 't',  align: 'center',width: 100,
              editor: { type: 'text', height: 60 }
          },
          {
              display: '订单量', name: 'order_requirement',   align: 'center',type:'int' ,width: 60,
              editor: { type: 'int', height: 60 }
          },
          {
              display: '纳期', name: 'order_lead_time', type: 'date', format: 'yyyy年MM月dd',  align: 'center',width: 100,
              editor: { type: 'date',format: 'yyyy-MM-dd'}
          },
          {
              display: '库存', name: 'actual_storage',  align: 'center', width: 80,
              editor: { type: 'text', height: 60 }
          },
          {
              display: '预入库存', name: 'future_storage',  align: 'center', width: 80,
              editor: { type: 'text', height: 60 }
          },
          {
              display: '可发货状态', name: 'forecast',  align: 'center', 
              editor: { type: 'text', height: 60 },
              render: function(rowdata, index, value){
            	  var h="";
            	 if(value+''=='0')
            		 h+='可直接发货';
            	 else if(value+''=='1')
            		 h+='预期可发货（在生产中）';
             	  return h;
              }
          }
     ]
    	
};
$(function () {
	var res;
	dialogWait("正在分析，稍后......",function(){
		res =bridge_map.super_api(Util.formatString(erp_api_sql.procedure_order_analysis4,1,0,0));
	},null,function(){
		
		if(res&&res.status)
		{
			//alert(res.status);
			$(f_initGrid);
		}
		else
		{
			tipOnce("提示",'分析错误，请刷新。', 10000);
		}
	});
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
        entity_edit_model .manager = $(entity_edit_model.grid_div).ligerGrid(ERPUtils.get_default_grid_option_for_url({
        	toolbar: { 
        		items: [
        		        { text: '删除',click:function()
        		        	{
        		        		if(entity_edit_model.checked_record&&entity_edit_model.checked_record.length>0)
        		        		{
        		        			if(confirm('确定删除'+entity_edit_model.checked_record.join(',')+'?'))
        		        			{
        		        			// console_info(entity_edit_model.checked_record.join(','));
        		        				var errors=[];
        		        				var rights=[];
        		        				if(entity_edit_model.checked_record&&entity_edit_model.checked_record.length>0)
        		        				{
        		        					for(var i in entity_edit_model.checked_record)
        		        					{
        		        						if(!ERPUtils.deleteEntityById(entity_edit_model.checked_record[i],erp_api_service.TmpOrderFilter[0]))
        		        							errors.push(entity_edit_model.checked_record[i]);
        		        						else
        		        							rights.push(entity_edit_model.checked_record[i]);
        		        					}
        		        					if(errors.length>0)
        		        						tipOnce("提示", Util.formatString("[{0}]删除失败", errors.join(",")), 10000);
        		        					else
        		        						tipOnce("提示", Util.formatString("[{0}]删除成功", rights.join(",")), 5000);
        		        					entity_edit_model.manager.reload();
        		        				}
        		        			}
        		        			else
        		        			{
        		        				tipOnce("提示", "取消删除。", 5000);
        		        			}
        		        		}
        		        		else
        		        		{
        		        			tipOnce("提示", "请选择后删除。", 5000);
        		        		}
        		        	}, img: '../lib/ligerUI/ligerUI/skins/icons/delete.gif' },
        		        	
        		        { line: true },
        		        { text: '高级自定义查询', click: function(){
        		        	entity_edit_model.manager.showFilter(entity_edit_model.filter_div);
        		        }, icon: 'search2'},
        		        { line: true }
        		     ]
        	},
        	onBeforeSubmitEdit:function()
            {
            	console_info(arguments[0]);
                var param;
                if (arguments[0].record.__status == "add") {
                    param = {
                        url: entity_edit_model.url[entity_edit_model.url_index],
                        method: "POST",
                        data: Util.extend(arguments[0].record, arguments[0].newdata)
                        //encode:"utf-8"
                    };
                }
                else {
                	console_info(arguments[0]);
                    param = {
                        url: erp_api_service.EntOrder[0] + arguments[0].record.id+"/",
                        method: "PATCH",
                        //data: Util.extend(arguments[0].record, arguments[0].newdata)
                        data:arguments[0].newdata
                        //encode:"utf-8"
                    };
                }
                 
                 var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
                if (res != null && res.status > 199 && res.status<300) {
                    tipOnce("提示", "修改成功", 5000);
                    entity_edit_model .manager.reload();
                    return true;
                }
                else {
                    tipOnce("提示", Util.formatString("修改失败，请重试[失败码:{0}]", res?res.status:null), 10000)
                    return false;
                }
            },
        	onCheckAllRow:function(checked)
        	{
        		 for (var rowid in this.records)
        		{
        			if(checked)
        				addChecked(this.records[rowid][entity_edit_model.key]);
        			else
        				removeChecked(this.records[rowid][entity_edit_model.key]);
        		}
        	},
        	onCheckRow: function(checked, data)
        	{
        		 if (checked) 
        			 addChecked(data[entity_edit_model.key]);
        		 else removeChecked(data[entity_edit_model.key]);
        	},
        	isChecked: function(rowdata)
        	{
        		 if (findChecked(rowdata.order_id) == -1)
        			   return false;
        		return true;
        	},
        	 enabledEdit: true,
             detailToEdit: false,
             clickToEdit: false,
        	selectRowButtonOnly:true,
        	pageSize:entity_edit_model.default_pages_size,
            pageSizeOptions:entity_edit_model.pages_size,
        	url:entity_edit_model.url[entity_edit_model.url_index],
        	urlFilter:function(){
        		var op=arguments[1].options;
        		var ps=[];
        		//console_info(op);
        		var url=op.url+"?callback=?&sys_status__regex=("+erp_api_order_sys_status.lead_overtime+")|("+erp_api_order_sys_status.info_miss+")|("+erp_api_order_sys_status.item_not_exists+")";
        		if(op.parms&&op.parms.where)
        		{
        			var filter=JSON.parse(op.parms.where);
        			if(filter&&filter!="")
        				url+="&"+change_ligerui_filter_to_python(filter);
        		}
        		console_info(url);
        		return url;
        	},
        	columns:entity_edit_model.dispaly_columns
        }));
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
           entity_edit_model .manager.reload();
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
function beginEdit(rowid) {
    entity_edit_model .manager.beginEdit(rowid);
}
function cancelEdit(rowid) {
    entity_edit_model .manager.cancelEdit(rowid);
}
function endEdit(rowid) {
    entity_edit_model .manager.endEdit(rowid);
}