var fs = require("fs");


var date = "Oct_7";

totPage = 33;
for (var i = 1; i < totPage; i++){
	require("./" + date + "/page"+i+".js");
}

// totPage = 8;
// for (var i = 4; i < totPage; i++){
// 	require("./NewsFromOct_"+i+".js");
// }


allNews = [];
allHref = [];
allNewsText = "";
totNews = 0;
// var n = {};

for (var i = 1; i < totPage; i++){
	var n = eval("news" + i)
	// var n = eval("news_oct_" + i)
	// console.log(n.length);
	totNews = totNews + n.length;
	for (var j = 0; j < n.length; j++){
		// console.log(n[j]);
		for (var k = 0; k < allHref.length; k++){

			// console.log(n[j]["href"]);
			if (n[j]["href"] == allHref[k]) {
				console.log("Already found");
				break;
			}
		}
		allHref.push(n[j]["href"]);
		var data = JSON.stringify(n[j]) + ",\n";
		allNewsText = allNewsText + data;
		// allNews = JSON.parse(data);
		// allNews.push(n[j]);
	}
}


console.log(totNews );
console.log("Allnews news num = " + allHref.length)
// fs.writeFile("TotalNewsTilDate.js", allNewsText , function(err) {
fs.writeFile("NewsFrom"+date+".js", allNewsText , function(err) {
    if(err) {
        console.log(err);
    } else {
        console.log("The file was saved!");
    }
}); 