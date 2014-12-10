$(document).ready(function() {
	$("#runProgram").submit(function(event) {
		event.preventDefault();
	    console.log("Button clicked!");
	    var val1 = $("#start").val();
	    var val2 = $("#end").val();
	    var val3 = $("#jump").val();
	    var toPrint = $("#print").val().replace(/</g, "&lt;").replace(/>/g, "&gt;");
	    var start = parseInt(val1, 10);
	    var end = parseInt(val2, 10);
	    var increment = parseInt(val3, 10);
	    //var result = "<p>" + val1 + " " + val2 + " " + val3 + "</p>";
	    var result = "";
	    console.log("Val1: " + val1);
	    console.log("Val2: " + val2);
	    console.log("Val3: " + val3);
	    //make sure user entered actual integers. Kids these days...
	    if (val1 == start && val2 == end && val3 == increment)
	    {
           	//$("#programOutput").html(result);
           	if ((end - start)/increment > 100) //kid wants to see what infinity looks like. Let's not
           		$("#programOutput").html("<p>...Let's NOT explode the page by printing more than 100 times.</p>");
           	else if (end - start < 1) //won't print in this case
           		$("#programOutput").html("<p>Check your first two values and think about the conditional you're producing.</p><p>Do you see why nothing will print?</p>");
           	else //we're good, actually print the results
           	{
           		for(var i = start; i < end; i += increment)
           			result += "<p><pre>" + toPrint + "                 i is currently " + i + " </pre></p>";
           		$("#programOutput").html(result);
           	}
	    }
	    else 
	    {
	    	console.log("Not integers?");
	    	console.log(val1 === parseInt(val1, 10));
	    	console.log(val2 === parseInt(val2, 10));
	    	console.log(val3 === parseInt(val3, 10));

	    	$("#programOutput").html("<p>All your inputs must be integers!</p>");
	    }

		/*console.log(val1);
		console.log(val2);
		console.log(val3);*/
	})
})
