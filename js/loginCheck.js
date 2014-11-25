(function () {
    jQuery.ajax({
        url: "cgi-bin/loginCheck.py",
        method: "GET",
        async: false,
        dataType: "text",
        success: function (data) {
            if (data !== "") {
                window.location.href = data;
            }
        },
        error: function (jqXHR, errorStatus, errorString) {
            console.log(jqXHR);
            console.log(errorStatus);
            console.log(errorString);
        }
    });
}());
jQuery(document).ready(function ($) {
    $("#loginUsername").focus();
});
