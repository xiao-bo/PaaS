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
String sensorValuePrefix;
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
IPAddress server(192,168,0,103);
//IPAddress server(192,168,11,3);
EthernetClient client;

void ethernet_connect(){
    
    // start the Ethernet connection:
    Ethernet.begin(mac);
    Serial.println(Ethernet.localIP());
      
    // give the Ethernet shield a second to initialize:
    
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
    // initial global variable
    clockPrefix21=String("C21:");
    clockPrefix22=String("C22:");
    clockPrefix23=String("C23:");
    head=String("head:");
    sensorValuePrefix=String("Value:");
    Ethernet.begin(mac);
    Serial.println(Ethernet.localIP());
    //initial_R();
    ethernet_connect();
    //disconnectBuffer=String("sensorValue");
}

void loop() {
    sensorValue = analogRead(analogInPin);
    Serial.println(sensorValue);
    
    //delay(100);
    
    if(sensorValue>1012){
        time_c21 = micros();
        clock21+=head+clockPrefix21+time_c21+":"+sensorValuePrefix+sensorValue;
        Serial.println(clock21);
        if(client.connected()){
            client.print(clock21);
            Serial.println("send message");
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

    /*
            if (client.available() > 0) {// receive message from server       
                rece=client.read();
                Serial.print("receive message from server:");
                Serial.println(rece);
                clock21=String("");
                time_c22 = micros();
                
                time_c23 = micros();
                clock22=clockPrefix22+time_c22;//conta
                clock23=clockPrefix23+time_c23;
                client.print(clock22+clock23);
                
                // echo the bytes to the server as well:
                Serial.println(clock22);
                Serial.println(clock23);
            }
            */
            
    /*
    // if the server's disconnected, stop the client:
    if(!client.connected()) {
        Serial.println("disconnecting. retry after 3s");
        R=1.0;
        client.stop();
        
        if(sensorValue >1022){
            time_c21 = micros();
            clock21=sensorValue+clockPrefix21+time_c21+",";
            disconnectBuffer+=clock21;
            Serial.println(disconnectBuffer);
            delay(500);
        }
        ethernet_connect();
    }
    else if(client.connected()){ 
        if(R!=2.0){
            client.print(str_R);
            R=2.0;
            client.print(disconnectBuffer);
            disconnectBuffer=String("");
            //clear (memory)
        }
        
        if (sensorValue>1022 ){//or sensorValue<10){
            senseData();
            delay(500);
        }
    }
    */
}
void senseData(){
    time_c21 = micros();
                      
    ///send message
    clock21=sensorValue+clockPrefix21+time_c21;
    //Serial.print(sensorValue);
    //Serial.println(clock21);
    client.print(clock21);
 
    if (client.available() > 0) {// receive message from server       
        rece=client.read();
        Serial.print("receive message from server:");
        Serial.println(rece);
        time_c22 = micros();
        
        time_c23 = micros();
        clock22=clockPrefix22+time_c22;//conta
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
    
}

