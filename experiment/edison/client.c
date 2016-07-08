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
    uint16_t adc_value = 0; //assign pin value
	struct timeval tv1;// time value
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char buffer[1024];

    portno = 13000;
    server = gethostbyname("10.8.0.31");
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
	int i=0;
	while(i<30){
        adc_value = mraa_aio_read(adc_a0);
		if (adc_value>1022){
		sockfd = socket(AF_INET, SOCK_STREAM, 0);
		connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr));
			gettimeofday(&tv1,NULL);
			fprintf(stdout, "ADC A0 read %X - %d\n", adc_value, adc_value);
			printf("sec:%d.%d\n",tv1.tv_sec,tv1.tv_usec);
			sprintf(buffer,"%d",tv1.tv_sec);
			sprintf(tmp,"%d",tv1.tv_usec);

			strcat(buffer,point);
			strcat(buffer,tmp);
			
			printf("buffer : %s\n",buffer);
			n=write(sockfd,buffer,strlen(buffer));
			printf("%d\n",strlen(buffer));
			usleep(100000);//microsecond
		}
	}
	mraa_aio_close(adc_a0);
	close(sockfd);
    return MRAA_SUCCESS;
}
