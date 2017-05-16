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
#define _POSIX_C_SOURCE 200809L
#include <inttypes.h>
#include <math.h>
#include <time.h>
#include<signal.h>

volatile sig_atomic_t stop;//signal for ctrl-c
void inthand(int signum){
	stop=1;
}
void error(const char *msg)
{
    perror(msg);
    exit(0);

    //send message
    
}

int main(){
    mraa_aio_context adc_a0;
    uint16_t adc_value = 2; //assign pin value
	long ms;
	//struct timeval tv1;// time value
	struct timespec tv1;
    int sockfd, portno;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char message[1024];
    char tmp[100];
	FILE *wFile;
	// assign server ip address and port
    portno = 11000;
    server = gethostbyname("192.168.11.3");
	
	//assign ping value
	adc_a0 = mraa_aio_init(2);
	if (adc_a0 == NULL) {
        return 1;
    }
	// initial property of socket 
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(portno);
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);

	// build socket connection
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr));
	//write file
	wFile=fopen("edison.txt","w");

	// stop signal
	signal(SIGINT,inthand);
	while(!stop){
		// read analog value
        adc_value = mraa_aio_read(adc_a0);
		//printf("adc_value%d\n",adc_value);
		if (adc_value>0){
			// get current time 
			clock_gettime(CLOCK_REALTIME, &tv1);
			ms=tv1.tv_nsec/1.0e2;

			// transfer integer of time into string
			sprintf(message,"%d",tv1.tv_sec);
			sprintf(tmp,"%d",ms);

			// cascades sec and usec by "." , for example 10.1234567  
			strcat(message,".");
			strcat(message,tmp);
			
			// send message by socket
			write(sockfd,message,strlen(message));
			fprintf(wFile,"%s\n",message);
			printf("%s\n",message);
			
			usleep(500000);//microsecond  500000=0.5s for 1hz
		}
	}
	mraa_aio_close(adc_a0);
	//close(sockfd);
	fclose(wFile);
    return MRAA_SUCCESS;
}
