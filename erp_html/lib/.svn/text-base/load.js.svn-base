/// <reference path="ex/ligeruiutils.js" />
/// <reference path="bridge_map.js" />
/// <reference path="util/utils.js" />
loadJsCssFile = function(filename, filetype) {
    if (filetype == "js") { //
        document.write("<script src='" + filename + "'></script>");
        //var fileref=document.createElement('script')//
        //fileref.setAttribute("type","text/javascript")//text/javascript 
        //fileref.setAttribute("src", filename)// 
    } else if (filetype == "css") { //
        //document.write();
        var fileref = document.createElement("link")
        fileref.setAttribute("rel", "stylesheet")
        fileref.setAttribute("type", "text/css")
        fileref.setAttribute("href", filename)
    }
    if (typeof fileref != "undefined") document.getElementsByTagName("head")[0].appendChild(fileref)
}

scripLoction = (function() {
    var r = new RegExp("(^|(.*?\\/))(load.js)(\\?|$)"),
        s = document.getElementsByTagName('script'),
        src, m, l = "";
    for (var i = 0, len = s.length; i < len; i++) {
        src = s[i].getAttribute('src');
        if (src) {
            m = src.match(r);
            if (m) {
                l = m[1];
                break;
            }
        }
    }
    return (function() {
        return l;
    });
})();
//�����load��js�ļ�������css/js�ļ�,filename�ײ�����Ҫ��"/"
loadJsCssFileRelToLoadJs = function(filename, filetype) {
	loadJsCssFile(scripLoction()+filename,filetype);
}
//console.info(scripLoction()+"1");
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/skins/Aqua/css/ligerui-all.css', 'css');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/skins/ligerui-icons.css', 'css');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/skins/Gray/css/all.css', 'css'); //
//loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/skins/Gray2014/css/all.css', 'css');//
//loadJsCssFile(scripLoction()+'ligerUI/ligerUI/skins/Aqua/css/ligerui-all.css', 'css');//


loadJsCssFile(scripLoction() + 'ligerUI/jquery/jquery-1.3.2.min.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/jquery.cookie.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/json2.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/core/base.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/ligerui.all.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerGrid.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerToolBar.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerResizable.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerCheckBox.js', 'js');

loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerLayout.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerTab.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerDrag.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerTree.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerComboBox.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerTextBox.js', 'js');

loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerDialog.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerAccordion.js', 'js');


loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerGrid.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerDateEditor.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerSpinner.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerForm.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerGrid.showFilter.js', 'js');

loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerWindow.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerPortal.js', 'js');
loadJsCssFile(scripLoction() + 'ligerUI/ligerUI/js/plugins/ligerPanel.js', 'js');



loadJsCssFile(scripLoction() + 'ex/Class.js', 'js');
loadJsCssFile(scripLoction() + 'ex/Event.js', 'js');
loadJsCssFile(scripLoction() + 'ex/TimerTask.js', 'js');
loadJsCssFile(scripLoction() + 'ex/Utils.js', 'js');
loadJsCssFile(scripLoction() + 'ex/LigerUIUtils.js', 'js');
loadJsCssFile(scripLoction() + 'ex/ERPUtils.js', 'js');


loadJsCssFile(scripLoction() + 'local/service_api.js', 'js'); //
loadJsCssFile(scripLoction() + 'local/bridge_map.js', 'js'); //


//loadJsCssFile(scripLoction()+'local/item/item.js','js');
//  <script src="../CustomersData.js" type="text/javascript"></script>