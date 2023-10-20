
var socket = io();
socket.on('connect', function() {
    socket.emit("conn_valid", "connection");
});

socket.on("data", (message) => {
    console.log("Got a message! " + message)
})