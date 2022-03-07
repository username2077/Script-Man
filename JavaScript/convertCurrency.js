//转换为中文大写
function convertCurrency_CN(a) {
    var b = 9.999999999999E10,
        f = "零",h = "壹",g = "贰",e = "叁",k = "肆",p = "伍",q = "陆",r = "柒",s = "捌",t = "玖",
        l = "拾",d = "佰",i = "仟",m = "万",j = "亿",o = "元",c = "角",n = "分",v = "整";

    a = a.toString();
    b = a.split(".");
    if (b.length > 1) {
        a = b[0];
        b = b[1];
        b = b.substr(0, 2)
    } else {
        a = b[0];
        b = "";
    }
    h = new Array(f, h, g, e, k, p, q, r, s, t);
    l = new Array("", l, d, i);
    m = new Array("", m, j);
    n = new Array(c, n);
    c = "";
    if (Number(a) > 0) {
        for (d = j = 0; d < a.length; d++) {
            e = a.length - d - 1;
            i = a.substr(d,1);
            g = e / 4;
            e = e % 4;
            if (i == "0"){
                j++;
            }else{
                if (j > 0) {c += h[0];}
                j = 0;
                c += h[Number(i)] + l[e];
            }
            if (e == 0 && j < 4) {c += m[g];}
        }
        c += o;
    }
    if (b != "") {
        for (d = 0; d < b.length; d++) {
            i = b.substr(d, 1);
            if (i != "0") c += h[Number(i)] + n[d];
        }
    }
    if (c == "") {c = f + o;}
    if (b.length < 2) {c += v;}
    return c = c;
}

//英文转换整数部分
function intergernumber(a) {
    var b = a.length,
        f, h = 0,
        g = "",
        e = Math.ceil(b / 3),
        k = b - e * 3;
        g = "";
    for (f = k; f < b; f += 3) {
        ++h;
        num3 = f >= 0 ? a.substring(f, f + 3) : a.substring(0, k + 3);
        strEng = English(num3);
        if (strEng != "") {
            if (g != "") g += ",";
            g += English(num3) + arr1[e - h]
        }
    }
    return g.toUpperCase();
}

//英文转换小数部分
function decimalnumber(a) {
    var b = a.length,
        f, h = 0,
        g = "",
        e = Math.ceil(b / 3),
        k = b - e * 3;
        g = "";
    for (f = k; f < b; f += 3) {
        ++h;
        num3 = f >= 0 ? a.substring(f, f + 3) : a.substring(0, k + 3);
        strEng = English(num3);
        if (strEng != "") {
            if (g != "") g += ",";
            g += English(num3) + arr1[e - h]
        }
    }
    return "CENTS "+g.toUpperCase();
}

var arr1 = new Array("", " thousand", " million", " billion"),
    arr2 = new Array("zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"),
    arr3 = new Array("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"),
    arr4 = new Array("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen");

//整数数字转换英文大写
function numbertotext(a) {
    var b = a.length,
        f, h = 0,
        g = "",
        e = Math.ceil(b / 3),
        k = b - e * 3;
        g = "";
    for (f = k; f < b; f += 3) {
        ++h;
        num3 = f >= 0 ? a.substring(f, f + 3) : a.substring(0, k + 3);
        strEng = English(num3);
        if (strEng != "") {
            if (g != "") g += ",";
            g += English(num3) + arr1[e - h]
        }
    }
    return g.toUpperCase()+" ONLY";
}

//数字翻译成英文
function English(a) {
    strRet = "";
    if (a.length == 3 && a.substr(0, 3) != "000") {
        if (a.substr(0, 1) != "0") {
            strRet += arr3[a.substr(0, 1)] + " hundred";
            if (a.substr(1, 2) != "00") strRet += " and "
        }
        a = a.substring(1);
    }
    if (a.length == 2)
        if (a.substr(0, 1) == "0") a = a.substring(1);
        else if (a.substr(0, 1) == "1") strRet += arr4[a.substr(1, 2)];
    else {
        strRet += arr2[a.substr(0, 1)];
        if (a.substr(1, 1) != "0") strRet += "-";
        a = a.substring(1)
    } if (a.length == 1 && a.substr(0, 1) != "0") strRet += arr3[a.substr(0, 1)];
    return strRet;
};

<div>
            选择语言格式：<select id="language" title="语言格式">
                <option value="EN">英文</option>
                <option value="CNY">中文</option>
        </div>

var jsonData = JSON.stringify({
                            "原小写金额": amo,
                            "货币单位": cur,
                            "语言": "",
                            "大写金额": ""
            });