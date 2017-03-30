#include <stdio.h>   /* Standard input/output definitions */
#include <string.h>  /* String function definitions */
#include <unistd.h>  /* UNIX standard function definitions */
#include <fcntl.h>   /* File control definitions */
#include <errno.h>   /* Error number definitions */
#include <termios.h> /* POSIX terminal control definitions */
#include <sys/time.h>
#include<stdlib.h>
/*
 *  * 'open_port()' - Open serial port 1.
 *   *
 *    * Returns the file descriptor on success or -1 on error.
 *     */
int read_data(void){
	struct timeval tv1; //time value
	int fd; /* File descriptor for the port */
	char buffer[1024];
	fd = open("/dev/cu.usbmodem1411", O_RDWR | O_NOCTTY | O_NDELAY);//open port
	struct termios options;
	// Get the current options for the port..
	tcgetattr(fd, &options);

	//Set the baud rates to 19200...

	cfsetispeed(&options, B115200);
	cfsetospeed(&options, B115200);

	//Enable the receiver and set local mode...
	options.c_cflag |= (CLOCAL | CREAD);

	// Set the new options for the port...

	if (fd == -1){
			//Could not open the port.
		perror("open_port: Unable to open /dev/ttyf1 - ");
	}
	else{
		fcntl(fd, F_SETFL, 0);
		//options.c_cc[VMIN]  = 10; /* Read 10 characters */  
		options.c_cc[VTIME]=0;
		tcsetattr(fd, TCSADRAIN, &options);
		read(fd,&buffer,1024);		

		printf("buffer:%s\n===end==\n",buffer);
		gettimeofday(&tv1,NULL);
		printf("sec:%d.%d\n",tv1.tv_sec,tv1.tv_usec);
		}
	//tcflush(fd,TCIOFLUSH);
	close(fd);
	return (fd);
}
int main() {
	int i;
	while(i<50){
		read_data();
		//printf("read serial data%d\n",i);
		i++;
	}
	
	//printf("read serial data%d\n",i);
	return 0;
}
