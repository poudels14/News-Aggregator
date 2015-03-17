var d=document;
var cE = "createElement";

function addNews(title, descri, site, href, time){
	var news = d[cE]("div");
	news.className = "news";
		var site_circular_logo = d[cE]("div");
		site_circular_logo.className = "site_circular_logo";
		// site_circular_logo.innerHTML = initial;
		news.appendChild(site_circular_logo);

		var news_cont = d[cE]("div");
		news_cont.className="news_cont";
		news.appendChild(news_cont);
			var news_title = d[cE]("div");
			if (title.length > 68) {
				news_title.className = "double_line_title news_title";
			}
			else {
				news_title.className = "single_line_title news_title";
			}
			// news_title.className = "news_title";
			news_title.innerText = title;
			news_cont.appendChild(news_title);

			var news_descri_holder = d[cE]("div");
			news_descri_holder.className = "news_descri_holder";
			news_cont.appendChild(news_descri_holder);
				var news_descri = d[cE]("div");
				news_descri.className = "news_descri";
				news_descri.innerHTML = "\n &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; " + descri;
				news_descri_holder.appendChild(news_descri);

			var news_details_share = d[cE]("div");
			news_details_share.className = "news_details_share";
			// news_details_share.innerHTML = "&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; " + descri;
			news_cont.appendChild(news_details_share);
				var news_details = d[cE]("div");
				news_details.className = "news_details";
				news_details.innerHTML = site + " | Sagar Poudel | " + time;
				news_details_share.appendChild(news_details);
	d.getElementsByClassName("all_news")[0].appendChild(news);
}


jData =  {"descri" : "Even a budget-cutting Congress isn't hurting Washington's standing on Wall Street.", "pubdate" : "Oct 05, 2014  8:00 PM ET", "title" : "Washington Bonds Beat Market as Federal Cuts Defied", "image" : "http://www.bloomberg.com/image/idVN_xycrDsM.jpg", "link" : "http://www.bloomberg.com/news/2014-10-06/washington-bonds-beat-market-as-federal-cuts-defied.html",  "lastmod" : "2014-10-10T00:14:29-04:00" }


function getNews()	{
	var xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function()
  		{
  			if (xmlhttp.readyState==4 && xmlhttp.status==200)
    			{
					jData = JSON.parse(xmlhttp.responseText);
   				}
  		}
		xmlhttp.open("GET","http://localhost:8080/db",true);
		xmlhttp.send();
}	
