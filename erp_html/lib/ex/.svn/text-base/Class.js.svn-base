function Class () {
    var len = arguments.length;
    var P = arguments[0];
    var F = arguments[len - 1];

    var C = typeof F.initialize == "function" ?
        F.initialize :
        function () { P.prototype.initialize.apply(this, arguments); };
    C.prototype = F;
    return C;
}
