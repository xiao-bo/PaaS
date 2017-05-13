#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h> //Load UDP Library
#include "floatToString.h"
const int analogInPin = A1; 
int sensorValue = 0;
int outputValue = 0;
String clock21;
String clock22;
String clock23;
String clockPrefix21;
String clockPrefix22;
String clockPrefix23;
char str_R[25];
char rece;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];  //buffer to hold incoming packet,
char  ReplyBuffer[] = "acknowledged";       // a string to send back
float R=2.0;
unsigned long tmp[40];
// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;
unsigned long time_c21;
unsigned long time_c22;
unsigned long time_c23;
// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
    0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
    
};


//IPAddress ip(192,168,11,10);
// Enter the IP address of the server you're connecting to:

IPAddress server(192,168,11,3);
//IPAddress server(192,168,11,8);
EthernetClient client;

void ethernet_connect(){
    clockPrefix21=String(" counterC21:");
    clockPrefix22=String(" counterC22:");
    clockPrefix23=String(" :counterC23:");
    // start the Ethernet connection:
    Ethernet.begin(mac);
    Serial.println(Ethernet.localIP());
      
    // give the Ethernet shield a second to initialize:
    initial_R();
    delay(2000);
    Serial.println("connecting...");
    //Udp.begin(10005);
    // if you get a connection, report back via serial:
    
    if (client.connect(server, 10005)) {
        Serial.print("connected to ");
        Serial.println(server);
        
    } else {
        Serial.println("connection failed");
    }
    
} 
void initial_R(){
    //initially find to R
    int i=0;
    float small;
    Serial.println("initial R...");
    for(;i<sizeof(tmp)/4;i++){
       tmp[i]=micros();
       delay(100);
    }
     
    //find smallest R
    for(i=0;i<sizeof(tmp)/4;i++){
        small=(tmp[i+1]-tmp[i])/(100000.0);
        //Serial.print(tmp[i+1]-tmp[i]);
        //Serial.println(small,10);
        //delay(100);
        if (small<R){
          R=small;
        }
    }
    floatToString(str_R,R,10);
    Serial.print("str_R");
    Serial.println(str_R);
    
    //debug message
    /*
    for(i=0;i<sizeof(tmp);i++){
      Serial.println(tmp[i],10);
    }
    for(i=0;i<sizeof(tmp)-1;i++){
      Serial.println(tmp[i+1]-tmp[i]);
    }
    */
    Serial.print("R=========");
    Serial.println(R,10);
    Serial.println("====");
}

void setup() {
   
     // Open serial communications and wait for port to open:
    Serial.begin(9600);
    
    ethernet_connect();
    
}

void loop() {
    sensorValue = analogRead(analogInPin);
    // if the server's disconnected, stop the client:
    if(!client.connected()) {
        Serial.println("disconnecting. retry after 3s");
        client.stop();
        delay(3000);
        ethernet_connect();
    }  
    else if(client.connected()){ 
        if (sensorValue==1023){
            time_c21 = micros();
            if(R!=2.0){
                client.print(str_R);
                R=2.0;
            }          
            ///send message
            clock21=clockPrefix21+time_c21;
            Serial.println(clock21);
            client.print(clock21);
         
			      if (client.available() > 0) {// receive message from server				
                rece=client.read();
                Serial.print("receive message from serverreceive message from server:");
                Serial.println(rece);
				        time_c22 = micros();
                
				        time_c23 = micros();
				        clock22=clockPrefix22+time_c22;
				        clock23=clockPrefix23+time_c23;
				        client.print(clock22+clock23);
                
				        // echo the bytes to the server as well:
                Serial.println(clock22);
                Serial.println(clock23);
			      }else{
			          Serial.println("do not receive message");
                time_c22 = micros();
                Serial.print("if_c22:");
                Serial.println(time_c22);
			      }
            delay(500);
        }
    }     
}



