# !/usr/bin/env python
# python script.py <file_name> <first> <last> <aspect>
import os,sys,numpy,datetime
from moviepy.editor import *
from random import randint
import lib.chapters as chapters
import lib.sdtools as sdtools
import lib.dvdtools as dvdtools
import lib.utilities as utilities

# Benchmarks
start = datetime.datetime.now()

# SETUP VARIABLES
c = 0
first_disc  = int(sys.argv[2])
last_disc   = int(sys.argv[3])
total_discs = last_disc - first_disc

# Video Info
aspect_ratio   = sys.argv[4]
full_file_name = sys.argv[1]
name_noext     = os.path.splitext(full_file_name)[0]
log_name       = name_noext
clip           = VideoFileClip(full_file_name)
duration       = clip.duration
output_dir     = "OUTPUT"
working_dir    = os.popen('pwd').read().strip()

utilities.write_to_log(log_name, 'Starting...')
utilities.write_to_log(log_name, "Video: {0}".format(full_file_name) )
utilities.write_to_log(log_name, "Duration: {0}".format(duration) )
utilities.write_to_log(log_name, "Aspect Ratio: {0}".format(aspect_ratio) )
utilities.write_to_log(log_name, " Videos {0} to {1} will be created.".format(first_disc, last_disc) )

print "Setting up folders..."
os.system("mkdir {0}".format(output_dir))

# ANALYZING VIDEO
# Scene Detection
ffout_log      = name_noext + '_ffout'
timestamps_log = name_noext + '_timestamps'

print "Getting markers and settings times..."
marker_starts = chapters.get_marker_starts(full_file_name)
marker_starts = map(float, marker_starts)
# marker_starts = map(int, marker_starts)

t1 = marker_starts[0]
t2 = marker_starts[1]
t3 = marker_starts[2]
t4 = marker_starts[3]
t5 = marker_starts[4]

utilities.write_to_log(log_name, "Marker1: {0}".format(t1))
utilities.write_to_log(log_name, "Marker2: {0}".format(t2))
utilities.write_to_log(log_name, "Marker3: {0}".format(t3))
utilities.write_to_log(log_name, "Marker4: {0}".format(t4))
utilities.write_to_log(log_name, "Marker5: {0}".format(t5))

# Setting Chapters
print "Setting Chapters..."
chapter1 = chapters.convert_seconds(t1)
chapter2 = chapters.convert_seconds(t2)
chapter3 = chapters.convert_seconds(t3)
chapter4 = chapters.convert_seconds(t4)
chapter5 = chapters.convert_seconds(t5)

utilities.write_to_log(log_name, "Chapter1: {0}".format(chapter1))
utilities.write_to_log(log_name, "Chapter2: {0}".format(chapter2))
utilities.write_to_log(log_name, "Chapter3: {0}".format(chapter3))
utilities.write_to_log(log_name, "Chapter4: {0}".format(chapter4))
utilities.write_to_log(log_name, "Chapter5: {0}".format(chapter5))

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

utilities.write_to_log(log_name, "Marker1 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx1,sly1,blx1,bly1))
utilities.write_to_log(log_name, "Marker2 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx2,sly2,blx2,bly2))
utilities.write_to_log(log_name, "Marker3 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx3,sly3,blx3,bly3))
utilities.write_to_log(log_name, "Marker4 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx4,sly4,blx4,bly4))
utilities.write_to_log(log_name, "Marker5 Positions :: x: {0} - y:{1} - x:{2} - y:{3}".format(slx5,sly5,blx5,bly5))

print "Project variables have been set."
# THE LOOP
# wait 5seconds
sfs = 9
bfs = 30

# Small text duration - may need to be tweeked
strt = .06
print "---------------------------"
while c < (total_discs + 1):
    number            = first_disc + c
    output_name       = "%s_%d.mov" % (name_noext,number)
    output_name_noext = os.path.splitext(output_name)[0]
    utilities.write_to_log(log_name, 'Rendering video with number: {0}'.format(number))
    print "Rendering video with number %d." % number

    # 01 Create TEXT STEP
    # small text 1 frame - pop on
    stc1 = (TextClip(str(number),fontsize=sfs,color='white')
                 .set_pos((slx1, sly1))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc1 = (TextClip(str(number),fontsize=bfs,color='white').set_pos((blx1, bly1))).set_duration(15)

    # 02 Create TEXT STEP
    # small text 1 frame - pop on
    stc2 = (TextClip(str(number),fontsize=sfs,color='white')
                 .set_pos((slx2, sly2))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc2 = (TextClip(str(number),fontsize=bfs,color='white').set_pos((blx2, bly2))).set_duration(15)

    # 03 Create TEXT STEP
    # small text 1 frame - pop on
    stc3 = (TextClip(str(number),fontsize=sfs,color='white')
                 .set_pos((slx3, sly3))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc3 = (TextClip(str(number),fontsize=bfs,color='white').set_pos((blx3, bly3))).set_duration(15)

    # 04 Create TEXT STEP
    # small text 1 frame - pop on
    stc4 = (TextClip(str(number),fontsize=sfs,color='white')
                 .set_pos((slx4, sly4))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc4 = (TextClip(str(number),fontsize=bfs,color='white').set_pos((blx4, bly4))).set_duration(15)

    # 05 Create TEXT STEP
    # small text 1 frame - pop on
    stc5 = (TextClip(str(number),fontsize=sfs,color='white')
                 .set_pos((slx5, sly5))
                 .set_duration(strt))

    # big text 101 - for a duration :15
    btc5 = (TextClip(str(number),fontsize=bfs,color='white').set_pos((blx5, bly5))).set_duration(15)

    # Composite Clips and Text numbers together. Fadein & Fadeout w/crossfade
    # GET START time based scene detection for 5 evenly spaced points
    final_clip = CompositeVideoClip([clip,
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
    final_clip.to_videofile( output_name, codec='prores',
                                          audio_codec='pcm_s16le',
                                          ffmpeg_params=['-vf', 'setdar=16:9'],
                                          audio_fps=48000 )
    print "---------------------------"

    # # DVD
    # print "Generating Mpeg for DVD..."
    # utilities.write_to_log(log_name, 'Encoding MPG')
    # dvdtools.create_mpg(output_name_noext,aspect_ratio)
    #
    # print "---------------------------"
    # print "Moving Files..."
    # # Put into separate Folder ex. TEST_100/
    # move = "mv *%s* %s/" % (output_name_noext,output_dir)
    # os.system(move)
    #
    # # CREATE DVD/ISO
    # utilities.write_to_log(log_name, 'Creating DVD...')
    # print "---------------------------"
    # print "Creating DVD..."
    # dvdtools.create_dvd(chapters, output_dir, output_name_noext)
    #
    # utilities.write_to_log(log_name, 'Creating ISO...')
    # print "Creating ISO..."
    # dvdtools.create_iso(output_dir, output_name_noext)
    #
    # CLEANUP
    print "Performing Cleanup..."
    utilities.write_to_log(log_name, 'Cleaning up')
    utilities.cleanup(output_dir,output_name_noext)
    utilities.write_to_log(log_name, 'Video {0} is complete.'.format(number))
    utilities.write_to_log(log_name, '-------------------------------------')

    # PLUS ONE
    c += 1

# Benchmarks
end = datetime.datetime.now()

utilities.write_to_log(log_name, 'COMPLETE')
print "----Completed----"
print "Start: %s" % start
print "End: %s" % end
