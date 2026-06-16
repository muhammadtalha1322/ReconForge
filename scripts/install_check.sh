#!/bin/bash


echo "[+] ReconForge Dependency Check"


tools=(

nmap

subfinder

httpx

nuclei

whatweb

)



for tool in "${tools[@]}"
do

if command -v $tool >/dev/null

then

echo "[OK] $tool"

else

echo "[MISSING] $tool"

fi


done
