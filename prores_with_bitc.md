###Create ProRes with burned in timecode

- starts at 58:30:00
```
ffmpeg -i VF_DNxHD.mov -c:v prores -profile:v 3 -pix_fmt yuv422p10le -vf setdar=16:9 -acodec pcm_s16le -ar 48000 -vf "drawtext=fontfile=/Library/Fonts/Arial.ttf: timecode='00\:58\:30\:00': r=23.98: x=(w-tw)/2: y=h-1040: fontsize=60: fontcolor=white: box=1: boxcolor=0x00000099" OUTPUT_ProRes_BITC.mov
```

###Get timecode from ProRes
```shell
#GET TimeCode via ffbmc
echo “Getting timecode of video…!!!”
sleep 1

TIMECODE=$(ffmbc -i INPUT.mov 2>&1|grep timecode:|sed "s/[^0-9]*//")
echo $TIMECODE
echo “Reformatting timecode…!!!”
sleep 2

#Format TimeCode FFMPEG
TCFORMAT=$(echo "$TIMECODE" | sed -e 's/\:/\\\:/g')
echo $TCFORMAT

ffmpeg -i INPUT.mov -c:v prores -profile:v 3 -pix_fmt yuv422p10le -vf setdar=16:9 -acodec pcm_s16le -ar 48000 -vf "drawtext=fontfile=/Library/Fonts/Arial.ttf: timecode='$TCFORMAT': r=23.98: x=(w-tw)/2: y=h-1040: fontsize=60: fontcolor=white: box=1: boxcolor=0x00000099" OUTPUT_ProRes_BITC.mov

```