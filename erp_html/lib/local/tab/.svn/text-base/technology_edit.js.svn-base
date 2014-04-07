var entity_edit_model  = {
    manager: null,
    menu:null,
    url_index:0,
    url:erp_api_service.EntTechnology,
    top_menu:null,
    checked_record:[],
    default_pages_size:10,//默认页面大小
    pages_size:[10, 15, 30,50,100],//定义分页时 页面的大小级别
    dispaly_columns:  [
                       { display: '主键', name: 'id', width: 50, type: 'int' },
                       {
                           display: '名称', name: 'name', width: 150,
                           editor: { type: 'text', height: 60 }
                       },
                       {
                           display: '描述', name: 'descr', width: 200,align: 'left',
                           editor: { type: 'text' }
                       },
                       {
                           display: '备注', name: 'remark',  align: 'left',
                           editor: { type: 'text', height: 60 }
                       },
                       {
                           display: '添加时间', name: 'i_time', type: 'date', format: 'yyyy年MM月dd', width: 150
                          //editor: { type: 'date' }
                       },
                       {
                           display: '操作', isSort: false, width: 120, render: function (rowdata, rowindex, value) {
                               var h = "";
                               if (!rowdata._editing) {
                                   h += "<a href='javascript:beginEdit(" + rowindex + ")'>修改</a> ";
                                   h += "<a href='javascript:deleteRow(" + rowindex + ")'>删除</a> ";
                               }
                               else {
                                   h += "<a href='javascript:endEdit(" + rowindex + ")'>提交</a> ";
                                   h += "<a href='javascript:cancelEdit(" + rowindex + ")'>取消</a> ";
                               }
                               return h;
                           }
                       }
                       ]
};
$(function () {
    $(f_initGrid);
});

$.ligerDefaults.Grid.editors['textarea'] = {
    create: function (container, editParm) {
        var input = $("<textarea />");
        container.append(input);
        container.width('auto').height('auto');
        return input;
    },
    getValue: function (input, editParm) {
        return input.val();
    },
    setValue: function (input, value, editParm) {
        input.val(value);
    },
    resize: function (input, width, height, editParm) {
        var column = editParm.column;
        input.width(column.editor.width);
        input.height(column.editor.height);
    }
};
function f_initGrid() {
	//添加顶层菜单栏
	 $("#top_menu").ligerMenuBar({ items: [
	                                      { text: '文件',
	                                    	menu: 
	                                      		{ width: 120, items:
	                                      				[
	                                      				 	{ text: '保存', click: function(){} },
	                                      				 	{ text: '列存为', click: function(){} },
	                                      				 	{ line: true },
	                                      				 	{ text: '关闭', click: function(){} }
	                                      				 	]
	                                      		} 
	                                      }
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
	  $("#technology").bind("contextmenu", function (e)
	   {
		  	entity_edit_model .menu.show({ top: e.pageY, left: e.pageX });
		    return false;
		});
    entity_edit_model .manager = $("#technology").ligerGrid({
        columns: entity_edit_model.dispaly_columns,
        onSelectRow: function (rowdata, rowindex) {
        	//选择行操作
        },
        checkbox: true,//是否使用多选框
        onCheckAllRow:function(checked)
        {
        	 for (var rowid in this.records)
            {
                if(checked)
                    addChecked(this.records[rowid]['id']);
                else
                    removeChecked(this.records[rowid]['id']);
            }
        	
        },
        onCheckRow: function(checked, data)
        {
        	 if (checked) 
        		 addChecked(data.id);
             else removeChecked(data.id);
        },
        isChecked: function(rowdata)
        {
        	 if (findChecked(rowdata.id) == -1)
        		   return false;
        	return true;
        },
        onBeforeSubmitEdit:function()
        {
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
                param = {
                    url: entity_edit_model.url[entity_edit_model.url_index] + arguments[0].record.id,
                    method: "PATCH",
                    data: arguments[0].newdata
                    //encode:"utf-8"
                };
            }
             
             var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
            if (res != null && res.status > 199 && res.status<300) {
                tipOnce("提示", "修改成功", 5000);
                return true;
            }
            else {
                tipOnce("提示", Util.formatString("修改失败，请重试[失败码:{0}]", res?res.status:null), 10000)
                return false;
            }
        },
        onAfterSubmitEdit:function()
        {
        	entity_edit_model .manager.reload();
        },

        onBeforeCancelEdit:function()
        {
        },
        isScroll: false,
        frozen: false,
        pageSize:entity_edit_model.default_pages_size,
        pageSizeOptions: entity_edit_model.pages_size,
        enabledEdit: true,
        detailToEdit: false,
        clickToEdit: false,
        url:entity_edit_model.url[entity_edit_model.url_index],
        method:"get",
        urlFilter:function(){
        	var op=arguments[1].options;
        	var ps=[];
        	console_info(op);
        	var url=op.url+"?callback=?";
        	if(op.parms&&op.parms.where)
        	{
        		var filter=JSON.parse(op.parms.where);
        		if(filter&&filter!="")
        			url+="&"+change_ligerui_filter_to_python(filter);
        	}
        	console_info(url);
        	return url;
        	
        },
        paramFilter:function(){
        	var op=arguments[1].options;
        	var ps=[];
    		var page=op.newPage;
    		var pageSize=op.pageSize;
    		var sortOrder=op.sortOrder=="asc"?"":"-";
        	if(op.sortName)
        		ps.push({name:"order_by",value:sortOrder+op.sortName});
        	ps.push({name:"offset",value:(page-1)*pageSize});
        	ps.push({name:"limit",value:pageSize});
        	return ps;
        },
        onSuccess:function()
        {
        	arguments[0].Rows=arguments[0].objects;
        	arguments[0].Total=arguments[0].meta.total_count;
        },
        onError:function(XMLHttpRequest, textStatus, errorThrown) {
           
        },
        toolbar: { items: [
                    { text: '高级自定义查询', click: function(){
                    	entity_edit_model .manager.showFilter("");
                    }, icon: 'search2'},
                    {
                        text: '增加', click: function () {
                            console_info(arguments);
                           
                            entity_edit_model .manager.addEditRow();
                        }, icon: 'add'
                    },
                    { line: true },
                    { text: '删除',click:function(){
                    	if(confirm('确定删除'+entity_edit_model .checked_record.join(',')+'?'))
                    	{
                    		console_info(entity_edit_model .checked_record.join(','));
                    		var errors=[];
                    		var rights=[];
                        	if(entity_edit_model .checked_record&&entity_edit_model .checked_record.length>0)
                        	{
                        		for(var i in entity_edit_model .checked_record)
                        		{
                        			if(!deleteById(entity_edit_model .checked_record[i],true))
                        				errors.push(entity_edit_model .checked_record[i]);
                        			else
                        				rights.push(entity_edit_model .checked_record[i]);
                        		}
                        		entity_edit_model .manager.reload();
                        		if(errors.length>0)
                        			tipOnce("提示", Util.formatString("[{0}]删除失败", errors.join(",")), 10000);
                        		else
                        			tipOnce("提示", Util.formatString("[{0}]删除成功", rights.join(",")), 5000);
                        	}
                    	}
                    }, img: '../lib/ligerUI/ligerUI/skins/icons/delete.gif' }
        ]
        },
        width: '100%'
    });
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
function deleteRow(rowid,not_confirm) {
    if (not_confirm||confirm('确定删除?')) {
        var row = entity_edit_model .manager.getRow(rowid);
        if (row&&row.id)
        {
           var  param = {
               url: entity_edit_model.url[entity_edit_model.url_index] + row.id + "/",
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
function deleteById(id,not_confirm) {
    if (not_confirm||confirm('确定删除?')) {
        if (id)
        {
           var  param = {
               url: entity_edit_model.url[entity_edit_model.url_index] + id + "/",
                method: "DELETE"
           };
           var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
           if (res != null && res.status > 199 && res.status < 300) {
        	   if(!not_confirm)
        		   tipOnce("提示", "删除成功", 5000);
        	    return true;
           }
           else {
        	   if(!not_confirm)
        		   tipOnce("提示", Util.formatString("修改失败，请重试[失败码:{0}]", res ? res.status : null), 10000)
        	   return false;
           }
        }
    }
}