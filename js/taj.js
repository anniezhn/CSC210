jQuery(document).ready(function ($) {
    $.ajax({
        url: "http://tnichols.rochestercs.org/cgi-bin/loginCheck.py",
        method: "GET",
        dataType: "text",
        success: function () {}
    });
});
