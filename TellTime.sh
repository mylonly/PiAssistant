#!/usr/bin/sh

file="./tts/libtts.so"

if[ ! -f "$file" ]; then
    cd ./tts/
    make &
    cd ../    
fi

python ./src/clockSpeaker.py &
mplayer ./src/tts.wav