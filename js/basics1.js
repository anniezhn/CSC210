 jQuery(document).ready(function($) {
	  console.log("Test");
 //I found this click once function online but it's not working.
//	  $("#getStringDef").one('click', function() {
//	        $.ajax({
//	           url: "cgi-bin/basics1.py",
//	           type: "GET",
//	           dataType: "text",
//	           success: function(dat) {
//	             console.log(dat);
//	             $("#string").append('<li>' + dat + '</li>');
//	           },
//	        });
//	      });

    $("#getStringDef").click(function() {
    $.ajax(
      {
        url: "../cgi-bin/basics1.py",
        type: "GET",
        dataType: "text",

        success: function(dat) {
          console.dir(dat);
          $("#string").append(dat);
        },
      }
    );
  });
});
