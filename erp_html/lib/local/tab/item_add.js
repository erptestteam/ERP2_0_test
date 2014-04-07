$(function (){
	 //tipOnce("提示", "添加成功", 5000);
		 var param={
			 url: erp_api_service.EntMaterial[0],
             method: "GET"
			 };
	    var res = JSON.parse(bridge_map.ajax(JSON.stringify(param)));
	    if(res&&res.result)
	    {
	    	var materiadata=JSON.parse(res.result).objects;
	    	$("#material").ligerComboBox(
	    			{
	    				data: materiadata,
	    				width:'300px',
	    				valueField : 'id',
	    				textField: 'name',
	    				emptyText: '(空)',
	    				onSelected: function (newvalue)
	    				{
	    					materialId=newvalue;
	    				}
	    			}
	    	);
	    }
	});
function add_item()
{
	var item=
	{
			"d_time": null,
     		"i_time": new Date().pattern("yyyy-MM-dd hh:mm:ss"),
     		"meterial": materialId,
     		"number": $("#item_No").val(),
     		"remark": $("#remark").val(),
     		"u_time": null
	};
	 var param={
			 url: erp_api_service.EntItem,
             method: "POST",
             data:item
	 };
	 alert(JSON.stringify(param));
	var r=bridge_map.ajax(JSON.stringify(param));
	var res = JSON.parse(r);
	if(res.status>=200&&res.status<300)
	{
		tipOnce("提示", "添加成功", 5000);
		alert("添加成功");
	}
	else
	{
		tipOnce("提示", "添加失败", 10000);
		alert(res.status);
	}
	
}
function go_bom_page()

{
	 $.ligerDialog.open({ height: 600,width:600,url: 'item_bom.html' });
}
	
	