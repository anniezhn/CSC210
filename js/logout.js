$(document).ready(function() {
  console.log("Document is ready!");

  $("#logoutForm").submit(function(event) {
    event.preventDefault();
    console.log("Button clicked!");
    $.removeCookie('user', {path: '/'}); //kill all cookies with jQuery
    $.removeCookie('session_id', {path: '/'});
    console.log("Cookie now:");
    console.log(document.cookie);
    window.location.replace("http://tnichols.rochestercs.org");
  });
});
