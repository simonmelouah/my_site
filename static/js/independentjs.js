$(document).ready(function () {
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
