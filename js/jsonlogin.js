$(document).ready(function() {
  console.log("Ajax triggered!");

  $("#signIn").submit(function(event) {
    event.preventDefault();
   // var $form = $( this ),
    //uname = $form.find( "input[name='username']" ).val(),
    //pname = $form.find( "input[name='password']" ).val(),
    $.ajax(
      {
        url: "cgi-bin/part3.py",
        type: "POST",
        data: {
          username: $("#loginUsername").val(),
          password: $("#loginPassword").val()
        },
        dataType: "json",

        success: function(data) {
          console.dir(data); //sanity check
          console.log($("#loginPassword").val());
          if (data.password == null)
          {
            alert("Incorrect password: Please try again");
          }
          else if (data.username == null)
          {
            alert("You don't seem to be a registered user. Please sign up for an account.");
          }
          else //no errors triggered, so update cookie and redirect to homepage
          {
            //document.cookie = data; //perhaps we can import the jquery cookie library
            $.cookie('user', data.username, {expires: 1}, {path: data.path}); //set cookies to expire in a day
            $.cookie('session_id', data.session_id, {expires: 1}, {path: data.path})
            window.location.href = "http://tnichols.rochestercs.org/homepage.html"; //redirect
          }
        },
        error: function (jqXHR, errorStatus, errorString) {
        console.log(jqXHR);
        console.log(errorStatus);
        console.log(errorString);
        }
      }
    );
  });
});
