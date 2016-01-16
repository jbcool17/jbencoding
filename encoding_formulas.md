##Collection of Formulas - Video/Audio
- Work in progress...


###Creates MP4 from SD Interlaced/Progressive source - with 2000k video, 192k audio - w/Deinterlacing
```shell
ffmpeg -i $INPUT -vb 2000k -pix_fmt yuv420p -ab 192k -vf "yadif=0:-1:0, scale=640:480" $OUTFILE.mp4
```

###Creates MP4 
- deinterlace if necessary
- HD 1080 - 8000k
- HD 720 - 5000k
- SD 480 - 2000k
```
ffmpeg -i $INPUT -vb 8000k -pix_fmt yuv420p -ab 192k  $OUTFILE.mp4
```

###TRANSPORT STREAMS
```
ffmpeg -i $INPUT -vcodec mpeg2video -s 1920x1080 -r 23.976 -b:v 50M -minrate:v 50M -maxrate:v 50M -pix_fmt yuv420p -acodec mp2 -ac 2 -f mpegts $OUTPUT_FILE.ts
```

```
ffmpeg -i $INPUT -vcodec libx264 -s 1920x1080 -r 23.976 -b:v 5M -minrate:v 5M -maxrate:v 5M -pix_fmt yuv420p -an -f mpegts $OUTPUT_FILE.ts
```

###Merges Audio/Video
```
ffmpeg -i ATT_-OUTPUT_FILE-noaudio.ts -i audio.ac3 -map 0 -map 1 -codec copy -shortest output_video.ts
```

###Mono WAV to 5.1 AC3
```
ffmpeg -i front_left.wav -i front_right.wav -i front_center.wav -i lfe.wav -i back_left.wav -i back_right.wav -filter_complex "[0:a][1:a][2:a][3:a][4:a][5:a]amerge=inputs=6[aout]" -map "[aout]" -b:a 384k output.ac3
```

###AC3 to WAVs
```
ffmpeg -i audio.ac3 -filter_complex "channelsplit=channel_layout=5.1[FL][FR][FC][LFE][BL][BR]" -map "[FL]" front_left.wav -map "[FR]" front_right.wav -map "[FC]" front_center.wav -map "[LFE]" lfe.wav -map "[BL]" back_left.wav -map "[BR]" back_right.wav
```

###ProRes - aspect 16x9
```
ffmpeg -i $INPUT -c:v prores -profile:v 3 -pix_fmt yuv422p10le -vf setdar=16:9 -acodec pcm_s16le -ar 48000 $OUTPUT.mov
```

###DXP - run this in the folder of the DPX sequence.
```
ffmpeg -f image2 -r 24/1 -pattern_type glob -i "*.dpx" -c:v prores -profile:v 3 -pix_fmt yuv422p10le OUTPUT.mov
```

###OGG - Theora
```
-codec:v libtheora -qscale:v 7 -codec:a libvorbis -qscale:a 5 OUTPUT.ogg
```
```
-codec:v libtheora -b:v 1600k -codec:a libvorbis -b:a 128k -vf scale=960:540 OUTPUT.ogg
```


### MOV to wav - mapping FFMPEG	
```
ffmpeg -i MOVIE.mov -vn -acodec pcm_s24le -map 0:0 left.wav && ffmpeg -i MOVIE.mov -vn -acodec pcm_s24le -map 0:1 right.wav && ffmpeg -i MOVIE.mov -vn -acodec pcm_s24le -map 0:2 center.wav && ffmpeg -i POKEMONSHORT_PLUSFEATURE_17_v3.mov -vn -acodec pcm_s24le -map 0:3 lfe.wav && ffmpeg -i POKEMONSHORT_PLUSFEATURE_17_v3.mov -vn -acodec pcm_s24le -map 0:4 ls.wav && ffmpeg -i POKEMONSHORT_PLUSFEATURE_17_v3.mov -vn -acodec pcm_s24le -map 0:5 rs.wav
```

### MOV to wav - mapping	FFMPEG	
```
ffmpeg -i $MOV -vn -acodec pcm_s24le -map 0:1 left.wav && ffmpeg -i $MOV -vn -acodec pcm_s24le -map 0:2 right.wav && ffmpeg -i $MOV -vn -acodec pcm_s24le -map 0:3 center.wav && ffmpeg -i $MOV -vn -acodec pcm_s24le -map 0:4 lfe.wav && ffmpeg -i $MOV -vn -acodec pcm_s24le -map 0:5 ls.wav && ffmpeg -i $MOV -vn -acodec pcm_s24le -map 0:6 rs.wav
```

### Pull 5.1 from MOV to WAV	FFMPEG	
```
ffmpeg -i {INPUT FILE}.mov -filter_complex "channelsplit=channel_layout=5.1[FL][FR][FC][LFE][BL][BR]" -map "[FL]" LEFT.wav -map "[FR]" RIGHT.wav -map "[FC]" CENTER.wav -map "[LFE]" Lfe.wav -map "[BL]" LEFT_SURROUND.wav -map "[BR]" RIGHT_SURROUND.wav
```

### 2 Mono Channels to STEREO	FFMPEG	
```
ffmpeg -i left.mp3 -i right.mp3 -filter_complex "[0:a][1:a]amerge=inputs=2[aout]" -map "[aout]" output.wav
```


###AUDIO 
###Loop - AIF to WAV
```
for name in *.aif; do ffmpeg -i "$name" -acodec pcm_s24le "${name%.*}.wav"; done
```



