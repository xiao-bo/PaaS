// demo: CAN-BUS Shield, send data
#include <mcp_can.h>
#include <SPI.h>

// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
const int SPI_CS_PIN = 9;
MCP_CAN CAN(SPI_CS_PIN); // Set CS pin

//packet
unsigned char packet[8] = {0,0,0,0,0,0,0,0};

//for loop variable
int i;

// for split variable
unsigned long tmp;




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
      
    CAN.sendMsgBuf(0x13,0,8,packet);    
    //delayMicroseconds(500); //80%
    delayMicroseconds(1140); //35%
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
