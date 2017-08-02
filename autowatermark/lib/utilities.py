import os,datetime

def cleanup(output_dir,output_name_noext):
    # Remove MOV
    # os.system("rm {0}/*.mov".format(output_dir))
    # Remove MPG
    os.system("rm {0}/*.mpg".format(output_dir))
    # Remove DVD_FOLDERS
    os.system("rm -rf {0}/{1}".format(output_dir,output_name_noext))

def write_to_log(name, text):
    log = open(name + '_log.txt', 'a')
    log_text = "%s ==> %s" % (datetime.datetime.now(), text)
    log.write(log_text)
    log.write("\n")
    log.close()
