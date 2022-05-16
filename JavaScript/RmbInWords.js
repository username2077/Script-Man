function rmbInWords(num) {
	const objNumber = {
		0: "零", 1: "壹", 2: "贰", 3: "叁", 4: "肆", 5: "伍", 6: "陆", 7: "柒", 8: "捌", 9: "玖",
	};
	const arrInner = ["", "拾", "佰", "仟"];
	const arrOuter = ["", "万", "亿", "兆", "京"];
	const arrWhenWithoutZero = arrOuter.concat(["元", "零"]);
	const arrSplitedNumber = String(Math.round(num * 100) / 100).split(".").map(x=>x.split(""));
	const [aboveZero, belowZero] = arrSplitedNumber.length === 2? arrSplitedNumber: [arrSplitedNumber[0], []];
	
	function numberAboveZero(remainedArr, currStr, outerIdx, innerIdx) {
		if (remainedArr.length === 0) {
			return "人民币" + currStr;
		}
		if (innerIdx >= arrInner.length) {
			innerIdx = 0;
			outerIdx += 1;
		}
		const lastChar = currStr.charAt(0);
		var currChar = objNumber[remainedArr.slice(-1)];
		remainedArr.pop();
		if ((arrWhenWithoutZero.includes(lastChar) || innerIdx === 0) && currChar === "零") {
			currChar = "";
		}
		if (currChar !== "" && currChar !== "零") {
			currChar += arrInner[innerIdx];
		}
		if (innerIdx === 0) {
			currChar += arrOuter[outerIdx];
		}
		return numberAboveZero(remainedArr, currChar + currStr, outerIdx, innerIdx + 1);
	}
	
	function numberBelowZero(arrBelow) {
		switch (arrBelow.length) {
			case 0:
				return "整";
			case 1:
				return `${objNumber[arrBelow[0]]}角整`;
			case 2:
				const [xtyCents, cent] = arrBelow.map(x=>objNumber[x]);
				return `${xtyCents}${xtyCents === "零"? "" : "角"}${cent}分`;
		}
	}
	
	return numberAboveZero(aboveZero, "元", 0, 0) + numberBelowZero(belowZero);
}