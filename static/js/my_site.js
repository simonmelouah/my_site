$(document).ready(function () {

    $('.hoverCheck').hover( function(){
    console.log("Here");
    var val = $(this).data('id');
    console.log("This is the value: " + val);
    $.ajax({
        type : "POST",
        url : "/software_portfolio",
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
        url : "/software_portfolio",
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
        url : "/software_portfolio",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'data-click-youtube': val}),
        dataType: "json",
        success: function(result) {
            console.log(result);
        }
    });
    });

    $('.editProject').click(function(){

       console.log("Pressed");
       var id = $(this).val();
       window.location.href="/add_project?id=" + id;

    });

    if (top.location.pathname === '/add_project'){
        var start_technology = $("#technology option:selected").text();
        console.log(start_technology);
        if (start_technology == "Other") {
          document.getElementById('newTech').style.display = "block";
          document.getElementById('image').style.display = "block";
        }
        else{
            document.getElementById('newTech').style.display = "none";
            document.getElementById('image').style.display = "none";
        }
        $('#technology').on('change', function () {
            var technology = $("#technology option:selected").text();
            console.log(technology);
            if (technology == "Other") {
                console.log("Other");
                document.getElementById('newTech').style.display = "block";
                document.getElementById('image').style.display = "block";
            }
            else if (technology != "Other"){
                document.getElementById('newTech').style.display = "none";
                document.getElementById('image').style.display = "none";

            }
        });
    }

});