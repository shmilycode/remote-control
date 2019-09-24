#!/bin/sh

#####################
# Get 3 parameter
# 0. Transfer mode, m for multicast, t for tcp
# 1. The script path
# 2. server address
#####################

TRANSFER_MODE=$1
SCRIPT_PATH=$2
SERVER_ADDRESS=$3

#ip_addr=$(ifconfig $ETHER | grep "inet " | awk '{ print $2}' | awk -F: '{print $2}')
ip_addr=$(ifconfig $ETHER | grep "inet " | awk 'NR==1 {print $2}')
LOG_FILE="/tmp/"$ip_addr"_multicast_server.log"

echo "Save log to "$LOG_FILE

if [ "$TRANSFER_MODE" == "m" ];then
nohup python $SCRIPT_PATH"/mfiletransfer.py" -c -a $SERVER_ADDRESS>$LOG_FILE 2>&1 &
elif [ "$TRANSFER_MODE" = "t" ];then
nohup python $SCRIPT_PATH"/tcptransfer.py" -c -a $SERVER_ADDRESS>$LOG_FILE 2>&1 &
fi