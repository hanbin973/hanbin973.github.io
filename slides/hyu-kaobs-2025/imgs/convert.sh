#!/bin/bash

dir_bak=./
dir_eps=./

if [ ! -d ${dir_bak} ]; then
    mkdir -p ${dir_bak}
fi

if [ ! -d "${dir_eps}" ]; then
    mkdir -p ${dir_eps}
fi

check=$(ls|grep eps)
if [ ! -z "${check}" ]; then
for fullfile in *.eps; do
    filename="${fullfile%.*}"
    extension="${fullfile##*.}"
#    if [ ! -f ${filename}.svg ]; then
        echo "${fullfile} --> ${filename}.svg"
        ps2pdf -dEPSCrop ${fullfile} tmp.pdf
        pdf2svg tmp.pdf ${filename}.svg
        rm tmp.pdf
        mv ${fullfile} ${dir_eps}
        mv ${dir_eps}/${fullfile} ${dir_eps}/$(date +%y%m%d%H%M%S)_${fullfile}
#    fi
done
fi
