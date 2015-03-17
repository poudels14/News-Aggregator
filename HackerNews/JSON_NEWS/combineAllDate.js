var fs = require("fs");

var date = "Oct_7";



allNews = [];
allHref = [];
allNewsText = "";
totNews = 0;
var news = {};



totPage = 8;
for (var i = 4; i < totPage; i++){
	var content;
	fs.readFile("./NewsFromOct_"+i+".js", function read(err, data) {
    	if (err) {
        	throw err;
    	}
    	content = data.toString();
    
    	// console.log(content);  
    	x = JSON.parse(content);

    	for (var i = 0; i < x.length; i++){
    		// news.push(x[i]);
    		var found = false;
    		for (var k = 0; k < allHref.length; k++){
				if (x[i]["href"] == allHref[k]) {
					totNews = totNews + 1;
					// console.log("Already found");
					// console.log("num = " + totNews);
					found = true
					break;
				}
			}

			if (found){
			}
			else {
				totNews = totNews + 1;
				allHref.push(x[i]["href"]);
				var data = JSON.stringify(x[i]) + ",\n";
				allNewsText = allNewsText + data;
			}
    	}
	});
}

setTimeout(function(){
	console.log("total news = " + totNews);

	console.log(totNews );
	console.log("Allnews news num = " + allHref.length)
	fs.writeFile("TotalNewsTilDate.js", allNewsText , function(err) {
	    if(err) {
     	   console.log(err);
    	} else {
    	    console.log("The file was saved!");
    	}
	}); 
},2000);

// for (var i = 0; i < news.length; i++){
// 	console.log(n.length);
// 	totNews = totNews + news.length;
// 	for (var j = 0; j < n.length; j++){
// 		// console.log(n[j]);
// 		for (var k = 0; k < allHref.length; k++){

// 			// console.log(n[j]["href"]);
// 			if (news[j]["href"] == allHref[k]) {
// 				console.log("Already found");
// 				break;
// 			}
// 		}
// 		allHref.push(news[j]["href"]);
// 		var data = JSON.stringify(news[j]) + ",\n";
// 		allNewsText = allNewsText + data;
// 		// allNews = JSON.parse(data);
// 		// allNews.push(n[j]);
// 	}
// }


// console.log(totNews );
// console.log("Allnews news num = " + allHref.length)
// fs.writeFile("TotalNewsTilDate.js", allNewsText , function(err) {
//     if(err) {
//         console.log(err);
//     } else {
//         console.log("The file was saved!");
//     }
// }); 