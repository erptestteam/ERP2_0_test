//扩展 ligerGrid 的 搜索功能(高级自定义查询).应用: demos/filter/grid.htm
$.ligerui.controls.Grid.prototype.showFilter = function (panelDiv,title)
{
	
    var g = this, p = this.options;
    //var filter;
    if (g.winfilter)
    {
    	if(panelDiv)
    	{
    		if(g.winfilter.__show)
    		{
    			$(panelDiv).hide();//g.winfilter.close();
    			g.winfilter.__show=false;
    			loadData(true);
    			return;
    		}
    		else
    		{
    			$(panelDiv).show();//g.winfilter.close();
    			g.winfilter.__show=true;
    			loadData();
    			return;
    		}
    	}
    	else
    	{
    		g.winfilter.show();
    		return;
    	}
    }
    if(panelDiv)
    {
       // var filtercontainer = $('filterDiv').width(380).height(120); 
    	//var _filtercontainer = $();
    	g.winfilter =$(panelDiv).ligerPanel({
  	       title : title?title:'查询条件',
  	       width: "100%",
  	       height: document.all ?20:'outo'
  	      // isResize: true
  	    });
    	$(panelDiv).append('<div id="' + g.id + '_filtercontainer"></div>');
    	$(panelDiv).append('<input id="' + g.id + '_filtercontainer_button_ok" type="button" value="确定">');
    	$(panelDiv).append('<input id="' + g.id + '_filtercontainer_button_cancel" type="button" value="取消">');
//    	$('<div id="' + g.id + '_filtercontainer1"></div>').appendTo(panelDiv);
//    	$(button_ok).appendTo(panelDiv);
//    	$(button_cancel).appendTo(panelDiv);
    	
    	
        g.__filter = $('#' + g.id + '_filtercontainer').ligerFilter({ fields: getFields() });

    	 $('#' + g.id + '_filtercontainer_button_ok').unbind().bind('click', function() {
    		loadData();
    	});
    	 $('#' + g.id + '_filtercontainer_button_cancel').unbind().bind('click', function() {
 			$(panelDiv).hide();//g.winfilter.close();
			g.winfilter.__show=false;
			loadData(true);
			return;
    	 });
    	 g.winfilter.__show=true;
    	return g.winfilter;
    }
    else
    {
    	 var filtercontainer = $('<div id="' + g.id + '_filtercontainer"></div>').width(380).height(120).hide(); 
    	    g.__filter = filtercontainer.ligerFilter({ fields: getFields() });
    	    return g.winfilter = $.ligerDialog.open({
    	    	  title : title?title:'查询条件',
    	        width: 420, height: 208,
    	        target: filtercontainer, isResize: true, top: 50,
    	        buttons: [
    	            { text: '确定', onclick: function (item, dialog) {loadData(); dialog.hide(); } },
    	            { text: '取消', onclick: function (item, dialog) { dialog.hide(); } }
    	            ]
    	    }); 
    }
   

    //将grid的columns转换为filter的fields
    function getFields()
    {
        var fields = [];
        //如果是多表头，那么g.columns为最低级的列
        $(g.columns).each(function ()
        {
            var o = { name: this.name, display: this.display,filter:this.filter};
            var isNumber = this.type == "int" || this.type == "number" || this.type == "float";
            var isDate = this.type == "date";
            if (isNumber) o.type = "number";
            if (isDate) 
            {
            	o.type = "date";
            	o.editor = {type: 'date',showTime:true};
            }
            if (this.editor)
            {
                o.editor = this.editor;
            }
            if(o.filter!=false)
            	fields.push(o);
        });
        return fields;
    }

    function loadData(notUseFilter)
    {
    	var data=null;
    	if(!notUseFilter)
    	{
    		data = g.__filter.getData();
    	}
        if (g.options.dataAction == "server")
        {
            //服务器过滤数据
            loadServerData(data);
        }
        else
        {
            //本地过滤数据
            loadClientData(data);
        }
    }

    function loadServerData(data)
    { 
    	//console_info(data);
        if (data && data.rules && data.rules.length)
        {
            g.set('parms', { where: JSON2.stringify(data) });
            //console_info({ where: JSON2.stringify(data) });
        } else
        {
            g.set('parms', {});
        }
        g.loadData();
    }
    function loadClientData(data)
    {
        var fnbody = ' return  ' + filterTranslator.translateGroup(data);
        g.loadData(new Function("o", fnbody));
    } 

};


var filterTranslator = {
    
    translateGroup : function (group)
    {
        var out = [];
        if (group == null) return " 1==1 ";
        var appended = false;
        out.push('(');
        if (group.rules != null)
        {
            for (var i in group.rules)
            {
                var rule = group.rules[i];
                if (appended)
                    out.push(this.getOperatorQueryText(group.op));
                out.push(this.translateRule(rule));
                appended = true;
            }
        }
        if (group.groups != null)
        {
            for (var j in group.groups)
            {
                var subgroup = group.groups[j];
                if (appended)
                    out.push(this.getOperatorQueryText(group.op));
                out.push(this.translateGroup(subgroup));
                appended = true;
            }
        }
        out.push(')');
        if (appended == false) return " 1==1 ";
        return out.join('');
    },

    translateRule : function(rule)
    {
        var out = [];
        if (rule == null) return " 1==1 ";
        if (rule.op == "like" || rule.op == "startwith" || rule.op == "endwith")
        {
            out.push('/');
            if (rule.op == "startwith")
                out.push('^');
            out.push(rule.value);
            if (rule.op == "endwith")
                out.push('$');
            out.push('/i.test(');
            out.push('o["');
            out.push(rule.field);
            out.push('"]');
            out.push(')');
            return out.join('');
        }
        out.push('o["');
        out.push(rule.field);
        out.push('"]');
        out.push(this.getOperatorQueryText(rule.op));
        out.push('"');
        out.push(rule.value);
        out.push('"');
        return out.join('');
    },


    getOperatorQueryText : function(op)
    {
        switch (op)
        {
            case "equal":
                return " == ";
            case "notequal":
                return " != ";
            case "greater":
                return " > ";
            case "greaterorequal":
                return " >= ";
            case "less":
                return " < ";
            case "lessorequal":
                return " <= ";
            case "and":
                return " && ";
            case "or":
                return " || ";
            default:
                return " == ";
        }
    }

};