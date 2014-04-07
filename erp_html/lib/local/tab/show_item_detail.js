$(function (){  
	    var dialog = frameElement.dialog;
	    var dialogData = dialog.get('data');
            $("#portalMain").ligerPortal({
                draggable : true,
                rows: [ 
                    {
                        columns: [{
                            width: '100%',
                            panels: [
                                     {
                                title: dialogData.number+'的基本信息',
                                width: '100%',
                                height: 130,
                                frameName:'content1',
                                data: {
                           			 number: dialogData.number
                           		 },
                                url:'../tab/item_info.html'
                            },
                            {
                                title: dialogData.number+'的BOM结构',
                                width: '100%',
                                height:300,
                                data: {
                          			 number:dialogData.number
                          		 },
                                url:'../tab/item_bom_info.html'
                            },
                            {
                                title: dialogData.number+'的工序',
                                width: '100%',
                                height:300,
                                data: {
                          			 number:dialogData.number
                          		 },
                                url:'../tab/item_technology_info.html'
                            }
                            ]
                        } 
                          ]
                        }
                        ]
            }); 
}); 
