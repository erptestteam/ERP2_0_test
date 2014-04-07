$(function() {
	var panel = frameElement.panel;
	var dialogData = panel.get('data');
	$.ajax({
		type : 'GET',
		url : erp_api_service.EntRelTechnologyItemEquipment[0]
				+ "?callback=?&item_number=" + dialogData.number,
		dataType : 'json',
		cache : false,
		async : true,
		success : function(data) {
			if (data && data.objects) {
				data.Rows=data.objects;
				data.Total=data.meta.total_count;
				if (data.objects.length <= 0) {
					initForm();
				} 
				else 
				{
					//delete(data.objects);
					initGrid(data);
				}
					
				}
			 else {
				tipOnce("提示", "获取材料信息失败,请刷新。", 10000);
			}
		},
		error : function(XMLHttpRequest) {
			tipOnce("提示", "获取材料信息失败,请刷新。", 10000);
			// alert(XMLHttpRequest.status);
		}
	});
	
	function initGrid(technology_data){
		$("#shwow_item_technology").ligerGrid({
			columns : [ 
			            {
				display : '工序步骤',
				name : 'technology_rank',
				width : 50,
				type : 'int'
			}, {
				display : '工序名称',
				name : 'technology_name',
				editor : {
					type : 'text'
				}
			}, {
				display : '工序信息',
				name : 'technology_info',
				editor : {
					type : 'text'
				}
			} 
			],
			data : technology_data,
			//enabledEdit : true,
			//detailToEdit : true,
			isScroll : false,
			
			frozen : false,
			width : '100%'
		});
	}
});

function initForm(){
	 var tech_form=$("#shwow_item_technology").ligerForm({
         inputWidth: 170, labelWidth: 90, space: 40,
         fields: 
        [
         { display: "部品工艺信息", name: "technology_name",newline: true, type: "text",editor:{readonly:true}}
         ]
     });
	 tech_form.setData({technology_name:"没有当前部品的工艺情况"});
}