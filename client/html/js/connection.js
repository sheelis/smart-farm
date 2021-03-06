host = "127.0.0.1";
port = 9001;
client = new Paho.MQTT.Client(host, port, "JavaMan");

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({onSuccess:onConnect});

// called when the client connects
function onConnect() {
// Once a connection has been made, make a subscription and send a message.
    console.log("onConnect");
    client.subscribe("house/bulb1");
    message = new Paho.MQTT.Message("Hello");
    message.destinationName = "house/bulb1";
    client.send(message);
}
// called when the client loses its connection
function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        console.log("onConnectionLost:"+responseObject.errorMessage);
    }
}

    // called when a message arrives
function onMessageArrived(message) {
    console.log("onMessageArrived:"+message.payloadString);
}