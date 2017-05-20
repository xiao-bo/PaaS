#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h> //Load UDP Library
#include "floatToString.h"
const int analogInPin = A1; 
int sensorValue = 0;
String clock21;
String clock22;
String clock23;
String clockPrefix21;
String clockPrefix22;
String clockPrefix23;
String head;
char str_R[25];
char rece;
float R=1.0;
String disconnectBuffer;
unsigned long tmp[40];
unsigned long time_c21;
unsigned long time_c22;
unsigned long time_c23;
// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
    0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
    
};
// Enter the IP address of the server you're connecting to:
//IPAddress server(192,168,0,103);
IPAddress server(192,168,11,3);
EthernetClient client;

void ethernet_connect(){
    
    // start the Ethernet connection:
    
    
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
// not used R
/*
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
    
    Serial.print("R=========");
    Serial.println(R,10);
    Serial.println("====");
}
*/
void setup() {
   
    // Open serial communications and wait for port to open:
    Serial.begin(9600);
    
    // give the Ethernet shield a second to initialize:
    Ethernet.begin(mac);
    Serial.println(Ethernet.localIP());
    
    // initial global variable
    clockPrefix21=String("C21:");
    clockPrefix22=String("C22:");
    clockPrefix23=String("C23:");
    head=String("head:");
    Ethernet.begin(mac);
    Serial.println(Ethernet.localIP());
    //initial_R();
    
    ethernet_connect();
    
}

void loop() {
    sensorValue = analogRead(analogInPin);
    //Serial.println(sensorValue);
    
    //delay(100);
    
    if(sensorValue>1022){
        time_c21 = micros();
        clock21+=head+"C21:"+time_c21+":V:"+sensorValue;
        //Serial.println(clock21);
        if(client.connected()){
            
            client.print(clock21);
            //Serial.println("send message");
            // initial head and clear memory
            head=String("head:");
            clock21=String("");
            if(client.available()>0){// receive message from master
                rece=client.read();
                Serial.print("rece string:");
                Serial.println(rece);
                time_c22 = micros();
                time_c23 = micros();
                clock22=head+clockPrefix22+time_c22+":";//conta
                clock23=clockPrefix23+time_c23;
                client.print(clock22+clock23);
            }
        }else{
            clock21=clock21+",";
            Serial.println("connected fail, reconnect");
            client.stop();
            ethernet_connect();
            // because disconnect, so head is remove from data
            head=String("");
            
        }
        delay(500);
    } 
}
