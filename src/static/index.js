
var socket = io();
socket.on('connect', function() {
    socket.emit("conn_valid", "connection");
});

socket.on("data", (message) => {
    console.log("Got data! " + message)

    //here you will get all the messages for rendering
    //TODO
})