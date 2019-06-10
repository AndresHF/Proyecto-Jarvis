#!/bin/bash

ORANGE='\033[0;33m'
LBLUE='\033[1;34m'
LCYAN='\033[1;36m'
RESTORE='\033[1;32m'

sudo printf "${RESTORE}Looking for ${LCYAN}$1${RESTORE}";echo

if echo $2 | grep "deep" > /dev/null; then
	results=$(find / -type d -name *$1* 2> /dev/null)
elif echo $2 | grep "file" > /dev/null; then
	results=$(find / -type f -name *$1* 2> /dev/null)
	file=true
else 
	results=$(find ~/ -type d -name $1 2> /dev/null)
fi

lines=0
selectedLine="wrong"
result="undefined"

function openCode() {

	result=$(echo $results | tr " " "\n" | head -$selectedLine | tail -1)
	printf "Do you want to code ${LCYAN}$result${RESTORE} ? (y/n)";echo
	answer="wrong"

	while echo $answer | egrep -xv "(y)|(n)" > /dev/null; do
		read answer
	done 
	
	if echo $answer | grep "y" > /dev/null; then
		printf "Opening ${LCYAN}$result${RESTORE}... Have a nice coding!!";echo
	
		if echo $file | grep "true" > /dev/null; then
			sudo code --user-data-dir="~/.vscode-root" $result
			exit 0
		fi
		cd $result
		sudo code . --user-data-dir
		exit 0
	else
		selectedLine="wrong"
		checkMatches	
	fi
}

function checkMatches() {

if $(echo $results | egrep "[a-zA-Z]" > /dev/null); then
	lines=$(echo $results | tr " " "\n" | wc -l)
	printf "$lines matches!!\n"
	
	if [[ "$lines" > 1 ]]; then
	
		printf "${ORANGE}Select one of the following:${LCYAN}";echo;echo #'(type something to contiue...)'
		nl -n ln <(printf "${LCYAN}$results" | tr " " "\n")
		echo
		printf "${ORANGE}Type the selected line:${RESTORE} "

		while echo $selectedLine | egrep "[a-zA-Z - */?.'\[!¡¿#~$%&\(\)=]" > /dev/null; do
			read selectedLine
			selectedLine=$(awk -v var="$selectedLine" -v top="$lines" 'BEGIN{if((var > 0) && (var <= top)) print var; else print "Wrong number... must be between 1-"top}')
			echo $selectedLine | grep "number"
		done

		result=$(echo $results | tr " " "\n" | head -$selectedLine | tail -1)
        openCode
	else
		selectedLine=1
		openCode
	fi
else
	echo "No matches..."
	exit 1
fi

}

checkMatches
