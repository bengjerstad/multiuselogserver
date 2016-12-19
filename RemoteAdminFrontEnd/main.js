SERVERIP = '10.24.25.130:8000';

function getconnection(){
	$.getJSON("http://"+SERVERIP+"/logserver/connection", function(result){
		$("#main").html('<ul>');
		$("#stattxt").text('List of connections received.');
		$.each( result, function( key, val ) {
			username = key.split(" ")[0];
			thisview = "connview";
			link = "<a href='#' onclick='view(thisview)'><img class='mediumimg' src='"+val+".jpg'/>"+username+ "</a>"
			$("#main").append("<li>"+link+"</li>");
		});
		$("#main").append("</ul>");
	});
}
function hashlist(){
	$.getJSON("http://"+SERVERIP+"/logserver/hashlist", function(result){
		$("#stattxt").text('List of hash received.');
		$.each( result, function( key, val ) {
			username = key.split(" ")[0];
			thisview = "hashview";
			link = "<a href='#' onclick='view(thisview)'><img class='mediumimg' src='"+val+".jpg'/>"+username+ "</a>"
			$("#main").append("<li>"+link+"</li>");
		});
		$("#main").append("</ul>");
	});
}
function rolluplist(){
	$.getJSON("http://"+SERVERIP+"/logserver/rolluplist", function(result){
		$("#exlist").html("");
		$("#stattxt").text('List of rollups received.');
		$.each( result, function( key, val ) {
			username = key.split(" ")[0];
			link = "<a href='#' >"+username+ "</a>"
			$("#exlist").append("<li>"+link+"</li>");
		});
		$("#exlist").append("</ul>");
	});
}
function view(viewtype){
	$.getJSON("http://"+SERVERIP+"/logserver/"+viewtype+"", function(result){
		$("#logview").html("");
		$("#stattxt").text('Log View received.');
		$.each( result, function( key, val ) {
			username = key.split(" ")[0];
			link = "<a href='#' >"+val+ "</a>"
			$("#logview").append("<li>"+link+"</li>");
		});
		$("#logview").append("</ul>");
	});
}
	

getconnection();
hashlist();
rolluplist();
setInterval(getconnection,3600000);
setInterval(hashlist,3600000);
