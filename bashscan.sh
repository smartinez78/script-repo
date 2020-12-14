#!/bin/bash
#This script contains code that was modified from cyberciti.biz by Author: Vivek Gite
#This script will perform a port scan of an input ip  from ports 1-1024 when executed
#Name: Sofia Martinez, ITMS-543

# collect start time
start=`date +%s`

#ask the user to enter an ip address
echo "Enter an IP address to scan:"
read ip

echo " "
echo "Scanning ip.......$ip"
echo " "
echo "Scan Results:"

#for loop to interate through ports
for (( port=1; port<=1024; port++ ))
do
	(echo >/dev/tcp/$ip/$port) &>/dev/null && echo "Port $port is open" | grep open
done

# calculate and report total time elapsed
stop=`date +%s`
time="$(($stop-$start))"
echo "Total run time.......$time seconds"

exit 0
