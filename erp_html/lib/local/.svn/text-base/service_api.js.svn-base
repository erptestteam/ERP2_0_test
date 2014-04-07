//var erp_api_service_base = "http://192.168.0.100:80/erp2/api/v1/";
var erp_api_service_base = "http://61.160.98.53:5002/erp2/api/v1/";
var erp_api_service_trash = "http://61.160.98.53:5002/erp2/api/trash/v1/";
var erp_api_service_super = "http://61.160.98.53:5002/erp2/superAPI/";

var erp_file_service_check = "http://localhost:8080/upload";// ?file=1A7180-27701.pdf
var erp_file_service_upload = "http://localhost:8080/upload";// ?file=1A7180-27701.pdf

var erp_api_service = {
	EntFeeding : [ erp_api_service_base + "EntFeeding/",
					erp_api_service_trash + "EntFeeding/" ],
	EntFeedingStatus : [ erp_api_service_base + "EntFeedingStatus/",
					erp_api_service_trash + "EntFeedingStatus/" ],
	EntUser : [ erp_api_service_base + "EntUser/",
			erp_api_service_trash + "EntUser/" ],
	EntMenu : [ erp_api_service_base + "EntMenu/",
			erp_api_service_trash + "EntMenu/" ],
	EntMaterial : [ erp_api_service_base + "EntMaterial/",
			erp_api_service_trash + "EntMaterial/" ],
	EntMachine : [ erp_api_service_base + "EntMachine/",
			erp_api_service_trash + "EntMachine/" ],
	EntRelItemItem : [ erp_api_service_base + "EntRelItemItem/",
			erp_api_service_trash + "EntRelItemItem/" ],
	EntOrder : [ erp_api_service_base + "EntOrder/",
			erp_api_service_trash + "EntOrder/" ],

	EntItem : [ erp_api_service_base + "EntItem/",
			erp_api_service_trash + "EntItem/" ],
	EntTechnology : [ erp_api_service_base + "EntTechnology/",
			erp_api_service_trash + "EntTechnology/" ],
	
	EntStorage:[erp_api_service_base + "EntStorage/"],
	EntStorageChangesRecord:[erp_api_service_base + "EntStorageChangesRecord/"],
	
	EntRelTechnologyItemEquipment : [ erp_api_service_base
			+ "EntRelTechnologyItemEquipment/" ],

	EntRelMachineItem : [ erp_api_service_base + "EntRelMachineItem/" ],
	EntRelItemItem : [ erp_api_service_base + "EntRelItemItem/" ],
	
	EntRelStorageItem:[ erp_api_service_base + "EntRelStorageItem/" ],

	TmpOrderFilter : [ erp_api_service_base + "TmpOrderFilter/" ],
	TmpItemFullRel : [ erp_api_service_base + "TmpItemFullRel/" ],
	TmpOrderAnalysis : [ erp_api_service_base + "TmpOrderAnalysis/" ],

	VFeedingTracking : [erp_api_service_base + "VFeedingTracking/"],
	VOrder : [ erp_api_service_base + "VOrder/" ],
	VOrderAnalysis : [ erp_api_service_base + "VOrderAnalysis/" ],
	VOrderFilterExtract : [ erp_api_service_base + "VOrderFilterExtract/" ],
	VOrderAnalysis2 : [ erp_api_service_base + "VOrderAnalysis2/" ],

	TmpOrder : [ erp_api_service_base + "TmpOrder/" ],
	SuperAPI : [ erp_api_service_super + "superAPI/" ]
};
var erp_api_sql = {
	truncate_tmp_order : "TRUNCATE TABLE `tmp_order`",
	procedure_item_tree_create_all : "call item_tree_create_all()",
	procedure_item_tree_create_by_number : "call item_tree_create_by_number('{0}')",
	procedure_order_analysis4 : "call order_analysis4({0},{1},{2})",
	procedure_order_analysis3 : "call order_analysis3({0},{1},{2})",
	procedure_order_analysis2 : "call order_analysis2({0},{1})"
};
var erp_api_order_sys_status = {
	lead_overtime : '.0.1...',// 订单纳期超时(.0.1...)|(.0..1..)|(.0...1.)
	item_not_exists : '.0..1..',
	info_miss : '.0...1.',
	has_dead : '.1.....',
	has_analysis : '..1....'
};
var erp_api_order_sys_status_regexp = {
	lead_overtime : new RegExp(erp_api_order_sys_status.lead_overtime, "g"),
	item_not_exists : new RegExp(erp_api_order_sys_status.item_not_exists, "g"),
	info_miss : new RegExp(erp_api_order_sys_status.info_miss, "g"),
	has_dead : new RegExp(erp_api_order_sys_status.has_dead, "g"),
	has_analysis : new RegExp(erp_api_order_sys_status.has_analysis, "g")
};