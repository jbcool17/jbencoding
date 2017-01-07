# FFMPEG w/Docker Container

```
# Install docker

# Get FFMPEG Container
$ docker pull jrottenberg/ffmpeg

# Run file locally
$ docker run --rm -v `pwd`:/tmp/workdir -w="/tmp/workdir" jrottenberg/ffmpeg -i audio.wav -ab 192k audio.mp3
```
