import time

import psutil as psutil
import pvcheetah
import pyaudio
import numpy as np
import sounddevice
import subprocess
import sys
from vosk import Model, KaldiRecognizer, SetLogLevel
import queue
import argparse
import os


class stt:

    def __init__(self, model_path, language="en-us", log_level=-1):
        SetLogLevel(log_level)  # -1 only log errors/warnings
        device_info = sounddevice.query_devices(1, "input")  # 0 is microsoft sound mapper
        self.device = device_info['index']
        self.samplerate = int(device_info["default_samplerate"] * 4)  # 44100 * 4 = 176400
        self.model = Model(model_path, lang=language)
        self.rec = KaldiRecognizer(self.model, self.samplerate)
        self.sound_buffer = queue.Queue()
        self.audio_stream = sounddevice.RawInputStream(
            samplerate=self.samplerate,
            blocksize=8000,
            device=self.device,
            dtype="int16",
            channels=1,
            callback=self.callback)

    def get_transcript(self):
        if not self.sound_buffer.empty() and self.rec.AcceptWaveform(self.sound_buffer.get()):
            # efficient way to convert json into string
            result = self.rec.Result()[14:-3]
            # remove ghost the from string, 0.21 might fix
            result = result.lower() if result[0:4].strip() != 'the' else result[4:]
            return result
        else:
            return ""

    def callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.sound_buffer.put(bytes(indata))


if __name__ == '__main__':
    try:

        # need to change path according to where file is run/ use os for absolute path
        speech2Text = stt(model_path="./modelMedium", language="en-us", log_level=-1)
        with speech2Text.audio_stream:
            print("#" * 80)
            print("Press Ctrl+C to stop the recording")
            print("#" * 80)

            while True:
                text = speech2Text.get_transcript()
                # the whole match case will be replaced by a single function call to commandMapper
                # match case would then occur inside specific functions, on a small scale
                if text:
                    match text:
                        case "open notepad" | 'open note pad':
                            subprocess.Popen('notepad.exe')
                            print("opening")
                        case "close notepad" | 'close note pad':
                            for proc in psutil.process_iter():
                                # check whether the process name matches
                                print("killing")
                                if proc.name() == "notepad.exe":
                                    proc.kill()
                                    break
                        case "terminate all notepad":
                            for proc in psutil.process_iter():
                                # check whether the process name matches
                                print("terminating")
                                if proc.name() == "notepad.exe":
                                    proc.kill()
                        case _:
                            print(text)

    except KeyboardInterrupt:
        print("\nDone")
        sys.exit()
