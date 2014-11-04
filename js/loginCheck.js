(function () {
    jQuery.ajax({
        url: "http://tnichols.rochestercs.org/cgi-bin/loginCheck.py",
        method: "GET",
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
