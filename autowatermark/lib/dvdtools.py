import os

def create_mpg(output_name_noext,aspect_ratio):
    dvd = "ffmpeg -v quiet -stats -i %s.mov -aspect %s -target ntsc-dvd %s.mpg" % (output_name_noext,aspect_ratio,output_name_noext)
    os.system(dvd)

def create_dvd(chapters, output_dir, output_name_noext):
    os.system("export VIDEO_FORMAT=\"ntsc\"")
    create_dvd_folders = "dvdauthor -t -c %s -o %s/%s %s/%s.mpg" % (chapters,output_dir,output_name_noext,output_dir,output_name_noext)
    set_default_ntsc = "dvdauthor -o %s/%s -T" % (output_dir,output_name_noext)
    os.system(create_dvd_folders)
    os.system(set_default_ntsc)

def create_iso(output_dir, output_name_noext):
    make_iso = "hdiutil makehybrid -udf -udf-volume-name DVD -o %s/%s.iso %s/%s/" % (output_dir,output_name_noext,output_dir,output_name_noext)
    os.system(make_iso)
