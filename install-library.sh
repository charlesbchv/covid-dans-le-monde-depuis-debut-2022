#! /bin/bash

failure()
{
	echo "$(tput setaf 7; tput setab 1; tput bold)[KO]$(tput sgr 0)"
	exit 1
}

pip install dash
[ $? -eq 0 ] || failure

pip install plotly-express;
[ $? -eq 0 ] || failure

pip install plotly;
[ $? -eq 0 ] || failure

pip install pandas;
[ $? -eq 0 ] || failure
