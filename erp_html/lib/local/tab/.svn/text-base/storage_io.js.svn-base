$(function (){ 
	  $("#storage_io").ligerPortal({
          columns: [
            {
              width: "90%",
              panels: [{
                  title: '入库',
                  width: '100%',
                  height: 400,
                  url:'../tab/storage_in.html',
                  onLoaded:function(){
                	  this.toggle();
                  }
              },
              {
                  title: '出库',
                  width: '100%',
                  height: 400,
                  url: '../tab/storage_out.html',
                  onLoaded:function(){
                	  this.toggle();
                  }
              },
              {
                  title: '出库入库记录',
                  width: '100%',
                  height: 600,
                  url: '../tab/storage_io_record.html'
              }
              ]
           }
           ]
      }); 
});