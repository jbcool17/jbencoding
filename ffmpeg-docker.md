# FFMPEG w/Docker Container

```
# Install docker

# Get FFMPEG Container
$ docker pull jrottenberg/ffmpeg

# Run file locally
$ docker run --rm -v `pwd`:/tmp/workdir -w="/tmp/workdir" jrottenberg/ffmpeg -i audio.wav -ab 192k audio.mp3
```


docker service create --replicas 1 --rm -v `pwd`:/tmp/workdir -w="/tmp/workdir" jrottenberg/ffmpeg -i audio.wav -ab 192k audio.mp3


def execute_ffmpeg(cmd)

  command = "#{cmd} 2>&1"
  progress = nil
  frames = nil
  fps = 25
  ffmpeg = IO.popen(command)
  ffmpeg.each("\r") do |line|
    if frames.nil? && line =~ /Duration:(\s.?(\d*):(\d*):(\d*\.\d*))/
      duration = $2.to_s + ":" + $3.to_s + ":" + $4.to_s
      frames = ($4.to_i + ($3.to_i * 60) + ($2.to_i * 60 * 60)) * fps
    end
    if line =~ /frame=(\s.?(\d*))/
      progress = $1.to_i / frames.to_i
      print "Progress: #{progress}"
    end
  end
end


ssh vagrant@192.168.56.110 docker run --rm -v `pwd`:/tmp/workdir -w="/tmp/workdir" jrottenberg/ffmpeg -f lavfi -i testsrc=duration=10:size=1280x720:rate=30 testsrc4.mpg && scp vagrant@192.168.56.110:`pwd`/testsrc4.mpg .

ssh vagrant@192.168.56.110 docker run --rm -v `pwd`:/tmp/workdir -w="/tmp/workdir" jrottenberg/ffmpeg -f lavfi -i testsrc=duration=10:size=1280x720:rate=30 testsrc7.mpg &&

ssh vagrant@192.168.56.110 cp -pvr `pwd`/testsrc7.mpg /home/vagrant/


#NODE 1
- setup ssh keys
ssh vagrant@192.168.56.111 "docker run --rm -v `pwd`:/tmp/workdir -w="/tmp/workdir" jrottenberg/ffmpeg -f lavfi -i testsrc=duration=10:size=1280x720:rate=30 testsrc.mpg"

ssh vagrant@192.168.56.111 "docker run --rm -v `pwd`:/tmp/workdir -w="/tmp/workdir" jrottenberg/ffmpeg -i testsrc.mpg testsrc.mov"

# SSH
ssh = Net::SSH.start('192.168.56.111', 'vagrant', :password => "vagrant")
ssh.exec!("hostname")
ssh.exec!("ls")
ssh.exec!("docker run --rm -v `pwd`:/tmp/workdir -w=\"/tmp/workdir\" jrottenberg/ffmpeg -f lavfi -i testsrc=duration=10:size=1280x720:rate=30 testsrc10.mpg")

https://github.com/net-ssh/net-ssh
