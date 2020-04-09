#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import snowboydecoder
import sys
import signal
import time
#from pixels import Pixels
from call_assistant import main

'''
Follow up of the word done here:
https://www.sigmdel.ca/michel/ha/rpi/voice_rec_02_en.html

This demo is based on the following shared file:
https://www.sigmdel.ca/michel/ha/rpi/dnld/sbdemo7.py

The problem described on their website (and file) shared above
was that they did not terminate the detector before invoking
the Google Assistant. Of course Google Assistant has its own
issues, which I resolve here:
https://glrs.github.io/2019-12-17-ga_sdk-voice_rec-RasPi/

I do not use pixels, but I have just comment it out so you
can just uncomment it if you want to use it.

Last modified: 17-12-2019
Github: @glrs
'''

# default parameters that can be changed with command line parameters

### Change with your own trained Snowboy model
SnowboyModel = 'resources/models/snowboy.umdl'
sleepTime      = 0.03
detectedSignal = 3     # 0 - nothing, 1 - print yes..., 2 + flash pixels, 3 + play DING

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(SnowboyModel, sensitivity=0.5)

def detectedCallback():
    if detectedSignal > 2:
        print('signal more 2')
        snowboydecoder.play_audio_file()
    if detectedSignal > 1:
        print('signal more 1')
        #pixels.listen()
        pass
    if detectedSignal > 0:    
        #print('yes...', end='', flush=True)
        print('yes more 0')

    detector.terminate() # Terminate detector before calling main
    main(verbose=True) # in googlesamples.assistant.grpc.talkassist
    detector.restart()
    print('\nListening... Press Ctrl+C to exit 2')
 
#pixels = Pixels() 
print('Listening... Press Ctrl+C to exit 1')

# main loop
while True:
    detector.start(detected_callback=detectedCallback,
               interrupt_check=interrupt_callback,
               sleep_time=sleepTime)

detector.terminate()
#pixels.off()
time.sleep(1)