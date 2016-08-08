#include <stdio.h>
#include <stdlib.h>

#include <netdb.h>
#include <netinet/in.h>
#include <string.h>

int main( int argc, char *argv[] ) {
	int sockfd, newsockfd, portno, clilen;
	char buffer[256];
	struct sockaddr_in serv_addr, cli_addr;
	int  n;
	char sec[100],usec[100];
	char point[1]=".";
	struct timeval tv1;
	FILE *wFile;
	/* First call to socket() function */

	/* Initialize socket structure */
	bzero((char *) &serv_addr, sizeof(serv_addr));
	portno = 10005;

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
	newsockfd = accept(sockfd, (struct sockaddr *)&cli_addr, &clilen);
	if (newsockfd < 0) {
		perror("ERROR on accept");
		exit(1);
	}
	
	wFile=fopen("data.txt","w");
	
	while(1){
		/* If connection is established then start communicating */
		read( newsockfd,buffer,255 );
		
		gettimeofday(&tv1,NULL);
		sprintf(sec,"%ld",tv1.tv_sec);
		sprintf(usec,"%ld",tv1.tv_usec);
		strcat(sec,point);
		strcat(sec,usec);

		printf("%s:sss:%s\n",buffer,sec);
		fwrite(buffer,sizeof(buffer),1,wFile);
		
	}
	exit(3);
	fclose(wFile);

	return 0;
}