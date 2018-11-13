#!/bin/sh
#####################################
# Get 1 parameter
# 1. The port to enable input, output
#######################################

#PORT=16666
PORT=$1

iptables -A INPUT -p tcp -m tcp --dport $PORT -j ACCEPT
iptables -A INPUT -p udp -m udp --dport $PORT -j ACCEPT

iptables-save > /dev/null
iptables -L -n | grep $PORT

date '+%s.%N'
