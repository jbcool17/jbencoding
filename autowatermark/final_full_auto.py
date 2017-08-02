# !/usr/bin/env python
# python script.py <file_name> <first> <last>
import os,sys,numpy,datetime
from moviepy.editor import *
from random import randint
import lib.chapters as chapters
import lib.sdtools as sdtools
import lib.utilities as utilities

reload(sys)
sys.setdefaultencoding('utf-8')

# Benchmarks
start = datetime.datetime.now()

# SETUP VARIABLES
c = 0
first_video_num = int(sys.argv[2])
last_video_num  = int(sys.argv[3])
total_videos    = last_video_num - first_video_num

# Video Info
full_file_name  = sys.argv[1]
file_name_noext = os.path.splitext(full_file_name)[0]
log_name        = file_name_noext
video           = VideoFileClip(full_file_name)
video_duration  = video.duration
output_dir      = "OUTPUT"
log_dir         = "LOG"
working_dir     = os.popen('pwd').read().strip()

print "Setting up folders..."
if ( not os.path.exists(output_dir) ):
    os.system("mkdir {0}".format(output_dir))
    print "Output directory has been created."
else:
    print "Output directory has already been created."

if ( not os.path.exists(log_dir) ):
    os.system("mkdir {0}".format(log_dir))
    print "Log directory has been created."
else:
    print "Log directory has already been created."

utilities.write_to_log(log_dir, log_name, 'Starting...')
utilities.write_to_log(log_dir, log_name, "Video: {0}".format(full_file_name) )
utilities.write_to_log(log_dir, log_name, "Duration: {0}".format(video_duration) )
utilities.write_to_log(log_dir, log_name, " Videos {0} to {1} will be created.".format(first_video_num, last_video_num) )

# ANALYZING VIDEO
# Scene Detection
ffout_log      = log_dir + '/' + file_name_noext + '_ffout'
timestamps_log = log_dir + '/' + file_name_noext + '_timestamps'

# check if files exist?
if ( not os.path.isfile(ffout_log) ):
    print "Starting Scene Detection..."
    sdtools.detection(full_file_name,ffout_log)
else:
    print 'File found. Skipping Scene Detection...'

# Get Time Stamps
if ( not os.path.isfile(timestamps_log) ):
    print "Parsing timestamps..."
    sdtools.parse_timestamps(ffout_log,timestamps_log)
else:
    print 'File found. Skipping Timestamp parsing...'

# Read timestamps to Array
ts_list = []
f = open(timestamps_log)
for line in f:
    ts_list.append(line.strip('\n'))

# convert str to int/float
ts_list = map(float, ts_list)
ts_length = len(ts_list)

# Setting Times
print "Setting times..."
t1 = sdtools.set_time(15, 1, 't1', ts_list)
t2 = sdtools.set_time(t1, 3, 't2', ts_list) #+ 1
t3 = sdtools.set_time(t2, (ts_length / 4), 't3', ts_list)
t4 = sdtools.set_time(t3, (ts_length / 3), 't4', ts_list)
t5 = sdtools.set_time(t4, (ts_length / 2), 't5', ts_list) # open + 1

utilities.write_to_log(log_dir, log_name, "Marker1: {0}".format(t1))
utilities.write_to_log(log_dir, log_name, "Marker2: {0}".format(t2))
utilities.write_to_log(log_dir, log_name, "Marker3: {0}".format(t3))
utilities.write_to_log(log_dir, log_name, "Marker4: {0}".format(t4))
utilities.write_to_log(log_dir, log_name, "Marker5: {0}".format(t5))

# Setting Chapters
print "Setting Chapters..."
chapter1 = chapters.convert_seconds(t1)
chapter2 = chapters.convert_seconds(t2)
chapter3 = chapters.convert_seconds(t3)
chapter4 = chapters.convert_seconds(t4)
chapter5 = chapters.convert_seconds(t5)

utilities.write_to_log(log_dir, log_name, "Chapter1: {0}".format(chapter1))
utilities.write_to_log(log_dir, log_name, "Chapter2: {0}".format(chapter2))
utilities.write_to_log(log_dir, log_name, "Chapter3: {0}".format(chapter3))
utilities.write_to_log(log_dir, log_name, "Chapter4: {0}".format(chapter4))
utilities.write_to_log(log_dir, log_name, "Chapter5: {0}".format(chapter5))

chapters = "%s,%s,%s,%s,%s" % (chapter1,chapter2,chapter3,chapter4,chapter5)

# Setting Locations
print "Setting locations..."
video_w = 600
video_h = 400
slx1 = randint(0, video_w)
sly1 = randint(0, video_h)
blx1 = randint(0, video_w)
bly1 = randint(0, video_h)

slx2 = randint(0, video_w)
sly2 = randint(0, video_h)
blx2 = randint(0, video_w)
bly2 = randint(0, video_h)

slx3 = randint(0, video_w)
sly3 = randint(0, video_h)
blx3 = randint(0, video_w)
bly3 = randint(0, video_h)

slx4 = randint(0, video_w)
sly4 = randint(0, video_h)
blx4 = randint(0, video_w)
bly4 = randint(0, video_h)

slx5 = randint(0, video_w)
sly5 = randint(0, video_h)
blx5 = randint(0, video_w)
bly5 = randint(0, video_h)

utilities.write_to_log(log_dir, log_name, "Marker1 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx1,sly1,blx1,bly1))
utilities.write_to_log(log_dir, log_name, "Marker2 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx2,sly2,blx2,bly2))
utilities.write_to_log(log_dir, log_name, "Marker3 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx3,sly3,blx3,bly3))
utilities.write_to_log(log_dir, log_name, "Marker4 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx4,sly4,blx4,bly4))
utilities.write_to_log(log_dir, log_name, "Marker5 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx5,sly5,blx5,bly5))

print "Project variables have been set."
# THE LOOP
# wait 5seconds

# Font Size
sfs = 9
bfs = 30

# Small text duration - may need to be tweeked
strt = .06
print "--------------------------------------------------------"
while c < (total_videos + 1):
    number            = first_video_num + c
    output_name       = "/%s_%d.mov" % (file_name_noext,number)
    output_file_name_noext = os.path.splitext(output_name)[0]
    utilities.write_to_log(log_dir, log_name, 'Rendering video with number: {0}'.format(number))
    print "Rendering video with number %d." % number

    # 01 Create TEXT STEP
    # small text 1 frame - pop on
    stc1 = (TextClip(str(number),fontsize=sfs,font='Arial',color='white')
                 .set_pos((slx1, sly1))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc1 = (TextClip(str(number),fontsize=bfs,font='Arial',color='white').set_pos((blx1, bly1))).set_duration(15)

    # 02 Create TEXT STEP
    # small text 1 frame - pop on
    stc2 = (TextClip(str(number),fontsize=sfs,font='Arial',color='white')
                 .set_pos((slx2, sly2))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc2 = (TextClip(str(number),fontsize=bfs,font='Arial',color='white').set_pos((blx2, bly2))).set_duration(15)

    # 03 Create TEXT STEP
    # small text 1 frame - pop on
    stc3 = (TextClip(str(number),fontsize=sfs,font='Arial',color='white')
                 .set_pos((slx3, sly3))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc3 = (TextClip(str(number),fontsize=bfs,font='Arial',color='white').set_pos((blx3, bly3))).set_duration(15)

    # 04 Create TEXT STEP
    # small text 1 frame - pop on
    stc4 = (TextClip(str(number),fontsize=sfs,font='Arial',color='white')
                 .set_pos((slx4, sly4))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc4 = (TextClip(str(number),fontsize=bfs,font='Arial',color='white').set_pos((blx4, bly4))).set_duration(15)

    # 05 Create TEXT STEP
    # small text 1 frame - pop on
    stc5 = (TextClip(str(number),fontsize=sfs,font='Arial',color='white')
                 .set_pos((slx5, sly5))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc5 = (TextClip(str(number),fontsize=bfs,font='Arial',color='white').set_pos((blx5, bly5))).set_duration(15)

    # Composite Clips and Text numbers together. Fadein & Fadeout w/crossfade
    # GET START time based scene detection for 5 evenly spaced points
    final_video = CompositeVideoClip([video,
                                     stc1.set_start(t1),
                                     stc2.set_start(t2),
                                     stc3.set_start(t3),
                                     stc4.set_start(t4),
                                     stc5.set_start(t5),
                                     btc1.set_start(t1).crossfadein(2).crossfadeout(2),
                                     btc2.set_start(t2).crossfadein(2).crossfadeout(2),
                                     btc3.set_start(t3).crossfadein(2).crossfadeout(2),
                                     btc4.set_start(t4).crossfadein(2).crossfadeout(2),
                                     btc5.set_start(t5).crossfadein(2).crossfadeout(2)])

    # write the result to a file in any format = with uncompressed audio - ProRes
    final_video.to_videofile( output_dir + '/' + output_name, codec='prores',
                              audio_codec='pcm_s16le',
                              ffmpeg_params=['-vf', 'setdar=16:9'],
                              audio_fps=48000 )
    print "---------------------------"

    # CLEANUP
    print "Performing Cleanup..."
    utilities.write_to_log(log_dir, log_name, 'Cleaning up')
    utilities.cleanup(output_dir,output_file_name_noext)
    utilities.write_to_log(log_dir, log_name, 'Video {0} is complete.'.format(number))
    utilities.write_to_log(log_dir, log_name, '-------------------------------------')

    # PLUS ONE
    c += 1

# Benchmarks
end = datetime.datetime.now()

utilities.write_to_log(log_dir, log_name, 'COMPLETE')
print "----Completed----"
print "Start: %s" % start
print "End: %s" % end
