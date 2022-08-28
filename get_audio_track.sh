ls $1 | sed 's/.mp4//g' | \
xargs -I fn -P4 ffmpeg -loglevel 0 -i $1/fn.mp4 -ar 16000 -ac 1 $2/fn.wav -y