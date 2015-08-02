# PiLightShow
Christmas lights display driven by a raspebrry pi

I hope to be able to drive 16 sets of lights (channels of lights) with this code, with the option to drive more in the future.

# Usage

sudo python3.2 LightShow.py -l <path to light instructions file>

to start at a specific time in seconds:
sudo python3.2 LightShow.py -l <path to light instructions file> -t 10

# Layout of the 'light instructions file'
the first line shall be the path to the music file
the second line shall be the offset in seconds for when to start the song (don't play the first x seconds of the song)
Every line afterwards has this format:
<time index> <ON or OFF> <which light channels to change>

This will probably change.  After making lights dance for a few seconds, this is really slow going.  Some features I plan to add in the future:
	ability to 'twinkle' a group of lights for specified time
	ability to program a chorus of a song once, and then reuse it 