#!/usr/bin/env bash
# Author: John Brilla
# Description: Beep every second
# ------------------------------------------------------------------------------
# sh script.sh 1280x720 23.98 16:9 120
# sh script.sh <resolution> <rate> <aspect_ratio> <duration>

# ------------------------------------------------------------------------------
# PROJECT SETTINGS
FF=$(which ffmpeg)
RESOLUTION=$1
RATE=$2
RATIO=$3
DURATION=$4
SCAN="P"
LOG="-v quiet -stats"
OUTPUT_FOLDER='./output'

# ------------------------------------------------------------------------------
# VIDEO SETTINGS
VID_SETTINGS="-c:v prores -profile:v 3 -pix_fmt yuv422p10le -vf setdar=$RATIO"
MAP_SETTING="-map 0:v:0 -map 1:a:0"
GENERATOR="testsrc=duration=$DURATION:size=$RESOLUTION:rate=$RATE"
FILE_NAME="$RESOLUTION-$SCAN-${RATE//.}-${RATIO//:/x}-SYNC"
TEMP_FILE="temp-VIDEO.mov"
AUDIO_FINAL="tone/test_tone-$DURATION-2ch-24b.wav"

if [ ! -d "$OUTPUT_FOLDER" ]; then
  mkdir $OUTPUT_FOLDER
fi

echo "===> Starting BarsTone Generator..."
echo "===> Specs $RESOLUTION - $RATE - $RATIO"

# Generate Audio
sh sync_audio.sh $DURATION

echo "===> Building video..."

# Generate Video
$FF $LOG -f lavfi -i $GENERATOR $VID_SETTINGS $TEMP_FILE

# Merge Audio Video
echo "===> Merging Audio with Video"
$FF $LOG -y -i $TEMP_FILE -i $AUDIO_FINAL -c copy $MAP_SETTING "$OUTPUT_FOLDER/$FILE_NAME.mov"

echo "===> removing temp files..."
rm temp*

echo "===> Finished Job!"
