jQuery(document).ready(function ($) {
    $.ajax({
        url: "http://tnichols.rochestercs.org/cgi-bin/loginCheck.py",
        method: "GET",
        dataType: "text",
        success: function (data) {
            console.log(data);
        },
        error: function (jqXHR, errorStatus, errorString) {
            console.log(jqXHR);
            console.log(errorStatus);
            console.log(errorString);
        }
    });
});
