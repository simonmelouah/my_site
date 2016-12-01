$(document).ready(function () {

    $('.hoverCheck').hover( function(){
    console.log("Here");
    var val = $(this).data('id');
    console.log("This is the value: " + val);
    $.ajax({
        type : "POST",
        url : "/projects",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'data-hover': val}),
        dataType: "json",
        success: function(result) {
            console.log(result);
        }
    });
    });

    $('.gitRepo').click( function(){
    console.log("Here");
    var val = $(this).data('id');
    console.log("This is the href git value: " + val);
    $.ajax({
        type : "POST",
        url : "/projects",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'data-click-git': val}),
        dataType: "json",
        success: function(result) {
            console.log(result);
        }
    });
    });

    $('.youtube').click( function(){
    console.log("Here");
    var val = $(this).data('id');
    console.log("This is the href youtube value: " + val);
    $.ajax({
        type : "POST",
        url : "/projects",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'data-click-youtube': val}),
        dataType: "json",
        success: function(result) {
            console.log(result);
        }
    });
    });

    var start_technology = $('#technology').val();
    console.log(start_technology);
    if (start_technology == "other") {
      document.getElementById('newTech').style.display = "block";
      document.getElementById('image').style.display = "block";
    }
    else{
        document.getElementById('newTech').style.display = "none";
        document.getElementById('image').style.display = "none";
    }
    $('#technology').on('change', function () {
        var technology = $(this).val();
        if (technology == "other") {
            console.log("other");
            document.getElementById('newTech').style.display = "block";
            document.getElementById('image').style.display = "block";
        }
        else if (technology != "other"){
            document.getElementById('newTech').style.display = "none";
            document.getElementById('image').style.display = "none";

        }
    });

});