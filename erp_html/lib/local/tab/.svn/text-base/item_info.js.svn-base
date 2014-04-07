var materia_data=[];
$(function ()
        {	 
	 		 var panel = frameElement.panel;
	         var dialogData = panel.get('data');
            //创建表单结构 
            
            $.ajax({
	            type: 'GET',
	            url: erp_api_service.EntItem[0]+"?callback=?&number="+dialogData.number,
	            dataType: 'json',
	            cache: false,
	            async: true,
	            success: function(data) {
	            	if(data&&data.objects)
	            	{
	            		var res=data.objects;
	            		item_info.setData(res[0]);
	            		$.ajax({
	                           type: 'GET',
	                           url: erp_api_service.EntMaterial[0]+"?callback=?&id="+res[0].material,
	                           dataType: 'json',
	                           cache: false,
	                           async: true,
	                           success: function(data) {
	                           	if(data&&data.objects)
	                           	{
	                           		if(data.objects.length<=0){
	                           			var tempName={name:'目前没有该部品的材料信息'};
	                           			materia_data.push(tempName);
	                           			item_info.setData({ 
	                                        name:materia_data[0].name
	                                    });
	                           		}
	                           		else{
	                           			var res=data.objects;
	                           			materia_data.push(res[0]);
	                           			item_info.setData({ 
	                                        name:materia_data[0].name
	                                    });
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
            var item_info= $("#item_form").ligerForm({
                inputWidth: 170, labelWidth: 90, space: 40,
                fields: [
                { name: "id", type: "hidden" },
                { display: "部品编号", name: "number",newline: true, type: "text",editor:{readonly:true}},
                { display: "材料", name:"name",newline: true, type: "text",
                  editor:{ readonly:true, data:materia_data[0]} 
                },
                { display: "备注", name: "remark", newline: true, type: "text", editor:{readonly:true} }
                ]
            });
      });
         