# Tars&Bone

## Help
### Bash
```
# Resolution Ratio Duration
# sh script.sh <resolution> <aspect_ratio> <duration>
$ sh bt_interlaced_ntsc.sh 100x100 16:9 10

# Resolution Rate Ratio Duration
# sh script.sh <resolution> <rate> <aspect_ratio> <duration>
$ sh bt_progressive_all.sh 100x100 23.98 16:9 10

# Sync Video
# Beeps every second
# sh bt_sync.sh 1280x720 23.98 16:9 120
```
### Ruby
```
# generate files using a CSV file
$ ruby btgen.rb formats_progressive.txt bt_progressive.sh
```

## Interlaced Media
### SD
  - 720x486 - 29.97
  - 720x576 - 25*
### HD
  - 1920x1080 - 29.97/60i
  - 1920x1080 - 25/50i*

## Progressive Media
### SD
  - 720x480 - 23.98
  - 720x480 - 29.97
  - 720x480 - 30
  - 720x486 - 23.98
  - 720x486 - 29.97
  - 720x486 - 30
  - 720x576 - 25

### HD
  - 1280x720 - 23.98
  - 1280x720 - 24
  - 1280x720 - 25
  - 1280x720 - 29.97
  - 1280x720 - 30
  - 1280x720 - 50
  - 1280x720 - 59.94
  - 1280x720 - 60

  - 1920x1080 - 23.98
  - 1920x1080 - 24
  - 1920x1080 - 25
  - 1920x1080 - 30(29.97)
  - 1920x1080 - 50
  - 1920x1080 - 60(59.94)

### UHD
  - 2048x1536 - 24
  - 3840x2160 - 60 / 120
  - 4520x2540
  - 4096x3072
  - 7680x4320 - 60 / 120


## Notes
- Possible ruby gem
- Ex. Video without Audio = gen -v -r 1920x1080 29.97 16:9 -d 120 -i(-p)
- Ex. Video with Audio = gen -v -a -r 1920x1080 29.97 16:9 -d 120 -i(-p)

## TODO
- check for commands on start
