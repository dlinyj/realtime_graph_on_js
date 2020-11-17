#!/bin/bash
echo "Content-type: text/html;charset=utf-8"
echo
/usr/bin/python3 /usr/lib/cgi-bin/test.py > /dev/null 2&>1
echo "true" 
exit 0
