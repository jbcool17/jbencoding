import os

def detection(full_file_name,name_noext):
    scene_detection = "ffmpeg -i %s -filter:v \"select='gt(scene,0.2)',showinfo\" -f null - 2> %s_ffout" % (full_file_name,name_noext)
    os.system(scene_detection)


def parse_timestamps(name_noext):
    parse_timestamps = "grep showinfo %s_ffout | grep pts_time:[0-9.]* -o | grep '[0-9]*\.[0-9]*' -o > %s_timestamps" % (name_noext,name_noext)
    os.system(parse_timestamps)

def set_time(pt, cti, name, ts_num):
    ct = ts_num[cti]
    if (ct - pt) < 30 and (len(ts_num)-1) > cti:
        ct = set_time(pt, (cti+1), name, ts_num)
    # else:
        # print '---time %f set for %s' % (ct, name)

    return ct
