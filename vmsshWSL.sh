#!/bin/bash
ipaddr=$(arp.exe -a | grep 00-15-5d-38-01-03 | awk '{print $1}')
ssh taran@$ipaddr
