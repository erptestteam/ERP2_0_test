//var is_ie_tag = fdocument.all ? true : false;
var use_bridge_tag = document.all ? true : false;
var bridge_map = {
    
      /*
        requestEncoding:"utf-8"
        method:"get"
        userAgent:"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
        contentType:"application/json"
        accept:"application/json"
        timeout:20
        data:{}
      */
    
    ajax: function (o)
    {
        if (use_bridge_tag)
            return window.external.ajax(o);
        return null;
    },
    ajax_auto:function (param)
    {
    	if (use_bridge_tag)
    	{
    		if(param)
    		{
    			var res= window.external.ajax(JSON.stringify(param));
    			if(res)
    			{
    				return JSON.parse(res)
    			}
    		}
    	}
    	return null;
    },
    /**
     *  provider:"Microsoft.Jet.OLEDB.4.0"
     *  extended_properties:"Excel 8.0;HDR=Yes;IMEX=2"
     *  data_source:            *
     *  sql:                    *
     */
    import_order: function (param) {
        if (use_bridge_tag)
        {
        	var res= window.external.import_order(JSON.stringify(param));
        	//alert(res);
        	if(res)
			{
				return JSON.parse(res);
			}
        }
        return null;
    },
    get_excel_info:function ()
    {
        if (use_bridge_tag) {
            return window.external.get_excel_info();
        }
        return null;
    },
    super_api:function (sql)
    {
    	return this.ajax_auto({
    		method:"get",
    		url:erp_api_service_super+sql+"/",
    		timeout:12000
    	});
    },
    save_user_info:function( key , value)
    {
    	 if (use_bridge_tag) {
             return window.external.save_user_info(key,value);
         }
    },
    get_user_info:function( key )
    {
    	if (use_bridge_tag) {
    		return window.external.get_user_info(key);
    	}
    }
};
var console_info=function(s)
{
    if (!use_bridge_tag)
    {
        console.info(s);
    }
};
