﻿var tracking_data = [];
var entity_edit_model = {
    menu : null,
    url_index : 0,
    url:erp_api_service.VOrderAnalysis[0],
    top_menu : null,
    default_pages_size : 15,// 默认页面大小
    pages_size : [ 10, 15, 30, 50, 100 ],// 定义分页时 页面的大小级别
    dispaly_columns : [
        { 
        	display: '订单ID', 
        	name: 'order_id', 
        	width: 50, 
        	type: 'int' 
        },
        {
            display: '订单号', name: 'order_number', width: 70,
            editor: { type: 'text', height: 60 }
        },
        {
            display: '订单批号', name: 'order_batch_number', width: 50,
            editor: { type: 'text' }
        },
        {
            display: '顶部品', name: 't', align: 'center', width: 100,
            editor: { type: 'text', height: 60 }
        },
        {
            display: '订单量', name: 'order_count', align: 'center', type:'int', width: 50,
            editor: { type: 'int', height: 60 }
        },
        {
            display: '父部品', name: 'p', align: 'center', width: 100,
            editor: { type: 'text', height: 60 }
        },
        {
            display: '子部品', name: 'c', align: 'center', width: 100,
            editor: { type: 'text', height: 60 }
        },
        {
            display: '数量', name: 'n', align: 'center', width: 50,
            editor: { type: 'text', height: 60 }
        },
        {
            display: '订单需量', name: 'order_need', align: 'center', type:'int', width: 50,
            editor: { type: 'int', height: 60 }
        },
        {
            display: '库存数量', name: 'storage',  align: 'center', width: 50,
            editor: { type: 'text', height: 60 }
        },
        {
            display: '已投数量', name: 'future_count',  align: 'center', width: 50,
            editor: { type: 'text', height: 60 }
        },
        {
            display: '需要生产', name: 'from_product',  align: 'center', width: 50,
            editor: { type: 'text', height: 60 }
        },
        {
            display: '纳期', name: 'order_lead_time', type: 'date',
            format: 'yyyy年MM月dd',  align: 'center',width: 100,
            editor: { type: 'date',format: 'yyyy-MM-dd'}
        },
        {
            display: '调整投料数量',
            width : 50,
            type: 'int'
        },
        {
            display: '投料',
            width : 50,
            render : function(rowdata, rowindex, value) {
                if (value + '' == '0') {
                    return "未完";
                    }
                if (value + '' == '1') {
                    return "已完";
                    }
                }
        }
        ]
};
$(function() {
	$.ajax({
        type : 'GET',
        url : erp_api_service.VOrderAnalysis[0] + "?callback=?&limit=1000",
        dataType : 'json',
        cache : false,
        async : true,
        success : function(data) {
            if (data && data.objects) {
                var res = data.objects;
                console_info(res);
                if (res instanceof Array && res.length > 0) {
                    for ( var i in res) {
                        tracking_data.push(res[i]);
                    }
                } else {
                    tipOnce("提示", "获取投料单信息失败,请刷新。", 10000);
                }
            } else {
                tipOnce("提示", "获取投料单信息失败,请刷新。", 10000);
            }
        },
        error : function(XMLHttpRequest) {
            tipOnce("提示", "获取投料单信息失败,请刷新。", 10000);
        }
    });
    $(f_initGrid);
});
function f_initGrid() {
    // 添加顶层菜单栏
    $("#top_menu").ligerMenuBar({
        items : [ {
            text : '文件',
            menu : {
                width : 120,
                items : [ {
                    text : '保存',
                    click : function() {
                    }
                }, {
                    text : '列存为',
                    click : function() {
                    }
                }, {
                    line : true
                }, {
                    text : '关闭',
                    click : function() {
                    }
                } ]
            }
        } ]
    });
    // 鼠标右键
    entity_edit_model.menu = $.ligerMenu({
        top : 100,
        left : 100,
        width : 120,
        items : []
    });
    $("#item").bind("contextmenu", function(e) {
        entity_edit_model.menu.show({
            top : e.pageY,
            left : e.pageX
        });
        return false;
    });
    $.ligerDefaults.Filter.operators['string'] = $.ligerDefaults.Filter.operators['text'] = [
            "like", "equal", "notequal", "startwith", "endwith" ];
    $.ligerDefaults.Filter.operators['int'] = [ "equal", "notequal" ];
    entity_edit_model.manager = $("#item").ligerGrid(
        ERPUtils.get_default_grid_option_for_url({
        url : erp_api_service.VOrderAnalysis[0],
        columns : entity_edit_model.dispaly_columns,
        toolbar : {
        items : [
                 {
                     text : '高级自定义查询',
                     click : function() {
                         entity_edit_model.manager.showFilter("#filter");
                         },
                     icon : 'search2'
                 },
                 { line: true }
                 ]
        },
        isScroll : false,
        width : 'auto'
        }));
}