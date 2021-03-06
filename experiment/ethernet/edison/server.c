#include <stdio.h>
#include <stdlib.h>

#include <netdb.h>
#include <netinet/in.h>
#include <string.h>
#include<signal.h>
volatile sig_atomic_t stop;//signal for ctrl-c
void inthand(int signum){
	stop=1;
}

int main( int argc, char *argv[] ) {
	int sockfd, newsockfd, portno, clilen;
	char buffer[256];
	struct sockaddr_in serv_addr, cli_addr;
	char sec[100],usec[100];
	struct timeval tv1;
	FILE *wFile;
	/* First call to socket() function */

	/* Initialize socket structure */
	bzero((char *) &serv_addr, sizeof(serv_addr));
	portno = atoi(argv[2]);

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(portno);

	bzero(buffer,256);
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	
	if (sockfd < 0) {
		perror("ERROR opening socket");
		exit(1);
	}
	/* Now bind the host address using bind() call.*/
	setsockopt(sockfd,SOL_SOCKET,SO_REUSEADDR,&serv_addr,sizeof(serv_addr));
	if(bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr))<0){
		perror("ERROR binding");
		exit(1);
	
	} 

	/* Now start listening for the clients, here process will
	 *       * go in sleep mode and will wait for the incoming connection
	 *          */
	listen(sockfd,5);
	clilen = sizeof(cli_addr);

	/* Accept actual connection from the client */
	/*
	newsockfd = accept(sockfd, (struct sockaddr *)&cli_addr, &clilen);
	if (newsockfd < 0) {
		perror("ERROR on accept");
		exit(1);
	}
	*/

	wFile=fopen(strcat(argv[1],".txt"),"w");
	
	// catch signal which leave infinite loop, or you can't close file 
	// Ctrl-c will send signal-  SIGINT
	signal(SIGINT,inthand);
	int i=0;	
	while(!stop){
		newsockfd = accept(sockfd, (struct sockaddr *)&cli_addr, &clilen);
		/* If connection is established then start communicating */
		read( newsockfd,buffer,255 );
		// get time 
		gettimeofday(&tv1,NULL);
		sprintf(sec,"%ld",tv1.tv_sec);
		sprintf(usec,"%ld",tv1.tv_usec);

		//cat time string 
		strcat(sec,".");
		strcat(sec,usec);
		//write file
		fprintf(wFile,"%s:mac time:re_time:%s\n",buffer,sec);
		printf("%s:mac time :re_time:%s\n",buffer,sec);
	}
	fclose(wFile);
	printf("safe exit\n");

	return 0;
}
