var materia_data=[];
var entity_edit_model  = {
    manager: null,
    child_manager:null,
    child_url:erp_api_service.TmpItemFullRel,
    child_url:0,
    menu:null,
    url_index:0,
    url:erp_api_service.EntItem,
    top_menu:null,
    checked_record:[],
    default_pages_size:15,//默认页面大小
    pages_size:[10, 15, 30,50,100],//定义分页时 页面的大小级别
    dispaly_columns: [
                                              { display: '主键', name: 'id',filter:false, width: 50, type: 'int' },
                                              {
                                            	  display: '编号', name: 'number', width: 150,
                                            	  editor: { type: 'string'},
                                            	  render: function (rowdata, rowindex, value) {
                                            		  //row,
                                            		  // console_info(arguments);
                                            		  return "<a href=\"javascript:show_item_detail('" +value + "')\">"+value+"</a>";
                                            		  //return "";
                                            	  }
                                              },
                                              {
                                            	  display: '类别', name: 'type', width: 150,type:'int',
                                            	  editor: { type: 'select',emptyText: null, data:getItemTypeArry(), valueColumnName: 'type', displayColumnName: 'name' },
                                            	  render: function (rowdata, rowindex, value) {
                                            		  return getItemTypeMap()[value];
                                            	  }
                                              },
                                              {
                                                  display: '材料', name: 'material', width: 150, type: 'int',
                                                  editor:{ 	type: 'select',
                                                	  		emptyvalue:false, 
                                                	  		data:materia_data, 
                                                	  		valueColumnName: 'id', 
                                                	  		displayColumnName: 'name',
                                                	  		selectBoxWidth: 300 ,
                                                	  		selectBoxHeight:300,
                                                	  		//isShowCheckBox:false,
                                                	  		emptyText: null,
                                                	  		//emptyValue:0,
                                                	  		valueType:"int",
                                                	  		columns: [
                                                                          //{ header: 'ID', name: 'id',type:'int', width: 20 },
                                                                          { header: '名称', name: 'name' },
                                                                          { header: '类型', name: 'material_type',width: 30 }
                                                                      ]
                                              },
                                                  render:function (item)
                                                  {
                                                	// console_info(item);
                                                	 // console_info(entity_edit_model.materia_data);
                                                	  //console_info(materia_data);
                                                  			for (var i = 0; i < materia_data.length; i++)
                                                  			{
                                                  				//console_info(materia_data[i]['id']);
                                                  					if (materia_data[i]['id']+"" == item.material+"")
                                                  					{
                                                  						return materia_data[i]['name'];
                                                  					}
                                                  			}
                                                  			return "";
                                                  }
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
                                                  display: '操作', isSort: false, filter:false,width: 120, render: function (rowdata, rowindex, value) {
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
	/*var url=erp_api_service.EntMaterial+"?callback=?"+"&d_time__isnull=true||d_time__gt="+new Date().pattern("yyyy-MM-dd hh:mm:ss");
	$.ajax({
        type: 'GET',
        url: url,
        dataType: 'jsonp',
        cache: false,
        async: true,
        success: function(data) {
        	var materiadata=JSON.parse(data.result).objects;
        	entity_edit_model.materia_data=materiadata;
        },
        error: function(XMLHttpRequest) {
            alert(XMLHttpRequest.status);
        }
    });*/
	$.ajax({
        type: 'GET',
        url: erp_api_service.EntMaterial[0]+"?callback=?&limit=1000",
        dataType: 'json',
        cache: false,
        async: true,
        success: function(data) {
        	if(data&&data.objects)
        	{
        		var res=data.objects;
        		console_info(res);
        		if(res instanceof Array&&res.length>0)
        		{
        			materia_data.push({id:0,name:"(空)",material_type:""})
        			for(var i in res)
        			{
        				materia_data.push(res[i]);
        			}
        		}
        		else
        		{
        			tipOnce("提示", "获取材料信息失败,请刷新。", 10000);
        		}	
        		 
        	}
       	  	else
       	  	{
       		  tipOnce("提示", "获取材料信息失败,请刷新。", 10000);
       	  	}
        },
        error: function(XMLHttpRequest) {
        	 tipOnce("提示", "获取材料信息失败,请刷新。", 10000);
           // alert(XMLHttpRequest.status);
        }
    });
	  /* var res = JSON.parse(bridge_map.ajax(JSON.stringify({url:erp_api_service.EntMaterial[0]})));
	  if(res&&res.result)
	  {
		  var res=JSON.parse(res.result).objects;
		  for(var i in res)
		  {
			  materia_data.push(res[i]);
		  }
	  }
	  else
	  {
		  tipOnce("提示", "获取材料信息失败,请刷新。", 10000);
	  }*/
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
	  $("#item").bind("contextmenu", function (e)
	   {
		  	entity_edit_model .menu.show({ top: e.pageY, left: e.pageX });
		    return false;
		});
	  		$.ligerDefaults.Filter.operators['string'] =
	  		$.ligerDefaults.Filter.operators['text'] =["like" , "equal", "notequal", "startwith", "endwith" ];
	  		$.ligerDefaults.Filter.operators['int'] =["equal", "notequal"];
        entity_edit_model .manager = $("#item").ligerGrid({
        columns: entity_edit_model.dispaly_columns,
        onSelectRow: function (rowdata, rowindex) {
        	//选择行操作
        },
        onDblClickRow : function (data, rowindex, rowobj)
        {
        	show_item_detail(data.number);  //双击行操作
        },
        isShowDetailToggle:function(rowData){
        	//console_info(arguments);
        	if("2"==rowData.type)
        		return true;
        	return false;
        },
        detail: { height:'auto',onShowDetail: function (row, detailPanel,callback)
        {
        	var _data=getItemTree(row.number,true,function(tree){
        		var grid = document.createElement('div'); 
                $(detailPanel).append(grid);
                entity_edit_model.child_manager= $(grid).css('margin',10).ligerGrid({
                    columns:
                    	[
                        // { display: '序号', name: 'id', width: 30, type: 'int' },
                         {
                       	  display: '子件', name: 'c', id:"id1", align: 'left',
                       	  editor:{ 	type: 'select',
                 	  		emptyvalue:false, 
                 	  		//data:materia_data, 
                 	  		valueColumnName: 'number', 
                 	  		displayColumnName: 'number',
                 	  		selectBoxWidth: 500 ,
                 	  		selectBoxHeight:300,
                 	  		//isShowCheckBox:false,
                 	  		emptyText: null,
                 	  		//emptyValue:0,
                 	  		valueType:"int",
                 	  		grid:get_item_grid_option(entity_edit_model)
                       	 	}
                         },
                         {
                       	  display: '层次', name: 'l', width: 100,isSort: false
                       	 // editor: { type: 'text', height: 60 }
                         },
                         {
                        	 display: '数量', name: 'n', width: 100,isSort: false,
                        	 editor: { type: 'text', height: 60 }
                         },
                         {
                             display: '操作', isSort: false, width: 120, filter:false,render: function (rowdata, rowindex, value) {
                                 var h = "";
                                 if (!rowdata._editing) {
                                     h += "<a href='javascript:beginEdit_child(" + rowindex + ")'>修改</a> ";
                                     h += "<a href='javascript:deleteRow_child(" + rowindex + ")'>删除</a> ";
                                 }
                                 else {
                                     h += "<a href='javascript:endEdit_child(" + rowindex + ")'>提交</a> ";
                                     h += "<a href='javascript:cancelEdit_child(" + rowindex + ")'>取消</a> ";
                                 }
                                 return h;
                             }
                         }
                         ], 
                         onBeforeSubmitEdit:function()
                         {
                         	//console_info(arguments[0]);
                             var param;
                             if (arguments[0].record.__status == "add") {
                                 param = {
                                     url: entity_edit_model.child_url[entity_edit_model.child_url_index],
                                     method: "POST",
                                     data: Util.extend(arguments[0].record, arguments[0].newdata)
                                     //encode:"utf-8"
                                 };
                             }
                             else {
                             	console_info(arguments[0]);
                                 param = {
                                     url: entity_edit_model.child_url[entity_edit_model.child_url_index] + arguments[0].record.id,
                                     method: "PATCH",
                                     //data: Util.extend(arguments[0].record, arguments[0].newdata)
                                     data:arguments[0].newdata
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
                         enabledEdit: true,
                         detailToEdit: false,
                         clickToEdit: false,
                         //height:'90%',
                         tree: { columnId: 'id1' },
                         isScroll: false,//当 父容器detail: { height:'auto', 。。设置后  此参数失效 
                         showToggleColBtn: false,
                         width: '90%',
                         data: {Rows:tree}, 
                         showTitle: false, 
                         //enabledSort:false,//不允许排序
                        // columnWidth: 100,
                         onAfterShowData: callback,
                         rownumbers:true,
                         frozen:false
                });  
        	}) ;
            
        } },
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
                    url: entity_edit_model.url[entity_edit_model.url_index] + arguments[0].record.id,
                    method: "PATCH",
                    //data: Util.extend(arguments[0].record, arguments[0].newdata)
                    data:arguments[0].newdata
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
        allowHideColumn:true,
        //rownumbers:true,
        colDraggable:true,
        rowDraggable:true,
        //rownumbers:true,
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
        	//console_info(op);
        	var url=op.url+"?callback=?";
        	if(op.parms&&op.parms.where)
        	{
        		var filter=JSON.parse(op.parms.where);
        		if(filter&&filter!="")
        			url+="&"+change_ligerui_filter_to_python(filter);
        	}
        	//console_info(url);
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
        toolbar: { items: [
                    { text: '高级自定义查询', click: function(){
                    	entity_edit_model .manager.showFilter("");
                    }, icon: 'search2'},
                    {
                        text: '增加', click: function () {
                           // console_info(arguments);
                           
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
function beginEdit_child(rowid) {
	console_info(rowid);
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

function getGridOptions(checkbox)
{
    var options = {
        columns: [
        { display: '顾客', name: 'CustomerID', align: 'left', width: 100, minWidth: 60 },
        { display: '公司名', name: 'CompanyName', minWidth: 120, width: 100 },
        { display: '联系名', name: 'ContactName', minWidth: 140, width: 100 },
        { display: '电话', name: 'Phone', width: 100 },
        { display: '城市', name: 'City', width: 100 },
        { display: '国家', name: 'Country', width: 100 }
        ], switchPageSizeApplyComboBox: false,
        data: $.extend({}, CustomersData),
        pageSize: 30, 
        checkbox: checkbox
    };
    return options;
}