# SingleVideo Sequential Watermarker
- processes a single video with sequential numbers placed randomly throughout video
- Not yet fully operational - might run into a few bugs on different systems

## Requirements / Notes
- moviepy
- ffmpeg
- imagemagick
- Marker positions found in log

## Auto / Manual
- auto script automatically finds the markers in the video
- manual script pulls the chapter markers created by final cut pro

## Usage

```
$ python final_full_auto.py TESTCLIP.mov <START> <END>
$ python final_full_auto.py TESTCLIP.mov 0 3
```
