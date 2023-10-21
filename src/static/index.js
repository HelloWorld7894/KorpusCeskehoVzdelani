function get_data(idx){
    var school1 = document.getElementsByClassName("dropdown searchbar")[0]
    var school2 = document.getElementsByClassName("dropdown searchbar")[1]

    var school1_val = school1.value
    var school2_val = school2.value

    if (school1_val == "Vyberte z následujících" || school2_val == "Vyberte z následujících"){
        
    }
}

var socket = io();
socket.on('connect', function() {
    socket.emit("conn_valid", "connection");
});

socket.on("data", (message) => {
    console.log("Got data! " + message)

    //here you will get all the messages for rendering
    //TODO
})