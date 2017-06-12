# gen sync video mezz computer
# can beep at every second
# beep_factor=4

#!/usr/bin/env bash
# DURATION=120
# sh tone.sh 10
# ------------------------------------------------
# PROJECT SETTINGS
FF=$(which ffmpeg)
DURATION=$1
# LOG=""
LOG="-v quiet -stats"
OUTPUT_FOLDER='./tone'

if [ ! -d "$OUTPUT_FOLDER" ]; then
  mkdir $OUTPUT_FOLDER
fi
# ------------------------------------------------
# AUDIO SETTINGS
AUDIO="test_tone-$DURATION"

echo "===> Starting BarsTone Generator..."
echo "===> Specs 1k Tone - $DURATION seconds"
echo "===> Building audio..."

# Create Audio 24 bit - 120 seconds
$FF $LOG -f lavfi -i "sine=frequency=1000:sample_rate=48000:beep_factor=4:duration=$DURATION" -c:a pcm_s24le "temp_$AUDIO-mono-24b.wav"

echo "===> Creating 2Ch 24b audio..."
# Create 2Ch WAV file
$FF $LOG -i "temp_$AUDIO-mono-24b.wav" -i "temp_$AUDIO-mono-24b.wav" -filter_complex "[0:a][1:a]amerge=inputs=2[aout]" -map "[aout]" -c:a pcm_s24le -y "$OUTPUT_FOLDER/$AUDIO-2ch-24b.wav"

echo "===> removing temp files..."
rm temp_*

echo "===> Done!"
