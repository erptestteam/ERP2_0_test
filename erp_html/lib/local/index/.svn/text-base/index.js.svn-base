var global_model = {
    layout_container:null,
    tab_center: null,
    menu_tree_data: null,
    center_height: null,
    menu_accordion: null,
    tabItems:[]
}
$(function () {
    $("#container").ligerLayout({
        leftWidth: 200,
        topHeight: 100,
        bottomHeight: 30,
        allowBottomResize: false,
        allowLeftResize: false,
        allowTopResize: false,
        height: '100%',
        // heightDiff: -34,
        space: 4,
        onHeightChanged: function f_heightChanged(options) {
            if (global_model.tab_center)
                global_model.tab_center.addHeight(options.diff);
            if (global_model.menu_accordion && options.middleHeight - 24 > 0)
                global_model.menu_accordion.setHeight(options.middleHeight - 24);
        }
    });

    global_model.center_height = $(".l-layout-center").height();
    $("#center").ligerTab(
        {
            height: global_model.center_height,
            showSwitchInTab: true,
            changeHeightOnResize: true,
            contextmenu: true,
            showSwitch: true,
            onAfterAddTabItem: function (tabdata) {
                global_model.tabItems.push(tabdata);
                saveTabStatus();
            },
            onAfterRemoveTabItem: function (tabid) {
                for (var i = 0; i < global_model.tabItems.length; i++) {
                    var o = global_model.tabItems[i];
                    if (o.tabid == tabid) {
                        global_model.tabItems.splice(i, 1);
                        saveTabStatus();
                        break;
                    }
                }
            },
            onReload: function (tabdata) {
                var tabid = tabdata.tabid;
                addFrameSkinLink(tabid);
            }
        }
     );
    $("#menu_accordion").ligerAccordion(
        {
            height: global_model.center_height - 24,
            changeHeightOnResize: true,
            speed: null
        }
     );
    $(".l-link").hover(function () {
        $(this).addClass("l-link-over");
    }, function () {
        $(this).removeClass("l-link-over");
    });
    getMenus(function(menus)
    {global_model.menu_tree_data=menus;
    	 $("#menu_tree").ligerTree({
		        data: global_model.menu_tree_data,
		        checkbox: false,
		        slide: false,
		        nodeWidth: 120,
		        attribute: ['nodename', 'url'],
		        onSelect: function (node) {
		            if (!node.data.url) return;
		            var tabid = $(node.target).attr("tabid");
		            if (!tabid) {
		                tabid = new Date().getTime();
		                $(node.target).attr("tabid", tabid)
		            }
		            f_addTab(tabid, node.data.text, node.data.url);
		        }
		    });
    });
   

    global_model.layout_container = liger.get("container");
    global_model.tab_center = liger.get("center");
    global_model.menu_accordion = liger.get("menu_accordion");

    css_init();
    pages_init();
});
function f_addTab(tabid, text, url) {
    global_model.tab_center.addTabItem({
        tabid: tabid,
        text: text,
        url: url,
        callback: function () {
           // addShowCodeBtn(tabid);
            addFrameSkinLink(tabid);
        }
    });
}

function addShowCodeBtn(tabid) {
    var viewSourceBtn = $('<a class="viewsourcelink" href="javascript:void(0)">查看源码</a>');
    var jiframe = $("#" + tabid);
    viewSourceBtn.insertBefore(jiframe);
    viewSourceBtn.click(function () {
        showCodeView(jiframe.attr("src"));
    }).hover(function () {
        viewSourceBtn.addClass("viewsourcelink-over");
    }, function () {
        viewSourceBtn.removeClass("viewsourcelink-over");
    });
}
function showCodeView(src) {
    $.ligerDialog.open({
        title: '源码预览',
        url: 'dotnetdemos/codeView.aspx?src=' + src,
        width: $(window).width() * 0.9,
        height: $(window).height() * 0.9
    });

}
function addFrameSkinLink(tabid) {
    var prevHref = getLinkPrevHref(tabid) || "";
    var skin = getQueryString("skin");
    if (!skin) return;
    skin = skin.toLowerCase();
    attachLinkToFrame(tabid, prevHref + skin_links[skin]);
}
var skin_links = {
    "aqua": "lib/ligerUI/skins/Aqua/css/ligerui-all.css",
    "gray": "lib/ligerUI/skins/Gray/css/all.css",
    "silvery": "lib/ligerUI/skins/Silvery/css/style.css",
    "gray2014": "lib/ligerUI/skins/gray2014/css/all.css"
};
function pages_init() {
    var tabJson = $.cookie('liger-home-tab');
    if (tabJson) {
        var tabItems = JSON2.parse(tabJson);
        for (var i = 0; tabItems && tabItems[i]; i++) {
            f_addTab(tabItems[i].tabid, tabItems[i].text, tabItems[i].url);
        }
    }
}
function saveTabStatus() {
    $.cookie('liger-home-tab', JSON2.stringify(global_model.tabItems));
}
function css_init() {
    var css = $("#mylink").get(0), skin = getQueryString("skin");
    $("#skinSelect").val(skin);
    $("#skinSelect").change(function () {
        if (this.value) {
            location.href = "index.htm?skin=" + this.value;
        } else {
            location.href = "index.htm";
        }
    });


    if (!css || !skin) return;
    skin = skin.toLowerCase();
    $('body').addClass("body-" + skin);
    $(css).attr("href", skin_links[skin]);
}
function getQueryString(name) {
    var now_url = document.location.search.slice(1), q_array = now_url.split('&');
    for (var i = 0; i < q_array.length; i++) {
        var v_array = q_array[i].split('=');
        if (v_array[0] == name) {
            return v_array[1];
        }
    }
    return false;
}
function attachLinkToFrame(iframeId, filename) {
    if (!window.frames[iframeId]) return;
    var head = window.frames[iframeId].document.getElementsByTagName('head').item(0);
    var fileref = window.frames[iframeId].document.createElement("link");
    if (!fileref) return;
    fileref.setAttribute("rel", "stylesheet");
    fileref.setAttribute("type", "text/css");
    fileref.setAttribute("href", filename);
    head.appendChild(fileref);
}
function getLinkPrevHref(iframeId) {
    if (!window.frames[iframeId]) return;
    var head = window.frames[iframeId].document.getElementsByTagName('head').item(0);
    var links = $("link:first", head);
    for (var i = 0; links[i]; i++) {
        var href = $(links[i]).attr("href");
        if (href && href.toLowerCase().indexOf("ligerui") > 0) {
            return href.substring(0, href.toLowerCase().indexOf("lib"));
        }
    }
}
