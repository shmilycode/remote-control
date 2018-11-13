#!/bin/sh

###############################
# Take 3 parameter
# 1. The server to upload log
# 2. The form name
# 3. The log file path
################################


#UPLOAD_SERVER="http://172.18.91.173/Code/upload/upload_file.php"
UPLOAD_SERVER=$1

#FORM_NAME="userfile"
FORM_NAME=$2

#ETHER=eth0
ETHER=$3

#ip_addr=$(ifconfig $ETHER | grep "inet addr" | awk '{ print $2}' | awk -F: '{print $2}')
ip_addr=$(ifconfig $ETHER | grep "inet " | awk 'NR==1 {print $2}')
LOG_FILE='/tmp/'$ip_addr"_udp_server.log"
echo "Upload log "$LOG_FILE

sync
curl --form "${FORM_NAME}=@${LOG_FILE}" $UPLOAD_SERVER