var tracking_data = [];
var entity_edit_model = {
	menu : null,
	url_index : 0,
	url : erp_api_service.EntFeedingStatus,
	top_menu : null,
	default_pages_size : 15,// 默认页面大小
	pages_size : [ 10, 15, 30, 50, 100 ],// 定义分页时 页面的大小级别
	dispaly_columns : [ {
		display : '主键',
		name : 'id',
		filter : false,
		width : 50,
		type : 'int'
	}, {
		display : '部品编号',
		name : 'item_number',
		width : 150,
		type : 'int'
	}, {
		display : '投料单ID',
		name : 'feeding_id',
		width : 50,
		type : 'int'
	}, {
		display : '工艺ID',
		name : 'step_tie_id',
		width : 50,
		type : 'int'
	}, {
		display : '步骤名称',
		name : 'step_name',
		width : 150
	}, {
		display : '步骤顺序',
		name : 'step_rank',
		width : 50
	}, {
		display : '步骤状态',
		name : 'step_status',
		width : 50
	}, {
		display : '添加时间',
		name : 'i_time',
		type : 'date',
		format : 'yyyy-MM-dd hh:mm:ss',
		width : 150
	}, {
		display : '更改时间',
		name : 'u_time',
		type : 'date',
		format : 'yyyy-MM-dd hh:mm:ss',
		width : 150
	}]
};
$(function() {
	$.ajax({
		type : 'GET',
		url : erp_api_service.EntFeedingStatus[0] + "?callback=?&limit=1000",
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
					tipOnce("提示", "获取材料信息失败,请刷新。", 10000);
				}

			} else {
				tipOnce("提示", "获取材料信息失败,请刷新。", 10000);
			}
		},
		error : function(XMLHttpRequest) {
			tipOnce("提示", "获取材料信息失败,请刷新。", 10000);
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
				url : entity_edit_model.url[entity_edit_model.url_index],
				columns : entity_edit_model.dispaly_columns,
				toolbar : {
					items : [ {
						text : '高级自定义查询',
						click : function() {
							entity_edit_model.manager.showFilter("#filter");
						},
						icon : 'search2'
					}, {
						line : true
					} ]
				},
				groupColumnName : 'feeding_id',
				groupRender : function(city, groupdata) {
					return '投料单' + city + ' 跟踪状态数：' + groupdata.length;
				}
			}));
}