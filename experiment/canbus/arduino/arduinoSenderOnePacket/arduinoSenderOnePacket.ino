// demo: CAN-BUS Shield, send data
#include <mcp_can.h>
#include <SPI.h>

// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
const int SPI_CS_PIN = 9;
MCP_CAN CAN(SPI_CS_PIN); // Set CS pin
const int analogInPin = A0;
int sensorValue = 0;

String clock1;
String clock23;
int change = 1023;

// receive variable
char rece;

//counter buffer
byte digital[20];
int dIndex;

//counter 
unsigned long timeC1;
unsigned long timeC2;
unsigned long timeC3;

//packet
unsigned char packet[8] = {};
int pIndex;

//for loop variable
int i;

// for split variable
unsigned long tmp;

int len=0;
String id = "0x02";

void putClockIntoPacket(int sensorValue,long timeC,int id){
    tmp = timeC;
        
    // timeC1 is split into digital(0-9) assigned to digital
    for(i=0;tmp>0;i++){
      digital[i] = tmp%100;
      //Serial.println(digital[dIndex]);
      tmp = tmp/100;
       
    }
    
    //reverse timeC1buffer? or master receive and reverse? (master reverse)
    dIndex = 0;
    
    // just print timeC1 part of digital
    
    while(digital[dIndex]<100){ 
      //Serial.println(digital[dIndex]);
      dIndex++;
    }
    
    dIndex=0;
    while(digital[dIndex]<100){
        packet[dIndex+1] = digital[dIndex];
        // change next message
        dIndex++; 
         
    }
    
    
    /*
    for(i=0;i<8;i++){
       Serial.print(packet[i]);
       Serial.print(" ");
    }
    Serial.println("");
    */
    if (sensorValue<10 and sensorValue>=0){
        packet[0]=100;
        packet[dIndex+1] = 255; 
    }else if(sensorValue>1000){
        packet[0]=101;
        packet[dIndex+1] = 255;
    }else{
        packet[0]=102;
        packet[dIndex+1] = 255;
    }
    
    Serial.print(" analog value ");
    Serial.println(sensorValue);
    CAN.sendMsgBuf(id,0,8,packet);
  
}

void setup()
{
    Serial.begin(115200);

    while (CAN_OK != CAN.begin(CAN_500KBPS))              // init can bus : baudrate = 500k
    {
        Serial.println("CAN BUS Shield init fail");
        Serial.println(" Init CAN BUS Shield again");
        delay(100);
    }
    Serial.println("CAN BUS Shield init ok!");
}


void loop(){
    int masterId = 0;
    int len = sizeof(digital);
    unsigned char reclen = 0;
    unsigned char buf[8];
    // initialize digital is 14 because  
    // timeC1 will be split into digital(0-9)
    // assigned to digital and digital is not used part is 14.
    // digital 14 represents 0e in master
    // digital 13 represents 0d in master
    // digital 12 represents 0c in master
    // digital 11 represents 0b in master
    // digital 10 represents 0a in master
    // digital 09 represents 09 in master

    // initial digital, choose 150 as control variable in putClockIntoPacket.
    for (i=0;i<len-1;i++){
      digital[i] = 150;
      Serial.println(digital[i]);
    }
   
    sensorValue = analogRead(analogInPin);
    
    if(sensorValue != change and (sensorValue == 0 or sensorValue ==1023) ){
      
        timeC1 = micros();  
        Serial.print("timeC1: ");
        Serial.println(timeC1);
        putClockIntoPacket(sensorValue,timeC1,0x03);
        
        //timeC1=1046100012; //maximum length of long vaiable is 10 digital
        
        change = sensorValue;
    }  
     
    // receive data from master
    if(CAN_MSGAVAIL == CAN.checkReceive()){

        CAN.readMsgBuf(&reclen, buf);    // read data,  len: data length, buf: data buf
        Serial.println(timeC2);
        //Serial.println("get message");
        unsigned int canId = CAN.getCanId();
        if (canId == masterId){
            timeC2 = micros();
            Serial.println("master id is gooooooood");
            packet[0]=102;
            putClockIntoPacket(-1,timeC2,0x04);
            Serial.print("timeC2: ");
        }
      
    }
    
    
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
