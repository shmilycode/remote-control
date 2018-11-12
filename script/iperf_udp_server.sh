#!/bin/sh

#####################
# Get 2 parameter
# 1. Log filename to save log
# 2. The iperf path, default in /usr/bin
# 3. The listening port
#####################

#LOG_FILE="/tmp/network_test/1.log"
LOG_FILE=$1
#IPERF_PATH="/tmp/network_test/"
IPERF_PATH=$2
#LISTEN_PORT=16666
LISTEN_PORT=$3 

echo "Save log to "$LOG_FILE

#listen for iperf
$IPERF_PATH"/iperf" -s -i 1 -p $LISTEN_PORT | tee $LOG_FILE


