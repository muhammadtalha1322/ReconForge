#!/bin/bash


echo "[+] ReconForge System Check"


echo "OS:"
uname -a


echo ""


for tool in nmap subfinder httpx nuclei
do

command -v $tool >/dev/null

if [ $? -eq 0 ]
then

echo "[OK] $tool"

else

echo "[MISSING] $tool"

fi

done
