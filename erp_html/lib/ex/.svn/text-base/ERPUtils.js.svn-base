ERPUtils = "undefined" == typeof (ERPUtils) ? {} : ERPUtils;
function showItemDetail(item_number)//显示Item的详细信息
{
	console_info(item_number);
	getItemTree(item_number,function(tree){
		console_info(tree);
	});
}
/*
	获取合成件的树形结构
	注意：使用此方法的时候注意传入的item要是合成件（拥有子件）
 * 
 * */
function getItemTree(item_number,async,callBack,error)
{
	console_info(item_number);
	var _tree;
	$.ajax({
        type: 'GET',
        url: erp_api_service.TmpItemFullRel[0]+"?callback=?",
        dataType: 'json',
        cache: false,
        data:[{name:"t",value:item_number}],
        async: async?true:false,
        success: function(data) {
        	if(data&&data.objects)
        	{
        		var tmp=data.objects;
        		//console_info(tmp);
        		 if(typeof callBack=="function"&&tmp instanceof Array&&tmp.length>0)
        		{
        			 _tree=change_tmp_item_full_rel_to_tree(tmp);
        			 callBack(_tree);
        		}
        	}
       	  	else
       	  	{
       	  		callBack(null);
       	  	}
        },
        error: function(XMLHttpRequest) {
        	error(arguments);
        	//return null;
           // alert(XMLHttpRequest.status);
        }
    });
	return _tree;
}
function change_tmp_item_full_rel_to_tree(tmp)//将item的树形结构展示清楚
{
	//console_info(tmp);
	if(tmp instanceof Array&&tmp.length>0)
		return _get_tmp_item_chidren(tmp,tmp[0]['t']);
	return null;
}
function _get_tmp_item_chidren(tmp,item)
{
	var tree=[];
	for(var i in tmp)
	{
		if(tmp[i]['p']==item)
		{
			tree.push(tmp[i]);
		}
	}
	for(var j in tree)
	{
		var children=_get_tmp_item_chidren(tmp,tree[j]['c']);
		if(children.length>0)
		{
			tree[j]["children"]=children;
		}
	}
	return tree;
}
function getItemTypeMap()
{
	var types=getItemTypeArry();
	var map=new Object();
	for(var i in types)
	{
		map[types[i]["type"]]=types[i]["name"];
	}
	return  map;
}
function getItemTypeArry()
{
	return  [{type:1,name:"附件"},{type:2,name:"成品件"}];
}
var dialogs=new Object();
function show_item_detail(number)
{
	$.ligerui.win.top = true;
	if(!dialogs[number])
	{
		dialogs[number]=$.ligerDialog.open({ url:'../tab/show_item_detail.html', width: 800, showMax: true, showToggle: true, showMin: true, isResize: true, modal: false,height: 440 ,
			data: {
				number: number
			},title:number
		});
	}
	else
	{
		console_info(dialogs[number]);
		//$.ligerDialog.open(dialogs[number])
		dialogs[number].active();
	}
	
	 

}

function get_item_grid_option()
{
	var grid;
	return {
		columns: [
                    { display: '主键', name: 'id',filter:false, width: 50, type: 'int' },
                    {
                    	display: '编号', name: 'number', width: 150,
                    	//editor: { type: 'string'},
                    	render: function (rowdata, rowindex, value) {
                                            		  //row,
                                            		  // console_info(arguments);
                    		return "<a href=\"javascript:showItemDetail('" +value + "')\">"+value+"</a>";
                                            		  //return "";
                    	}	
                    },
                    {
                         display: '类别', name: 'type', width: 150,type:'int',
                        // editor: { type: 'select',emptyText: null, data:getItemTypeArry(), valueColumnName: 'type', displayColumnName: 'name' },
                         render: function (rowdata, rowindex, value) {
                                   return getItemTypeMap()[value];
                         }
                    },
                    {
                          display: '材料', name: 'material', width: 150, type: 'int',
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
                           display: '备注', name: 'remark',  align: 'left'
                          // editor: { type: 'text', height: 60 }
                     },
                     {
                             display: '添加时间', name: 'i_time', type: 'date', format: 'yyyy年MM月dd', width: 150
                                                 //editor: { type: 'date' }
                      },
        ],
		allowHideColumn:true,
        //rownumbers:true,
        colDraggable:true,
        rowDraggable:true,
        //rownumbers:true,
        isScroll: false,
        frozen: false,
        pageSize:30,
        pageSizeOptions:[10,20,30,50],
        enabledEdit: true,
        detailToEdit: false,
        clickToEdit: false,
        url:erp_api_service.EntItem[0],
        method:"get",
        urlFilter:function(){
        	var op=arguments[1].options;
        	var ps=[];
        	//console_info(op);
        	var url;
        	if(op.url.match(/callback/))
        		url=op.url;
        	else
        		url=op.url+"?callback=?";
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
        	grid=this;
        	var op=arguments[1].options;
        	var ps=[];
    		var page=op.newPage;
    		var pageSize=op.pageSize;
    		var sortOrder=op.sortOrder=="asc"?"":"-";
        	if(op.sortName)
        		ps.push({name:"order_by",value:sortOrder+op.sortName});
        	ps.push({name:"offset",value:(page-1)*pageSize});
        	ps.push({name:"limit",value:pageSize});
        	ps.push({name:"type",value:2});
        	return ps;
        },
        onSuccess:function()
        {
        	arguments[0].Rows=arguments[0].objects;
        	arguments[0].Total=arguments[0].meta.total_count;
        },
        toolbar: { 
        	items: [
                           { text: '高级自定义查询', click: function(){
                        	   grid.showFilter("");
                           }, icon: 'search2'}
               ]
               },
        width: '100%'
	};
}
/**
 * [
 * 	{	
 * 		name:xx,
 * 		width:xx,
 * 		type:
 * 	}
 * ]
 * */
function get_default_grid_option_for_array(arr,map)
{
	if(!(arr instanceof Array)||arr.length==0)
		return null;
	function get_columns(arr)
	{
		
		//if(!arr[0] instanceof Array||arr.length=0)
		var colums=[];
		for(var i in arr[0])
		{
			var w=100/arr.length;
			colums.push(Util.extend({ display: i+"", name: 'id'+i,filter:false,  type: 'text' },map?(map[i]?map[i]:{}):{}));
		}
		return colums;
	}
	function get_data(arr)
	{
		var data={
				Rows:[],
	        	Total:arr.length
		};
		for(var i in arr)
		{
			var _d=new Object();
			for(var j in arr[i])
			{
				_d["id"+j]=arr[i][j];
			}
			data.Rows.push(_d);
		}
		return data;
	}
	return {
		columns:get_columns(arr),
		data:get_data(arr),
		allowHideColumn:true,
        //rownumbers:true,
        colDraggable:true,
        rowDraggable:true,
        //rownumbers:true,
        isScroll: false,
        frozen: false,
        pageSize:15,
        isResize:true,
        pageSizeOptions:[10,20,30,50],
        enabledEdit: false,
        detailToEdit: false,
        clickToEdit: false,
        width: '100%'
	};
}
 ERPUtils.get_default_grid_option_for_url=function(param)
{
	 var checked_record=[];
	if(!param.url||!param.columns)
	{
		throw new error("url or columns are not allow null");
		return null;
	}
	function findChecked(id)
	{
	    for(var i =0;i<checked_record.length;i++)
	    {
	        if(checked_record[i] == id) return i;
	    }
	    return -1;
	}
	function addChecked(id)
	{
	    if(findChecked(id) == -1)
	    	checked_record.push(id);
	}
	function removeChecked(id)
	{
	    var i = findChecked(id);
	    if(i==-1) 
	    	return;
	    checked_record.splice(i,1);
	}
	return Util.extend({
        //columns: entity_edit_model.dispaly_columns,
        checkbox: true,//是否使用多选框
        allowHideColumn:true,
        //rownumbers:true,
        colDraggable:true,
        rowDraggable:true,
        //rownumbers:true,
        isScroll: false,
        frozen: false,
        pageSize:15,
        pageSizeOptions: [10,15,20,30,50],
        width: '100%',
        ///url:entity_edit_model.url[entity_edit_model.url_index],
        method:"get",
        urlFilter:function(){
        	var op=arguments[1].options;
        	var ps=[];
        	var url;
        	if(op.url.match(/\?/))
        		url=op.url+"&callback=?";
        	else
        		url=op.url+"?callback=?";
        	if(op.parms&&op.parms.where)
        	{
        		var filter=JSON.parse(op.parms.where);
        		if(filter&&filter!="")
        			url+="&"+change_ligerui_filter_to_python(filter);
        	}
        	if(op.parms&&op.parms.condition)
        	{
        		var condition=JSON.parse(op.parms.condition);
        		url+="&"+change_ligerui_rule_to_python(condition[0]);
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
        	this.checked_record=checked_record;
        	arguments[0].Rows=arguments[0].objects;
        	arguments[0].Total=arguments[0].meta.total_count;
        },
        onError:function(XMLHttpRequest, textStatus, errorThrown)
        {
        	
        	tipOnce("错误","数据获取错误,请重试。",10000);
        },
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
        }
    },param);
}
function get_material_data()
{
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
}
ERPUtils.deleteEntityById=function(id,url) {
	if (id) {
		var param = {
			url : url + id + "/",
			method : "DELETE"
		};
		var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
		if (res != null && res.status > 199 && res.status < 300) {
			return true;
		} else {
			return false;
		}
	}
}
ERPUtils.importOrderToFilterById=function(id) {
	if (id) {
		var param = {
			url : erp_api_service.TmpOrderFilter[0],
			data:{order_id:id},
			method : "POST"
			};
		var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
		if (res != null && res.status > 199 && res.status < 300) {
			return true;
		} else {
			return false;
		}
	}
}