#!/usr/bin/env bash
# Author: John Brilla
# Description: Generates progressive test video using FFMPEG
# ------------------------------------------------------------------------------
# sh script.sh 1280x720 23.98 16:9 120
# sh script.sh <resolution> <rate> <aspect_ratio> <duration>

# ------------------------------------------------------------------------------
# PROJECT SETTINGS
FF=$(which ffmpeg)
SH=$(which sh)
RESOLUTION=$1
RATE=$2
RATIO=$3
DURATION=$4
SCAN="P"
LOG="-v quiet -stats"
OUTPUT_FOLDER='./output'


if [ ! -d "$OUTPUT_FOLDER" ]; then
  mkdir $OUTPUT_FOLDER
fi

# ------------------------------------------------------------------------------
# VIDEO SETTINGS
FILE_NAME="$RESOLUTION-$SCAN-${RATE//.}-${RATIO//:}"
TESTSRC_FILE_NAME="$FILE_NAME-TESTSRC"
SMPTEBARS_FILE_NAME="$FILE_NAME-SMPTEBARS"
SMPTEHDBARS_FILE_NAME="$FILE_NAME-SMPTEHDBARS"

GENERATOR_OPTIONS="duration=$DURATION:size=$RESOLUTION:rate=$RATE"
TESTSRC_GENERATOR="testsrc=$GENERATOR_OPTIONS"
SMPTE_GENERATOR="smptebars=$GENERATOR_OPTIONS"
SMPTEHD_GENERATOR="smptehdbars=$GENERATOR_OPTIONS"
VID_SETTINGS="-c:v prores -profile:v 3 -pix_fmt yuv422p10le -vf setdar=$RATIO"
MERGE_SETTING="-c copy -map 0:v:0 -map 1:a:0"

# ------------------------------------------------------------------------------
# AUDIO SETTINGS
AUDIO_FINAL="tone/test_tone-$DURATION-2ch-24b.wav"

echo "===> Starting BarsTone Generator..."
echo "===> Specs $RESOLUTION - $RATE - $RATIO"
echo "===> Building audio..."
# Create Audio 24 bit - 120 seconds
$SH tone.sh $DURATION

echo "===> Building video..."
# Generate Video

$FF $LOG -f lavfi -i $TESTSRC_GENERATOR $VID_SETTINGS "temp_testsrc-VIDEO.mov"
$FF $LOG -f lavfi -i $SMPTE_GENERATOR $VID_SETTINGS "temp_smptebars-VIDEO.mov"
$FF $LOG -f lavfi -i $SMPTEHD_GENERATOR $VID_SETTINGS "temp_smptehdbars-VIDEO.mov"

echo "===> Merging Audio with Video"
# Merge Audio Video
$FF $LOG -y -i "temp_testsrc-VIDEO.mov" -i "$AUDIO_FINAL" $MERGE_SETTING "$OUTPUT_FOLDER/$TESTSRC_FILE_NAME.mov"
$FF $LOG -y -i "temp_smptebars-VIDEO.mov" -i "$AUDIO_FINAL" $MERGE_SETTING "$OUTPUT_FOLDER/$SMPTEBARS_FILE_NAME.mov"
$FF $LOG -y -i "temp_smptehdbars-VIDEO.mov" -i "$AUDIO_FINAL" $MERGE_SETTING "$OUTPUT_FOLDER/$SMPTEHDBARS_FILE_NAME.mov"

echo "===> removing temp files..."
rm temp_*

echo "===> Finished Job!"
