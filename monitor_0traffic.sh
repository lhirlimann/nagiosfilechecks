#!/bin/sh

if [ -z $1 ]
then
	echo "Please provide the interface you want monitor"
	echo "for example $0 eth0"
	exit 1
fi

`ip a show $1 >/dev/null`
if [ $? -gt 0 ]
then
	echo "Please provide an existing interface to monitor"
	exit 1
fi

`which ifstat >/dev/null`
if [ $? -gt 0 ]
then
	echo "ifstat is not installed on your system and is"
	echo "needed for $0 to work"
	exit 1
fi

rc=`ifstat $1 |grep $1 |awk '{print $2;}'`
echo rc = $rc
if [ $rc = "0" ]
then
	echo "ERROR - no traffic on $1"
	exit 2
else
	echo "OK - there is traffic on $1"
	exit 0
fi
