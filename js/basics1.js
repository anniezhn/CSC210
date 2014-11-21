$(document).ready(function($) {
$("#getStringDef").on('click', function() {
    $(".definition").html('<img src="images/loading.gif" />');
    $.ajax({
       url: "cgi-bin/basics1/basics1-string.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getCharDef").on('click', function() {
    $(".definition").html('<img src="images/loading.gif" />');
    $.ajax({
       url: "cgi-bin/basics1/basics1-char.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getIntDef").on('click', function() {
    $(".definition").html('<img src="images/loading.gif" />');
    $.ajax({
       url: "cgi-bin/basics1/basics1-int.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getFloatDef").on('click', function() {
    $(".definition").html('<img src="images/loading.gif" />');
    $.ajax({
       url: "cgi-bin/basics1/basics1-float.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getBoolDef").on('click', function() {
    $(".definition").html('<img src="images/loading.gif" />');
    $.ajax({
       url: "cgi-bin/basics1/basics1-bool.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getArrayDef").on('click', function() {
    $(".definition").html('<img src="images/loading.gif" />');
    $.ajax({
       url: "cgi-bin/basics1/basics1-array.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
});
