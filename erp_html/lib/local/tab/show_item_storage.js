var storage_data=[];
var storage_item_grid;
var dialogData;
$(function (){  
	    var dialog = frameElement.dialog;
	    dialogData = dialog.get('data');
	    $.ajax({
	        type: 'GET',
	        url: erp_api_service.EntStorage[0]+"?callback=?&limit=1000",
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
	        			storage_data.push({id:0,name:"(空)"})
	        			for(var i in res)
	        			{
	        				storage_data.push(res[i]);
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
	    init_item_storage(dialogData.number);
	    
})

function init_item_storage(item_number)
{
	storage_item_grid=$("#storage").ligerGrid(ERPUtils.get_default_grid_option_for_url(
			{url:erp_api_service.EntRelStorageItem[0]+"?item_number="+item_number,
				width:"95%",
				isScoll:false,
				columns: [
					{
						display : '实际库存',
						type:'int',
						name : 'actual_count'
					},
					{
						display : '预期库存',
						name : 'future_count'
					},
					{
						display : '类型',
						name : 'type',
						editor:{type:'text'}
					},
					{
						display : '仓库位置',
						name : 'storage_id',
						type:'int',
						editor:{ 	
							type: 'select',
                  	  		emptyvalue:false, 
                  	  		data:storage_data, 
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
                                            { header: '名称', name: 'name' }
                                        ]
                },
                    render:function (item)
                    {
                    			for (var i = 0; i < storage_data.length; i++)
                    			{
                    				//console_info(materia_data[i]['id']);
                    					if (storage_data[i]['id']+"" == item.storage_id+"")
                    					{
                    						return storage_data[i]['name'];
                    					}
                    			}
                    			return "";
                    }
					},
					{ display: '增加库存数量', name: 'add_count',
						editor: { type: 'int'},
						render: function (rowdata, rowindex, value) {
                  		  return "<input id='add_count"+rowindex+"' type='text'/>";
                  	  }
                    },
					{ display: '入库备注', name: 'add_remark', align: 'right', 
						editor: { type: 'text'},
						render: function (rowdata, rowindex, value) {
	                  		  return "<input id='add_remark"+rowindex+"' type='text'/>";
	                  	  }
                    },
                    {
                        display: '操作', isSort: false, filter:false, render: function (rowdata, rowindex, value) {
                            var h = "";
                            if (!rowdata._editing) {

                                h += "<a href='javascript:addCount(" + rowindex + ")'>入库</a> ";
                            }
                            else {
                                h += "<a href='javascript:endEdit(" + rowindex + ")'>提交</a> ";
                                h += "<a href='javascript:cancelEdit(" + rowindex + ")'>取消</a> ";
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
                        	 //alert(arguments[0].newdata.__index).val());
                        	 var r= /^[0-9]*[1-9][0-9]*$/ ;
                        	 var add;
                        		if(r.test(arguments[0].newdata.add_count)){
                        			add=arguments[0].newdata.add_count;
                        		}
                        		else{
                        			tipOnce("提示", "入库数量不准确", 5000);
                        			return false;
                        		}
                        		var inrecord_data={"count": add,
                        		           "item_number": item_number,
                        		           "item_type": arguments[0].newdata.type,
                        		           "remark": arguments[0].newdata.add_remark,
                        		           "storage_id": arguments[0].newdata.storage_id,
                        		           "type": "入库"
                        		           };
                        		add_info_to_iorecord(inrecord_data);
                             param = {
                                 url: erp_api_service.EntRelStorageItem[0],
                                 method: "POST",
                                 data: {"actual_count":add,
                                	 "item_number":item_number, "storage_id":arguments[0].newdata.storage_id,
                                	 "type":arguments[0].newdata.type
                                 }
                                 //encode:"utf-8"
                             };
                         }
                         else {
                             param = {
                                 url: erp_api_service.EntRelStorageItem[0] + arguments[0].record.id,
                                 method: "PATCH",
                                 //data: Util.extend(arguments[0].record, arguments[0].newdata)
                                 data:arguments[0].newdata
                                 //encode:"utf-8"
                             };
                         }
                          var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
                         if (res != null && res.status > 199 && res.status<300) {
                             tipOnce("提示", "入库成功", 5000);
                             storage_item_grid.reload();
                             return true;
                         }
                         else {
                             tipOnce("提示", Util.formatString("修改失败，请重试[失败码:{0}]", res?res.status:null), 10000)
                             return false;
                         }
                     },
					 toolbar: { items: [
					                    
					                    	{
					                        text: '增加', click: function () {
					                        	storage_item_grid.addEditRow();
					                        }, icon: 'add'
					                    	}
					                    ]
					 	},
					 	enabledEdit: true, 
					 	checkbox:false,
					 	clickToEdit: false,
					 	rownumbers:true
			})
	);
}
function addCount(rowid) {
	var row=storage_item_grid.getRow(rowid);
	var old=Number(row.actual_count);
	var string_add=$("#add_count"+row.__index).val();
	var string_remark=$("#add_remark"+row.__index).val();
	var add;
	/*验证 是否合法
	 * */
	var r= /^[0-9]*[1-9][0-9]*$/ ;
	if(r.test(string_add)){
		add=Number(string_add);
	}
	else{
		tipOnce("提示", "入库数量不准确", 5000);
		return;
	}
	var inrecord_data={"count": add,
	           "item_number": dialogData.number,
	           "item_type": row.type,
	           "remark": string_remark,
	           "storage_id": row.storage_id,
	           "type": "入库"
	           };
	add_info_to_iorecord(inrecord_data);
	 var param = {
             url: erp_api_service.EntRelStorageItem[0] + row.id,
             method: "PATCH",
             //data: Util.extend(arguments[0].record, arguments[0].newdata)
             data:{actual_count:old+add}
             //encode:"utf-8"
         };
      
      var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
     if (res != null && res.status > 199 && res.status<300) {
         tipOnce("提示", "入库成功", 5000);
         storage_item_grid.reload();
     }
}
function cancelEdit(rowid) {
	storage_item_grid.cancelEdit(rowid);
	storage_item_grid.deleteRow(rowid);
}
function endEdit(rowid) {
	storage_item_grid.endEdit(rowid);
}
function add_info_to_iorecord(data)
{
	var param = {
            url: erp_api_service.EntStorageChangesRecord[0],
            method: "POST",
            data: data
            };
	  var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
      if (res != null && res.status > 199 && res.status<300) {
          storage_item_grid.reload();
          return true;
      }
      else {
          tipOnce("提示", Util.formatString("修改失败，请重试[失败码:{0}]", res?res.status:null), 10000)
          return false;
      }
}