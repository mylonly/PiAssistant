#!/usr/bin/sh

file="./tts/libtts.so"

if[ ! -f "$file" ]; then
    cd ./tts/
    make   
file

cd /root/tools/PiAssistant/ 
python ./src/clockSpeaker.py &
mplayer ./src/tts.wav