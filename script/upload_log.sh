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

#LOG_FILE="/tmp/network_test/network_test.log"
LOG_FILE=$3

curl --form "${FORM_NAME}=@${LOG_FILE}" $UPLOAD_SERVER
