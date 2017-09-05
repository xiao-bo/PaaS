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
unsigned char packet[8] = {14, 58, 2, 3, 4, 5, 6,9};
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
      digital[i] = tmp%10;
      //digital = tmp%10;
      //Serial.println(digital[dIndex]);
      tmp = tmp/10;
       
    }
    
    //reverse timeC1buffer? or master receive and reverse? (master reverse)
    dIndex = 0;
    
    // just print timeC1 part of digital
    
    while(digital[dIndex]<10){ 
      //Serial.println(digital[dIndex]);
      dIndex++;
    }
    
    dIndex=0;
    pIndex=1;
    while(digital[dIndex]<10){
        packet[pIndex] = digital[dIndex];
        // change next message
        
        dIndex++; 
        pIndex++; 
        // because payload is too long, so send packet first and reassign digital to packet
        if (pIndex >7){ 
            CAN.sendMsgBuf(0x02,0,8,packet);
            Serial.print("one packet: ");
            for(i=0;i<8;i++){
                Serial.print(packet[i]);
                Serial.print(" ");
            }      
            pIndex = 0;
        }
    }
    if (sensorValue>=1000){
        packet[pIndex]=13; 
    }else if(sensorValue<10 and sensorValue>=0){
        packet[pIndex]=12;
    }else if(sensorValue<0){ 
        // represent time2 packet
        packet[pIndex]=14;      
    }
    
    Serial.print("\n analog value ");
    Serial.println(sensorValue);
    Serial.print("second packet: ");
    for(i=0;i<8;i++){
       Serial.print(packet[i]);
       Serial.print(" ");
    }  
    
    Serial.println("");
   
    // send data:  id = 0x00, standrad frame, data len = 8, stmp: data buf
    CAN.sendMsgBuf(id, 0, 8, packet);
    delay(10);// send data per 100ms
  
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
    
    int len = sizeof(digital);
    unsigned char reclen = 0;
    unsigned char buf[8];
    // initialize digital is 14 because  
    // timeC1 will be split into digital(0-9)
    // assigned to digital and digital is not used part is 14.
    // digital 14 represents 0e in master
    // digital 13 represents 0d in master
    // digital 12 represents 0c in master
    for (i=0;i<len-1;i++){
      digital[i] = 15; 
      
    }
    
    
    //sensorValue = (sensorValue+100) %1000;
    sensorValue = analogRead(analogInPin);
    if (sensorValue>=1000){
        packet[0]=13; 
    }else{
        packet[0]=12;
    }
    
    if(sensorValue != change and (sensorValue == 0 or sensorValue ==1023) ){
      
        timeC1 = micros();  
        Serial.print("timeC1: ");
        Serial.println(timeC1);
        putClockIntoPacket(sensorValue,timeC1,0x02);
        
        //timeC1=1046100012; //maximum length of long vaiable is 10 digital
        
        change = sensorValue;
        
        // receive data from master
        if(CAN_MSGAVAIL == CAN.checkReceive()){
            CAN.readMsgBuf(&reclen, buf);    // read data,  len: data length, buf: data buf

            unsigned int canId = CAN.getCanId();
            if (canId == 3){
                //Serial.println("gooooooood");
            
            
                timeC2 = micros();
          
                packet[0]=14;
                putClockIntoPacket(-1,timeC2,0x01);
                Serial.print("timeC2: ");
                Serial.println(timeC2);
                Serial.println("receive str from master");
                unsigned char len = 0;
                unsigned char buf[8];
                CAN.readMsgBuf(&len, buf);  
                for(int i = 0; i<len; i++){    // print the data
                    Serial.print(buf[i]);
                    Serial.print("\t");
                }    
            }
        }
    }
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
