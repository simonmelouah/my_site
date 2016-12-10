$(document).ready(function () {

    $('.hoverCheck').hover( function(){
    var val = $(this).data('id');
    console.log("This is the value: " + val);
    $.ajax({
        type : "POST",
        url : "/software_portfolio",
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
        url : "/software_portfolio",
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
//    if (top.location.pathname === '/software_portfolio'){
//        $('#technology').on('change', function () {
//            var technology_id = $("#technology option:selected").val();
//            var category_id = $("#category option:selected").val();
//            if (category_id != null && technology_id != null){
//            console.log("Technology id: ", technology_id);
//            console.log("Category id: ", category_id);
//            $.ajax({
//                type : "POST",
//                url : "/software_portfolio",
//                contentType: 'application/json;charset=UTF-8',
//                data: JSON.stringify({'technology-id': technology_id, 'category-id': category_id}),
//                dataType: "json",
//                success: function(result) {
//                }
//            });
//            }
//        });
//        $('#category').on('change', function () {
//            var technology_id = $("#technology option:selected").val();
//            var category_id = $("#category option:selected").val();
//            if (category_id != null && technology_id != null){
//            console.log("Technology id: ", technology_id);
//            console.log("Category id: ", category_id);
//            $.ajax({
//                type : "POST",
//                url : "/software_portfolio",
//                contentType: 'application/json;charset=UTF-8',
//                data: JSON.stringify({'technology-id': technology_id, 'category-id': category_id}),
//                dataType: "json",
//                success: function(result) {
//                }
//            });
//            }
//        });
//    }

    if (top.location.pathname === '/about'){
    console.log("Here");
    var elements = document.getElementsByClassName("navbar-a");
    for(var i = 0; i < elements.length; i++) {
        elements[i].style.color = 'black';
    }
    }

});