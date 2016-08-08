#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
#include <unistd.h>
#include "mraa/aio.h"
#include<sys/time.h>

void error(const char *msg)
{
    perror(msg);
    exit(0);

    //send message
    
}

int main(){
    mraa_aio_context adc_a0;
    uint16_t adc_value = 2; //assign pin value
	struct timeval tv1;// time value
    int sockfd, portno;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char message[1024];
    char tmp[100];

	// assign server ip address and port
    portno = 11000;
    server = gethostbyname("192.168.11.8");
	
	//assign ping value
	adc_a0 = mraa_aio_init(2);
    
	// initial property of socket 
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(portno);
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
	
	if (adc_a0 == NULL) {
        return 1;
    }

	// build socket connection
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr));

	while(1){
		// read analog value
        adc_value = mraa_aio_read(adc_a0);

		if (adc_value==1023){
			// get current time 
			gettimeofday(&tv1,NULL);

			// transfer integer of time into string
			sprintf(message,"%d",tv1.tv_sec);
			sprintf(tmp,"%d",tv1.tv_usec);

			// cascades sec and usec by "." , for example 10.1234567  
			strcat(message,".");
			strcat(message,tmp);

			// send message by socket
			write(sockfd,message,strlen(message));

			usleep(500000);//microsecond
		}
	}
	mraa_aio_close(adc_a0);
	close(sockfd);
    return MRAA_SUCCESS;
}
