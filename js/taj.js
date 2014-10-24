jQuery(document).ready(function ($) {
    $.ajax({
        url: "http://tnichols.rochestercs.org/cgi-bin/loginCheck.py",
        method: "GET",
        dataType: "text",
        success: function (data) {
            if (data === "True") {
                window.location.href = "http://tnichols.rochestercs.org/homepage.html";
            }
        },
        error: function (jqXHR, errorStatus, errorString) {
            $("body").prepend(
                "<div>" +
                "<ul>" +
                    "<li>Error: " + errorStatus + "</li>" +
                    "<li>Message: " + errorString + "</li>" +
                "</ul>" +
                "</div>" +
                "<div>Something went wrong.</div>"
            );
        }
    });
});
