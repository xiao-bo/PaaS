#include <SPI.h>
#include <Ethernet.h>

const int analogInPin = A0; 
int sensorValue = 0;
int outputValue = 0;
//char packetBuffer[UDP_TX_PACKET_MAX_SIZE];


// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:  


byte mac[] = {
    0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(10,8,0,37);

unsigned long time;           
// Enter the IP address of the server you're connecting to:
IPAddress server(10, 8, 0, 9);
EthernetClient client;

void ethernet_connect(){
    // start the Ethernet connection:
    Ethernet.begin(mac, ip);
    // Open serial communications and wait for port to open:
    Serial.begin(115200);
  

    // give the Ethernet shield a second to initialize:
    delay(1000);
    Serial.println("connecting...");

    // if you get a connection, report back via serial:
    if (client.connect(server, 10005)) {
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
    
    if (client.connected()){
      
        if (sensorValue==1023){
          time=micros();
        Serial.print("sensor value: ");
        Serial.println(sensorValue);
        client.print(time);  
        delay(500);
        }
      
      //delay(0.1);
    }  
    
    // if the server's disconnected, stop the client:
    if (!client.connected()) {
        Serial.println("disconnecting. retry after 3s");
        client.stop();
        delay(3000);
        ethernet_connect();
    }
   
}




