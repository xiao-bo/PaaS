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
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char buffer[1024];

    portno = 11000;
    server = gethostbyname("192.168.11.8");
	adc_a0 = mraa_aio_init(2);//assign ping value
    
	// initial socket
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(portno);
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
	
	if (adc_a0 == NULL) {
        return 1;
    }

    char tmp[100];
	char point[1]=".";
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr));
	while(1){
        adc_value = mraa_aio_read(adc_a0);
		if (adc_value==1023){
			gettimeofday(&tv1,NULL);
			//sprintf(buffer,"%d",tv1.tv_sec);
			//sprintf(tmp,"%d",tv1.tv_usec);

			//strcat(buffer,point);
			//strcat(buffer,tmp);
			//write(sockfd,buffer,strlen(buffer));
			write(sockfd,point,1);
			usleep(500000);//microsecond
		}
	}
	mraa_aio_close(adc_a0);
	close(sockfd);
    return MRAA_SUCCESS;
}
