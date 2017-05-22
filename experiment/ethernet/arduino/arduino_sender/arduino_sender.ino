#include <SPI.h>
#include <Ethernet.h>

//#include <EthernetUdp.h> //Load UDP Library
//#include "floatToString.h" //for R

//pin 
const int analogInPin = A2; 
int sensorValue = 0;

String clock21;
String clock2223;
String head;

// for initial R
/*
float R=1.0;
char str_R[25];
unsigned long tmp[40];
*/

// receive variable
char rece;

// counter
unsigned long time_c21;
unsigned long time_c22;
unsigned long time_c23;

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
    0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
    
};
// Enter the IP address of the server you're connecting to:
//IPAddress server(192,168,0,102);
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
    //Serial.println("????");
    Ethernet.begin(mac);
    Serial.println(Ethernet.localIP());
    // initial global variable
    head=String("head:");
    //initial_R();
    ethernet_connect();
    
}
/*
void loop() {
    sensorValue = analogRead(analogInPin);
    Serial.println(sensorValue);
    //delay(5);
    
    if(sensorValue>0 ){
        time_c21 = micros();
        //clock21+=head+"C21:"+time_c21+":V:"+sensorValue;
        clock21=head+"C21:"+time_c21+":V:"+sensorValue;
        Serial.println(clock21);
        
        if(client.connected()){
            delay(10);
            if(client.available()>0){
                client.print(clock21);
                Serial.println("send success???");
            }else{
                Serial.println("no ack , connection fail");
            }
        }else{
            Serial.println("no connection");  
            ethernet_connect();

        }
            
        delay(400);     
    } 
    
}
*/

void loop() {
    sensorValue = analogRead(analogInPin);
    //Serial.println(sensorValue);
    //delay(5);
    
    if(sensorValue>1020 or sensorValue<10){
        Serial.println(sensorValue);
        time_c21 = micros();
        clock21+=head+"C21:"+time_c21+":V:"+sensorValue;
        //Serial.println(clock21);
        
        if(client.connected()){
            client.print(clock21);
            Serial.print("send message ");
            //Serial.println(clock21);
            // initial head and clear memory
            head = String("head:");
            clock21 = String("");
            delay(10); // it not fast to receive message from master
            if(client.available()>0){// receive message from master
                rece = client.read();
                Serial.print("rece string:");
                Serial.println(rece);
                time_c22 = micros();
                time_c23 = micros();
                clock2223 = head+"C22:"+time_c22+":C23:"+time_c23;//message
                
                client.print(clock2223);
            }
        }else{
            clock21=clock21+",";
            Serial.println("connected fail, reconnect");
            client.stop();
            ethernet_connect();
            
            // because disconnect, so head is remove from data
            head=String("");
            
        }
        delay(480);
    } 
    
}
/*
*/
