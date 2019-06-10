#!/bin/bash

alarmInfo=""
alarmURL=""

if [ $1 ]; then
	alarmInfo="Alarm was set at $1 :"
	alarmURL="hour=$1"

	if [ $2 ]; then
		alarmInfo="$alarmInfo $2 :"
		alarmURL="$alarmURL&minute=$2"

		if [ $3 ]; then
			alarmInfo="$alarmInfo $3"
			alarmURL="$alarmURL&second=$3"
		else
			alarmInfo="$alarmInfo 00"
			alarmURL="$alarmURL&second=00"
		fi

	else
		alarmInfo="$alarmInfo 00 : 00"
		alarmURL="$alarmURL&minute=00&second=00"
	fi
     	
fi
echo $alarmInfo
pathToAlarm=$(find ~ -name "alarm.html" 2> /dev/null)
google-chrome "file://$pathToAlarm?$alarmURL" &
