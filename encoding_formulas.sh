#These some formulas I gather while I was a video engineer.
#Work in progress...


#Creates MP4 from SD Interlaced/or not source - with 2000k video, 192k audio - Deinterlacing
ffmpeg -i $INPUT -vb 2000k -pix_fmt yuv420p -ab 192k -vf "yadif=0:-1:0, scale=640:480" $OUTFILE.mp4

#HD 1080 - 8000k
#HD 720 - 5000k
#SD 480 - 2000k
ffmpeg -i $INPUT -vb 8000k -pix_fmt yuv420p -ab 192k  $OUTFILE.mp4


#TRANSPORT STREAM
ffmpeg -i $INPUT -vcodec mpeg2video -s 1920x1080 -r 23.976 -b:v 50M -minrate:v 50M -maxrate:v 50M -pix_fmt yuv420p -acodec mp2 -ac 2 -f mpegts $OUTPUT_FILE.ts


#Mono WAV to 5.1 AC3
ffmpeg -i front_left.wav -i front_right.wav -i front_center.wav -i lfe.wav -i back_left.wav -i back_right.wav -filter_complex "[0:a][1:a][2:a][3:a][4:a][5:a]amerge=inputs=6[aout]" -map "[aout]" -b:a 384k output.ac3

#AC3 to WAVs
ffmpeg -i audio.ac3 -filter_complex "channelsplit=channel_layout=5.1[FL][FR][FC][LFE][BL][BR]" -map "[FL]" front_left.wav -map "[FR]" front_right.wav -map "[FC]" front_center.wav -map "[LFE]" lfe.wav -map "[BL]" back_left.wav -map "[BR]" back_right.wav


#DXP - run this in the folder of the DPX sequence.
ffmpeg -f image2 -r 24/1 -pattern_type glob -i "*.dpx" -c:v prores -profile:v 3 -pix_fmt yuv422p10le OUTPUT.mov
