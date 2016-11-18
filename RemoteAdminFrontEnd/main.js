SERVERIP = '10.24.25.130:8000';
$(document).ready(function(){
    $("#mainnavbutton").click(function(){
        $.getJSON("http://"+SERVERIP+"/logserver/connection", function(result){
			$("#main").html('<ul>');
			$("#stattxt").text('List of duplicate logs received.');
			$.each( result, function( key, val ) {
				username = key.split(" ")[0];
				link = "<a href='#' class='dupitem'>"+username+ "</a>"
				$("#main").append("<li>"+link+"</li>");
			});
			$("#main").append("</ul>");
			$(".dupitem").click(function(){
				username = $(this).text();
				$(".selected").removeClass( "selected" );
				$(this).addClass( "selected" );
				$("#exusername").val(username);
				$("#exnav").removeClass('hidden');
				$.getJSON("http://"+SERVERIP+"/get_log?username="+username+"&compname=all", function(result){
					$("#logview").html("");
					$("#logview").append("<table>");
					$("#stattxt").text('Log for user '+username+' received.');
					$.each( result, function( key, val ) {
					datetime = val.time;
					datetime = datetime.split("_");
					date = datetime[0].split("-");
					date[0] = date[0].substring(1, 5);
					date = date[1]+"/"+date[2]+"/"+date[0];
					timeh = datetime[1].substring(0, 2);
					timem = datetime[1].substring(2, 4);
						$("#logview").append("<tr><td>"+val.username+" </td><td> "+val.compname+" </td><td> "+val.stat+" </td><td> "+timeh+":"+timem+" </td><td> "+date+" </td></tr>");
					});
				});
				
				
			});
        });
    });
});
