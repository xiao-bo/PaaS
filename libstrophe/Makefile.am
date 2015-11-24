AUTOMAKE_OPTIONS = subdir-objects

ACLOCAL_AMFLAGS = -I m4
AM_CFLAGS = -g -Wall

PARSER_CFLAGS=@PARSER_CFLAGS@
PARSER_LIBS=@PARSER_LIBS@

SSL_CFLAGS = @openssl_CFLAGS@
SSL_LIBS = @openssl_LIBS@

STROPHE_FLAGS = -I$(top_srcdir)
STROPHE_LIBS = libstrophe.la

## Main build targets
lib_LTLIBRARIES = libstrophe.la

libstrophe_la_CFLAGS = $(SSL_CFLAGS) $(STROPHE_FLAGS) $(PARSER_CFLAGS)
libstrophe_la_LDFLAGS = $(SSL_LIBS) $(PARSER_LIBS)
# Export only public API
libstrophe_la_LDFLAGS += -export-symbols-regex '^xmpp_'
libstrophe_la_SOURCES = src/auth.c src/conn.c src/ctx.c \
	src/event.c src/handler.c src/hash.c \
	src/jid.c src/md5.c src/sasl.c src/scram.c src/sha1.c \
	src/snprintf.c src/sock.c src/stanza.c src/thread.c \
	src/tls_openssl.c src/util.c src/rand.c src/uuid.c \
	src/common.h src/hash.h src/md5.h src/ostypes.h src/parser.h \
	src/sasl.h src/scram.h src/sha1.h src/snprintf.h src/sock.h \
	src/thread.h src/tls.h src/util.h src/rand.h

if PARSER_EXPAT
libstrophe_la_SOURCES += src/parser_expat.c
else
libstrophe_la_SOURCES += src/parser_libxml2.c
endif

include_HEADERS = strophe.h
noinst_HEADERS = strophepp.h

pkgconfig_DATA = libstrophe.pc

#EXTRA_DIST = docs

## Examples
noinst_PROGRAMS=examples/send
examples_send_SOURCES = examples/send.c
examples_send_CFLAGS = $(STROPHE_FLAGS)
examples_send_LDADD = $(STROPHE_LIBS)


