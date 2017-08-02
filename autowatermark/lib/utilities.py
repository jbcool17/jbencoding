import os,datetime

def cleanup(output_dir,output_name_noext):
    os.system("rm *.wav")


def write_to_log(log_dir, name, text):
    log = open(log_dir + '/' + name + '_log.txt', 'a')
    log_text = "%s ==> %s" % (datetime.datetime.now(), text)
    log.write(log_text)
    log.write("\n")
    log.close()
