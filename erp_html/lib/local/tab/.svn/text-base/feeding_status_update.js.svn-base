﻿var tracking_data = [];
var entity_edit_model = {
	menu : null,
	url_index : 0,
	url : erp_api_service.VFeedingTracking,
	top_menu : null,
	default_pages_size : 15,// 默认页面大小
	pages_size : [ 10, 15, 30, 50, 100 ],// 定义分页时 页面的大小级别
	innerGrid : [],
	dispaly_columns : [ {
		display : '主键',
		name : 'id',
		filter : false,
		width : 50,
		type : 'int'
	}, {
		display : '部品编号',
		name : 'item_number',
		// width : 150,
		type : 'int'
	}, {
		display : '投料数量',
		name : 'feeding_count',
		width : 100
	}, {
		display : '投料日期',
		name : 'feeding_date',
		width : 150,
		type : 'date',
		format : 'yyyy-MM-dd hh:mm:ss'
	}, {
		display : '投料单状态',
		name : 'storage_mark',
		width : 70,
		render : function(rowdata, rowindex, value) {
			if (value + '' == '0') {
				return "未入库";
			}
			if (value + '' == '1') {
				return "已入库";
			}
		}
	}, {
		display : '已完成工序',
		name : 'feeding_status_now',
		width : 80
	}, {
		display : '总共工序',
		name : 'feeding_status_all',
		width : 80
	}, {
		display : '添加时间',
		name : 'i_time',
		width : 150,
		type : 'date',
		format : 'yyyy-MM-dd hh:mm:ss'
	} ],
	dispaly_columns1 : [
			{
				display : '主键',
				name : 'id',
				filter : false,
				width : 50,
				type : 'int'
			},
			{
				display : '部品编号',
				name : 'item_number',
				width : 150
			},
			{
				display : '投料单ID',
				name : 'feeding_id',
				width : 50,
				type : 'int'
			},
			{
				display : '工艺ID',
				name : 'step_tie_id',
				width : 50,
				type : 'int'
			},
			{
				display : '步骤名称',
				name : 'step_name',
				width : 150
			},
			{
				display : '步骤顺序',
				name : 'step_rank',
				width : 50
			},
			{
				display : '步骤状态',
				name : 'step_status',
				width : 50,
				render : function(rowdata, rowindex, value) {
					if (value + '' == '0') {
						return "未完";
					}
					if (value + '' == '1') {
						return "已完";
					}
				}
			},
			{
				display : '操作',
				name : 'step_status',
				width : 50,
				render : function(rowdata, rowindex, value) {
					if (value + '' == '0') 
					{
						return "<button onClick='change_status_to_complete("
						+ rowdata.id+ ")'>完成</button>";
					}
				}
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
			} ]
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
	entity_edit_model.manager = $("#item")
			.ligerGrid(
					ERPUtils
							.get_default_grid_option_for_url({
								url : entity_edit_model.url[entity_edit_model.url_index],
								columns : entity_edit_model.dispaly_columns,
								toolbar : {
									items : [
											{
												text : '高级自定义查询',
												click : function() {
													entity_edit_model.manager
															.showFilter("#filter");
												},
												icon : 'search2'
											}, {
												line : true
											} ]
								},
								isScroll : false,
								width : 'auto',
								detail : {
									height : 'auto',
									onShowDetail : function(row, detailPanel,
											callback) {
										var grid = document
												.createElement('div');
										$(detailPanel).append(grid);
										var g = $(grid)
												.css('margin', 10)
												.ligerGrid(
														ERPUtils
																.get_default_grid_option_for_url({
																	width : 'auto',
																	url : erp_api_service.EntFeedingStatus[0]
																			+ "?feeding_id="
																			+ row.id
																			+ "&order_by=step_rank",
																	columns : entity_edit_model.dispaly_columns1
																}));
										entity_edit_model.innerGrid.push(g);
									}
								}
							}));
}
function change_status_to_complete(status_id) {
	alert(status_id);
	param = {
		url : erp_api_service.EntFeedingStatus[0] + status_id + '/',
		method : "PATCH",
		data : {
			'step_status' : '1'
		}
	};
	var res = bridge_map.ajax_auto(param);
	if (res.status == 202) {
		tipOnce("提示", Util.formatString("修改成功", res ? res.status : null), 10000)
		for ( var i in entity_edit_model.innerGrid)
			entity_edit_model.innerGrid[i].reload();
	} else {
		tipOnce("提示", Util.formatString("修改失败，请重试[失败码:{0}]", res ? res.status
				: null), 10000)
	}
}