# !/usr/bin/env python

import re,os,datetime

def get_marker_starts(file="TEST-Markers.mov"):
  output = []
  arr = os.popen("ffmpeg -i {0} 2>&1 | grep Chapter".format(file)).read().split('\n')
  arr = map(str.strip,arr)
  arr.pop()

  for line in arr:
    stime = re.findall(r'\d+\.\d+|\d+', line)[2]
    output.append(stime)
    # print stime

  return output


# BASH
# SOURCE="TEST-Markers"
# EXT="mov"
# ffmpeg -i "$SOURCE.$EXT" 2>&1 | grep Chapter | sed -E "s/ *Chapter #([0-9]+\.[0-9]+): start ([0-9]+\.[0-9]+), end \
# ([0-9]+\.[0-9]+)/-i \"$SOURCE.$EXT\" -vcodec copy -acodec copy -ss \2 -to \3 \"$SOURCE-\1.$EXT\"/" | xargs -n 11 ffmpeg

def convert_seconds(s):
    return str(datetime.timedelta(seconds=s))
