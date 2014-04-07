  $(function (){
	  var panel = frameElement.panel;
      var dialogData = panel.get('data');
      
	  getItemTree(dialogData.number,true,function(tree){
                $("#shwow_item_bom").css('margin',10).ligerGrid({
                	columns:
                    	[
                         {
                       	  display: '子件', name: 'c', id:"id1", align: 'left',
                       	  editor: { type: 'text', height: 60 }
                         },
                         {
                       	  display: '层次', name: 'l', width: 100,isSort: false,
                       	  editor: { type: 'text', height: 60 }
                         },
                         {
                        	 display: '数量', name: 'n', width: 100,isSort: false,
                        	 editor: { type: 'text', height: 60 }
                         }
                         ], 
                         tree: { columnId: 'id1' },
                         isScroll: false,//当 父容器detail: { height:'auto', 。。设置后  此参数失效 
                         showToggleColBtn: false,
                         width: '90%',
                         data: {Rows:tree}, 
                         showTitle: false, 
                         //enabledSort:false,//不允许排序
                        // columnWidth: 100,
                         rownumbers:true,
                         frozen:false
                });  
        	}) ;
  })