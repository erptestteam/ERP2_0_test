var storage_data=[];
var item_NO;
$(function() {
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
	init_form();
});
var selectGrid;
function getGridOptions() {
	var options = ERPUtils.get_default_grid_option_for_url({url:erp_api_service.EntItem[0],columns: [ {
			display : '部品编号',
			name : 'number',
			width : 150
		},
		{
      	  display: '类别', name: 'type', width: 150,type:'int',
      	  editor: { type: 'select',emptyText: null, data:getItemTypeArry(), valueColumnName: 'type', displayColumnName: 'name' },
      	  render: function (rowdata, rowindex, value) {
      		  return getItemTypeMap()[value];
      	  }
        }],
        isShowDetailToggle:function(rowData){
        	//console_info(arguments);
        	if("2"==rowData.type)
        		return true;
        	return false;
        },detail: { height:'auto',onShowDetail: function (row, detailPanel,callback)
            {
            	var _data=getItemTree(row.number,true,function(tree){
            		var grid = document.createElement('div'); 
                    $(detailPanel).append(grid);
                    $(grid).css('margin',10).ligerGrid({
                        columns:
                        	[
                            // { display: '序号', name: 'id', width: 30, type: 'int' },
                             {
                           	  display: '子件', name: 'c', id:"id1", align: 'left'
                             },
                             {
                           	  display: '层次', name: 'l', width: 40,isSort: false
                           	 // editor: { type: 'text', height: 60 }
                             },
                             {
                            	 display: '数量', name: 'n', width: 50,isSort: false,
                            	 editor: { type: 'text', height: 60 }
                             }
                             ], 
                             onSelectRow: function (rowdata, rowindex) {
                            	 item_NO=rowdata.c;
             					init_item_storage(rowdata.c);
             					show_item_storage_text(rowdata.c);
             					select._toggleSelectBox(true);
             		        },
                             enabledEdit: true,
                             detailToEdit: false,
                             clickToEdit: false,
                             //height:'90%',
                             tree: { columnId: 'id1' },
                             isScroll: false,//当 父容器detail: { height:'auto', 。。设置后  此参数失效 
                             showToggleColBtn: false,
                             width: '95%',
                             data: {Rows:tree}, 
                             showTitle: false, 
                             pageSize:30,
                             //enabledSort:false,//不允许排序
                            // columnWidth: 100,
                             onAfterShowData: callback,
                             rownumbers:true,
                             frozen:false
                    });  
            	}) ;
                
            }
		}, 
		onLoaded:function(g)
		{
			selectGrid=g;
		},
		/*toolbar: { items: [
		                      { text: '高级自定义查询', 
		                    	  click: function()
		                    	  {
		                    		  selectGrid.showFilter();
		                    	  }, 
		                    	  icon: 'search2'
		                    }
		                   ]
				},*/
				checkbox:false, 
				onSelectRow: function (rowdata, rowindex) {
					item_NO=rowdata.number;
					init_item_storage(rowdata.number);
					show_item_storage_text(rowdata.number);
		        }
		                      
	});
	
	return options;
}
var select;
function init_form() {
	 $("#choose_item").ligerForm({
		inputWidth : 300,
		labelWidth : 90,
		space : 40,
		fields : [{
			name : "id",
			type : "hidden"
		}, {
			display : '部品编号',
			type : 'select',
			name : 'item_number',
			isSort : false,
			isMultiSelect: false,
			editor : {
				condition: {
                    //prefixID : 'conditio',
                    fields: [
                        { label: '部品号', name: 'number', type: 'text' }
                    ]
                },
                onButtonClick:function(){
                	select=this;
                },
				selectBoxWidth: 400 ,
    	  		selectBoxHeight:300,
				valueField : 'number',
				textField : 'number',
				grid : getGridOptions()
			}
		}]
	});
}
var storage_item_grid;
function init_item_storage(item_number)
{
	storage_item_grid=$("#show_item").ligerGrid(ERPUtils.get_default_grid_option_for_url(
			{url:erp_api_service.EntRelStorageItem[0]+"?item_number="+item_number,
				width:"95%",
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
					{ display: '出库数量', name: 'add_count', align: 'right', 
						editor: { type: 'int'},
						render: function (rowdata, rowindex, value) {
                  		  return "<input id='add_count"+rowindex+"' type='text'/>";
                  	  }
                    },
					{ display: '出库备注', name: 'add_remark', align: 'right', 
						editor: { type: 'text'},
						render: function (rowdata, rowindex, value) {
	                  		  return "<input id='add_remark"+rowindex+"' type='text'/>";
	                  	  }
                    },
                    {
                        display: '操作', isSort: false, filter:false, render: function (rowdata, rowindex, value) {
                            var h = "";
                                h += "<a href='javascript:addCount(" + rowindex + ")'>出库</a> ";
                            return h;
                        }
                    }
					],
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
	if(r.test(string_add)&&(Number(string_add))<=(Number(row.actual_count))){
		
		add=Number(string_add);
	}
	else{
		tipOnce("提示", "出库数量不准确", 5000);
		return;
	}
	var inrecord_data={"count": add,
	           "item_number": item_NO,
	           "item_type": row.type,
	           "remark": string_remark,
	           "storage_id": row.storage_id,
	           "type": "出库"
	           };
	add_info_to_iorecord(inrecord_data);
	 var param = {
             url: erp_api_service.EntRelStorageItem[0] + row.id,
             method: "PATCH",
             //data: Util.extend(arguments[0].record, arguments[0].newdata)
             data:{actual_count:old-add}
             //encode:"utf-8"
         };
      
      var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
     if (res != null && res.status > 199 && res.status<300) {
         tipOnce("提示", "出库成功", 5000);
         storage_item_grid.reload();
     }
}
function show_item_storage_text(item_number){
		 var tech_form=$("#show_item_storage").ligerForm({
	         inputWidth: 170, labelWidth: 90, space: 40,
	         fields: 
	        [
	         { display: "库存信息", name: "item_storage_info",newline: true, type: "text",editor:{readonly:true}}
	         ]
	     });
		 tech_form.setData({item_storage_info:item_number+"的库存信息"});
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