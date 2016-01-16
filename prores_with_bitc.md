###Create ProRes with burned in timecode


- starts at 58:30:00
```
ffmpeg -i VF_DNxHD.mov -c:v prores -profile:v 3 -pix_fmt yuv422p10le -vf setdar=16:9 -acodec pcm_s16le -ar 48000 -vf "drawtext=fontfile=/Library/Fonts/Arial.ttf: timecode='00\:58\:30\:00': r=23.98: x=(w-tw)/2: y=h-1040: fontsize=60: fontcolor=white: box=1: boxcolor=0x00000099" OUTPUT_ProRes_BITC.mov
```