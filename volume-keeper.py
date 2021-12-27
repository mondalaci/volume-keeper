#!/usr/bin/env python3
import time
import alsaaudio

while True:
    try:
        mixer = alsaaudio.Mixer('PCM', cardindex=2)
    except alsaaudio.ALSAAudioError:
        pass
    else:
        mixer.setvolume(100, alsaaudio.MIXER_CHANNEL_ALL)
    time.sleep(1)
