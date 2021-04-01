#!/bin/bash
# $1 - hostname or IP address
# $2 - check script filename
# $3 - check script arguments
[ $# -ne 3 ] && { echo "Usage: $0 hostname_or_ip check_script_name check_script_args; exit 1 }
PLUGINS="/mnt/nagios_plugins"
RESULT=`ssh -q nagios@$1 $PLUGINS/$2 $3; echo $?`
OUTPUT=`echo $RESULT | awk '{print substr($0,0,length($0)-1)}'`
EXIT_CODE=`echo $RESULT | awk '{print substr($0, length($0),1)}'`
echo $OUTPUT
exit $EXIT_CODE
