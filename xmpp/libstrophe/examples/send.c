/* send.c
** libstrophe XMPP client library -- basic usage example
**
** Copyright (C) 2005-2009 Collecta, Inc. 
**
**  This software is provided AS-IS with no warranty, either express
**  or implied.
**
** This program is dual licensed under the MIT and GPLv3 licenses.
*/

/* simple bot example
**  
**
** This file will send  messages to xmpp.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <strophe.h>



/* define a handler for connection events */
void conn_handler(xmpp_conn_t * const conn, const xmpp_conn_event_t status, 
		const int error, xmpp_stream_error_t * const stream_error,
		void * const userdata)
{
	xmpp_ctx_t *ctx = (xmpp_ctx_t *)userdata;


	if (status == XMPP_CONN_CONNECT) {
		xmpp_stanza_t *message ,*body,*text;
		fprintf(stderr, "DEBUG: connected\n");

		
		/* inital message object*/
		message = xmpp_stanza_new(ctx);
		xmpp_stanza_set_name(message,"message");//name can not match object'name
		xmpp_stanza_set_type(message,"chat");

		//set message's target,attribute
		xmpp_stanza_set_attribute(message,"to","pig@localhost");

		/* inital message's context object*/
		body = xmpp_stanza_new(ctx);
		xmpp_stanza_set_name(body,"body");
		//print("%d\n",i);
		text = xmpp_stanza_new(ctx);
		xmpp_stanza_set_text(text,"hello I am xiao2");
		/*add text to body, and add body to message*/
		xmpp_stanza_add_child(body,text);
		xmpp_stanza_add_child(message,body);

		//send data
		xmpp_send(conn,message);
		
		//close connect
		xmpp_stanza_release(message);
		xmpp_disconnect(conn);



	}
	else {
		fprintf(stderr, "DEBUG: disconnected\n");
		xmpp_stop(ctx);
	}
}

int main(int argc, char **argv)
{
	xmpp_ctx_t *ctx;
	xmpp_conn_t *conn;
	char *jid, *pass;


	jid="xiao@localhost";
	pass="1119";
	
	/* init library */
	xmpp_initialize();

	/* create a context */
	ctx = xmpp_ctx_new(NULL, NULL);

	/* create a connection */
	conn = xmpp_conn_new(ctx);


	/* setup authentication information */
	xmpp_conn_set_jid(conn, jid);
	xmpp_conn_set_pass(conn, pass);
	/* initiate connection */
	int i=2;
	xmpp_connect_client(conn, NULL, 0, conn_handler, ctx);

	/* enter the event loop - 
	   our connect handler will trigger an exit */
	xmpp_run(ctx);

	/* release our connection and context */
	xmpp_conn_release(conn);
	xmpp_ctx_free(ctx);

	/* final shutdown of the library */
	xmpp_shutdown();

	return 0;
}
