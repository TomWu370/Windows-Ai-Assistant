# base script for utilising all the cores
import queue
import subprocess
import sys

from Cores.CommandMapper import CommandMapper
from Cores.Speech2Text import stt
from Cores.Text2Speech import TextToSpeech
import sounddevice as sound
import psutil

if __name__ == '__main__':
    try:
        # need to change path according to where file is run/ use os for absolute path
        commands = CommandMapper()
        speech2Text = stt(model_path="./Cores/modelMedium", language="en-us", log_level=-1)
        text2Speech = TextToSpeech()
        with speech2Text.audio_stream:
            print("#" * 80)
            print("Press Ctrl+C to stop the recording")
            print("#" * 80)

            while True:
                text = speech2Text.get_transcript()
                # the whole match case will be replaced by a single function call to commandMapper
                # match case would then occur inside specific functions, on a small scale
                if text:
                    text2Speech.say(text)

    except KeyboardInterrupt:
        print("\nDone")
        sys.exit()
    except Exception as e:
        sys.exit(type(e).__name__ + ": " + str(e))