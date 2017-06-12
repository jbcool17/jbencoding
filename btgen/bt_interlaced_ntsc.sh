#!/usr/bin/env bash
# Author: John Brilla
# Description: Generates progressive test video using FFMPEG
# ------------------------------------------------------------------------------
# sh script.sh 100x100 16:9 10
# sh script.sh <resolution> <aspect_ratio> <duration>

# ------------------------------------------------
# PROJECT SETTINGS
FF=$(which ffmpeg)
SH=$(which sh)
RESOLUTION=$1
RATE=29.97
RATIO=$2
DURATION=$3
SCAN="I"
LOG="-v quiet -stats"
OUTPUT_FOLDER="./output"

if [ ! -d "$OUTPUT_FOLDER" ]; then
  mkdir $OUTPUT_FOLDER
fi

# ------------------------------------------------
# VIDEO SETTINGS
FILE_NAME="$RESOLUTION-$SCAN-${RATE//./}-${RATIO//:/x}"
TESTSRC_FILE_NAME="$FILE_NAME-TESTSRC"
SMPTEBARS_FILE_NAME="$FILE_NAME-SMPTEBARS"
SMPTEHDBARS_FILE_NAME="$FILE_NAME-SMPTEHDBARS"

GENERATOR_OPTIONS="duration=$DURATION:size=$RESOLUTION:rate=23.98"
TESTSRC_GENERATOR="testsrc=$GENERATOR_OPTIONS"
SMPTE_GENERATOR="smptebars=$GENERATOR_OPTIONS"
SMPTEHD_GENERATOR="smptehdbars=$GENERATOR_OPTIONS"
VIDEO_CODEC_SETTINGS="-flags:v +ildct+ilme -c:v prores -profile:v 2 -pix_fmt yuv422p10le -vf setdar=$RATIO"
TELECINE_SETTING="-flags:v +ildct+ilme -c:v prores -profile:v 2 -vf telecine=top:23"
MERGE_SETTING="-c copy -map 0:v:0 -map 1:a:0"

# ------------------------------------------------
# AUDIO SETTINGS
AUDIO_FINAL="tone/test_tone-$DURATION-2ch-24b.wav"

echo "===> Starting BarsTone Generator..."
echo "===> Specs $RESOLUTION - $RATE - $RATIO"
echo "===> Building audio..."
$SH tone.sh $DURATION

echo "===> Building video..."
# Generate 2398 Video
$FF $LOG -f lavfi -i $TESTSRC_GENERATOR $VIDEO_CODEC_SETTINGS "temp_testsrc-VIDEO-step1.mov"
$FF $LOG -f lavfi -i $SMPTE_GENERATOR $VIDEO_CODEC_SETTINGS "temp_smptebars-VIDEO-step1.mov"
$FF $LOG -f lavfi -i $SMPTEHD_GENERATOR $VIDEO_CODEC_SETTINGS "temp_smptehdbars-VIDEO-step1.mov"

echo "===> Telecine to 29.97 Interlaced..."
# Telecine to 29.97
$FF $LOG -i temp_testsrc-VIDEO-step1.mov $TELECINE_SETTING temp_testsrc-VIDEO-step2.mov
$FF $LOG -i temp_smptebars-VIDEO-step1.mov $TELECINE_SETTING temp_smptebars-VIDEO-step2.mov
$FF $LOG -i temp_smptehdbars-VIDEO-step1.mov $TELECINE_SETTING temp_smptehdbars-VIDEO-step2.mov

echo "===> Merging Audio with Video"
# Merge Audio Video
$FF $LOG -y -i "temp_testsrc-VIDEO-step2.mov" -i $AUDIO_FINAL $MERGE_SETTING "$OUTPUT_FOLDER/$TESTSRC_FILE_NAME.mov"
$FF $LOG -y -i "temp_smptebars-VIDEO-step2.mov" -i $AUDIO_FINAL $MERGE_SETTING "$OUTPUT_FOLDER/$SMPTEBARS_FILE_NAME.mov"
$FF $LOG -y -i "temp_smptehdbars-VIDEO-step2.mov" -i $AUDIO_FINAL $MERGE_SETTING "$OUTPUT_FOLDER/$SMPTEHDBARS_FILE_NAME.mov"

echo "===> removing temp files..."
rm temp_*

echo "===> Finished Job!"
