var d=document;
var cE = "createElement";
var lastId = 10000000;
var ajax = true;
// var ip = "http://165.123.193.114:8080/";
var ip = "http://localhost:8080/";
var date = new Date();
var day = date.getDate();
var month = date.getMonth() + 1;
var ajaxSite = "theverge.com";

function addNews(title, date, image, descri, link, id){
	logo = ip + ajaxSite + "_logo.png";
	if (image == "none"){
		image = "/"+ ajaxSite + "_img_notfound.png";
	}
	var news = d[cE]("div");
	news.className = "news";
	news.id="news_no_" + id;
	news.setAttribute("data-title", title);
	news.setAttribute("data-domain", ajaxSite);
	news.setAttribute("onclick",'gotoNews(this, \''+ id +'\')');

		var news_cont = d[cE]("div");
		news_cont.className="news_cont";
		news.appendChild(news_cont);

			var site_square_logo = d[cE]("div");
			site_square_logo.className = "site_square_logo";
			news_cont.appendChild(site_square_logo);

				var site_logo = d[cE]("img");
				site_logo.src = logo;
				site_logo.height = "50";
				site_logo.width = "50";
				site_square_logo.appendChild(site_logo);

			var news_title = d[cE]("div");
			news_title.className = "news_title";
			news_title.innerHTML = '<div style="line-height:30px;height:30px;overflow:hidden;">' + title + '</div><div style="font-size:12px;line-height:15px;">' + date + '</div>';
			news_cont.appendChild(news_title);

			var descri_img = d[cE]("div");
			descri_img.setAttribute("style","float:left;width:500px;");
			descri_img.innerHTML = '<div class="news_img" style="overflow:hidden;"> <img style="" src="' + image + '" height="100%" width="100%"> </div><div class="news_descri_holder" style=""><div class="news_descri" style="">' + descri + '</div></div>';
			news_cont.appendChild(descri_img);

		var clear = d[cE]("div");
		clear.setAttribute("style","clear:both;");
		news.appendChild(clear);

	d.getElementsByClassName("all_news")[0].appendChild(news);
}


jData =  {"descri" : "Even a budget-cutting Congress isn't hurting Washington's standing on Wall Street.", "pubdate" : "Oct 05, 2014  8:00 PM ET", "title" : "Washington Bonds Beat Market as Federal Cuts Defied", "image" : "http://www.bloomberg.com/image/idVN_xycrDsM.jpg", "link" : "http://www.bloomberg.com/news/2014-10-06/washington-bonds-beat-market-as-federal-cuts-defied.html",  "lastmod" : "2014-10-10T00:14:29-04:00" }


function getNews()	{
	ajax = false;
	var xmlhttp=new XMLHttpRequest();
	if (month < 0){
		return;
	}
	xmlhttp.onreadystatechange=function()
  		{
  			if (xmlhttp.readyState==4 && xmlhttp.status==200)
    			{
    				// console.log(JSON.stringify(xmlhttp.responseText));
					jData = JSON.parse(xmlhttp.responseText);
					JsonToNews(jData);
					if (jData.length > 0) {
						lastId = jData[jData.length - 1]["id"];
						console.log("lastId = " + lastId);
						ajax = true;
					}
					else {
						lastId = 10000000;
						ajax = true;
						day = day - 1;
						if (day < 1){
							day = 31;
							month = month - 1;
						}
						getNews();
					}
   				}
  		}
  		var tmpSite = "db?site=" + ajaxSite + "&lastId=" + lastId + "&day=" + day + "&month=" + month;
  		console.log("site req = " + tmpSite);
		xmlhttp.open("GET",tmpSite , true);
		xmlhttp.send();
}	

function JsonToNews(json){
	for(var i = 0; i < json.length; i++){
		addNews(json[i]["title"], json[i]["date"], json[i]["image"], json[i]["descri"], json[i]["link"], json[i]["id"]);
	}
}

function loadNewSite(){
	lastId = 10000000;
	date = new Date();
	day = date.getDate();
	month = date.getMonth() + 1;
	d.getElementsByClassName("all_news")[0].innerHTML="";
	getNews();
}

function gotoNews(thisNews, id){
	window.open("http://localhost:8080/goto?id=" + id);
	//make ajax call to server:/visited_link=#id; // use cookie to keep track who read what
	// logo = ip + ajaxSite + "_logo.png";

	setTimeout(function(){
		var title = thisNews.dataset.title;
		var domain = thisNews.dataset.domain;
		var logo = ip + domain + "_logo.png";

		var major = d[cE]("div");
		major.className = "major";
		major.id="history_id_" + id;
		major.setAttribute("data-title", title);
		major.setAttribute("data-domain", domain);
		major.setAttribute("onclick","window.open('http://localhost:8080/goto?id="+ id +"\')");

			var img_holder = d[cE]("div");
			img_holder.className="img_holder";
			major.appendChild(img_holder);
					var site_logo = d[cE]("img");
					site_logo.src = logo;
					// site_logo.height = "70";
					// site_logo.width = "70";
					img_holder.appendChild(site_logo);

			var title_holder = d[cE]("div");
			title_holder.className = "title_holder";
			title_holder.innerHTML = "<div>" + title + "</div>";
			major.appendChild(title_holder);

			var share_holder = d[cE]("div");
			share_holder.className = "share_holder";
			share_holder.innerHTML = '<div class="logo_holder"> <img src="share_icon.png" height="30px" width="30px" ></div><input type="text" placeholder="Share/Comment" class="comment_box">';
			major.appendChild(share_holder);
		$(".major").removeClass("major").addClass("minor");
		$("#history_holder").prepend(major);
		$(thisNews).remove();
	},1000);
}
