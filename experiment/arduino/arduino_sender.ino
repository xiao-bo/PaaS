#include <SPI.h>
#include <Ethernet.h>

const int analogInPin = A0; 
int sensorValue = 0;
int outputValue = 0;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
    0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(10,1,1,7);

// Enter the IP address of the server you're connecting to:
IPAddress server(10, 1, 3, 2);
EthernetClient client;

void ethernet_connect(){
    // start the Ethernet connection:
    Ethernet.begin(mac, ip);
    // Open serial communications and wait for port to open:
    Serial.begin(9600);
    //while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
    //}

    // give the Ethernet shield a second to initialize:
    delay(1000);
    Serial.println("connecting...");

    // if you get a connection, report back via serial:
    if (client.connect(server, 10002)) {
        Serial.print("connected to ");
        Serial.println(server);
    } else {
        Serial.println("connection failed");
    }

}


void setup() {
    ethernet_connect();
}

void loop() {
    sensorValue = analogRead(analogInPin);
    outputValue = map(sensorValue, 0, 1023, 0, 255);

    if (outputValue){
        if (client.connected()){
            Serial.print("sensor value: ");
            Serial.println(sensorValue);
            client.print(sensorValue);  
        }  
    }

    // if the server's disconnected, stop the client:
    if (!client.connected()) {
        Serial.println("disconnecting. retry after 3s");
        client.stop();
        delay(3000);
        ethernet_connect();
    }
    delay(100);
}




