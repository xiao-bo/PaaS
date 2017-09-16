// demo: CAN-BUS Shield, send data
// loovee@seeed.cc

#include <mcp_can.h>
#include <SPI.h>

// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
const int SPI_CS_PIN = 9;

MCP_CAN CAN(SPI_CS_PIN);                                    // Set CS pin

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
int initial=0;
unsigned char stmp[8] = {0, 0, 0, 0,0,0,0,0};
unsigned char a[8] = {3, 1, 0, 0,0,0,0,0};
void loop()
{
    unsigned char reclen = 0;
    unsigned char buf[8];
    
    
    CAN.sendMsgBuf(0x00, 0,8, stmp);
        
    Serial.print("sendMsg  ");
    Serial.println(stmp[7]);
    stmp[7] = (stmp[7]+1)%8;
    
    
    /*
    CAN.sendMsgBuf(0x00, 0,8, stmp);
    Serial.print("sendMsg  ");
    Serial.println(stmp[7]);
    stmp[7] = (stmp[7]+1)%8;
    delay(1000);    
    CAN.sendMsgBuf(0x01, 0,8,a);
    Serial.print("send a  ");
    Serial.println(a[7]);
    a[7] = (a[7]+1)%8;
    */
    // send data:  id = 0x00, standrad frame, data len = 8, stmp: data buf
    
    if(CAN_MSGAVAIL == CAN.checkReceive())            // check if data coming
    { 
        CAN.readMsgBuf(&reclen, buf);
        unsigned int canId = CAN.getCanId();
        
        Serial.print("receive id = ");
        Serial.println(canId);
        CAN.sendMsgBuf(0x01, 0,8, a);
        Serial.print("sendSecondMsg  ");
        Serial.println(a[0]);
        a[0] = (a[0]+3)%8;
    }
    
    
    

   
    //delay(1000);                       // send data per 100ms
}

// END FILE
