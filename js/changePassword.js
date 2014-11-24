$(document).ready(function() {
	$("#changePasswordButton").submit(function(event) {//change ID name
	    event.preventDefault();
	    console.log("Changebutton clicked");
	    console.log($("#oldpassword").val());
	    console.log($("#newpassword").val());
	    console.log($("#confirmpassword").val());
	    $.ajax(
	      {
	        url: "cgi-bin/changePassword.py",
	        type: "POST",
	        data: {
	          oldpass: $("#oldpassword").val(),
	          newpass: $("#newpassword").val(),
	          confirmpass: $("#confirmpassword").val()
	        },
	        dataType: "text",

	        success: function(data) {
	          console.dir(data); //sanity check
	          if (data == "nomatch")
	          {
	            alert("Your confirmation of your new password didn't match. Please try again.");
	          }
	          else if (data == "incorrect")
	          {
	            alert("Your old password is incorrect. Please try again.");
	          }
	          else //no errors triggered, so update cookie and redirect to homepage
	          {
	            alert("Password change successful!");
	            window.location.replace("http://tnichols.rochestercs.org/homepage.html");
	          }
	         },
	        error: function (jqXHR, errorStatus, errorString) {
	       		//console.dir(data); 
			console.log(jqXHR);
	       	 	console.log(errorStatus);
	        	console.log(errorString);
	        }
	    });
	  });
})
