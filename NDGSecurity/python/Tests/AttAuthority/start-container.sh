#! /bin/sh
############################################################################
# Automatically generated by wsdl2web.py
# See LBNLCopyright for copyright notice!
###########################################################################

EXEC=twistd 
OPTIONS=-noy
CONFIG=server-config.tac

set - ${EXEC} ${OPTIONS} ${CONFIG} "$@"
exec "$@"
