$(document).ready(function () {

    $(document).mousemove(function(event){
        console.log(event.pageX + ", " + event.pageY);
    });

//    function getMousePosition(timeoutMilliSeconds) {
//        $(document).one("mousemove", function (event) {
//            window.xPos = event.pageX;
//            window.yPos = event.pageY;
//            setTimeout("getMousePosition(" + timeoutMilliSeconds + ")", timeoutMilliSeconds);
//            console.log("Mouse postion x and y: " + window.xPos + " " + window.yPos)
//        });
//    }
//
//    getMousePosition(100);
    $('.hoverCheck').hover( function(){
    var val = $(this).data('id');
    console.log("This is the value: " + val);
    $.ajax({
        type : "POST",
        url : "/software-portfolio",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'data-hover': val}),
        dataType: "json",
        success: function(result) {
        }
    });
    });

    $('.gitRepo').click( function(){
    var val = $(this).data('id');
    console.log("This is the href git value: " + val);
    $.ajax({
        type : "POST",
        url : "/software-portfolio",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'data-click-git': val}),
        dataType: "json",
        success: function(result) {
        }
    });
    });

    $('.youtube').click( function(){
    var val = $(this).data('id');
    console.log("This is the href youtube value: " + val);
    $.ajax({
        type : "POST",
        url : "/software-portfolio",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({'data-click-youtube': val}),
        dataType: "json",
        success: function(result) {
            console.log(result);
        }
    });
    });

    $('.editProject').click(function(){
       var id = $(this).val();
       window.location.href="/add_project?id=" + id;

    });

    if (top.location.pathname === '/add_project'){
        var start_technology = $("#technology option:selected").text();
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
    if (top.location.pathname === '/software-portfolio'){
        $(".category").hide();
        $('#category').on('change', function () {
            var category = $("#category option:selected").text();
            if (category != "Select a category..."){
            console.log("Category: ", category);
            $(".category").hide();
            $(".category[data-category="+category+"]").show();
            }
            else{
            $(".category").hide();
            }
        });
        }

    if (top.location.pathname === '/about' || top.location.pathname === '/contact'){
    console.log("Here");
    var elements = document.getElementsByClassName("navbar-a");
    for(var i = 0; i < elements.length; i++) {
        elements[i].style.color = 'black';
    }
    }



});
