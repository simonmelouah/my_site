// Declare
var position_x, position_y, window_width, window_height;
document.onmousemove = function(e) {
    position_x = e.clientX;
    position_y = e.clientY;
    window_width = window.innerWidth;
    window_height = window.innerHeight;
    }
setInterval(function() {
    $.ajax({
    type : "POST",
    url : "/mouse_recording",
    contentType: 'application/json;charset=UTF-8',
    data: JSON.stringify({'data-event_type': "move", 'data-window_width': window_width, 'data-window_height': window_height, 'data-x_position': position_x, 'data-y_position': position_y}),
    dataType: "json",
    success: function(result) {
    }
    });
    }, 500);

document.onclick = function(e) {
    position_x = e.clientX;
    position_y = e.clientY;
    window_width = window.innerWidth;
    window_height = window.innerHeight;
    $.ajax({
    type : "POST",
    url : "/mouse_recording",
    contentType: 'application/json;charset=UTF-8',
    data: JSON.stringify({'data-event_type': "click", 'data-window_width': window_width, 'data-window_height': window_height, 'data-x_position': position_x, 'data-y_position': position_y}),
    dataType: "json",
    success: function(result) {
    }
    });
    }