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
#include "mraa/gpio.h"
#include<sys/time.h>
#define _POSIX_C_SOURCE 200809L
#include <inttypes.h>
#include <math.h>
#include <time.h>
#include<signal.h>

volatile sig_atomic_t stop;//signal for ctrl-c
volatile sig_atomic_t adc_value;//signal for ctrl-c
struct timespec tv1;
mraa_aio_context adc_a0;
long millsecond;

//volatile uint16_t adc_value = 0; //analog read value

void inthand(int signum){
	stop=1;
}
void error(const char *msg)
{
    perror(msg);
    exit(0);

    //send message
    
}
void handle(int signal){
    adc_value = mraa_aio_read(adc_a0);
}

int main(){
	int change = 0;	
	int previous;
	int current;
	//long millsecond;
    char message[1024];
    char tmp[100];
	char *ptr;// tmp variable for pointer
	FILE *wFile_all,*wFile_1023;
	previous=0;
	//timer decler
	sigset_t wait_signals,old_signals;
	sigemptyset(&wait_signals);
	//sigaddset(&wait_signals,SIGALRM);
	sigprocmask(SIG_BLOCK,&wait_signals,&old_signals);
	signal(SIGALRM,handle);	
	timer_t timer_id;
	timer_create(CLOCK_REALTIME,NULL,&timer_id);
	
	struct itimerspec timer_spec , old_timer_spec;
	timer_spec.it_value.tv_sec=1;
	timer_spec.it_value.tv_nsec=100000;
	timer_spec.it_interval.tv_sec=0;
	timer_spec.it_interval.tv_nsec=4000000;
	timer_settime(timer_id,0,&timer_spec,NULL);

	wFile_all=fopen("edison.txt","w");
	signal(SIGINT,inthand);
	adc_a0 = mraa_aio_init(1);// pin position
	adc_value=0;
	while(!stop){
		sigsuspend(&wait_signals);
		if(adc_value!=change && (adc_value==0 || adc_value ==1023)){
			// get current time
			clock_gettime(CLOCK_REALTIME, &tv1);
			millsecond=tv1.tv_nsec/1.0e2;

			fprintf(wFile_all,"%d:%d.%d\n",adc_value,tv1.tv_sec,millsecond);
			//printf("%d:%d.%d\n",adc_value,tv1.tv_sec,millsecond);
			change = adc_value;
		}
		
	}
	mraa_aio_close(adc_a0);
	fclose(wFile_all);
}
