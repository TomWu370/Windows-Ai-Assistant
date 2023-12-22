import time

import psutil as psutil
import pvcheetah
import pyaudio
import numpy as np
import sounddevice as sd
import subprocess
import sys
from vosk import Model, KaldiRecognizer, SetLogLevel
import queue
import argparse
import os

class stt:
    cheetahAPI = ""
    handle = None
    audio_stream = None

    def __init__(self, api, pause_duration=0.5):
        self.cheetagAPI = "xUXq9Qp9l+VEivo6nq8217aVEHjW4469z3fY/pHZVJnigZRrLLF2YQ=="
        self.handle = pvcheetah.create(access_key=api, endpoint_duration_sec=0.5)
        self.audio_stream = pyaudio.PyAudio().open(
            rate=self.handle.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.handle.frame_length
        )

    def get_handle(self):
        return self.handle

    def get_next_audio_frame(self, frame_length):
        return np.frombuffer(self.audio_stream.read(frame_length), np.int16)

    def get_partial_transcript(self):
        return self.handle.process(self.get_next_audio_frame(self.handle.frame_length))

    def flush(self):
        return self.handle.flush()



if __name__ == '__main__':

    q = queue.Queue()


    def int_or_str(text):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text


    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))


    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-l", "--list-devices", action="store_true",
        help="show list of audio devices and exit")
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        "-f", "--filename", type=str, metavar="FILENAME",
        help="audio file to store recording to")
    parser.add_argument(
        "-d", "--device", type=int_or_str,
        help="input device (numeric ID or substring)")
    parser.add_argument(
        "-r", "--samplerate", type=int, help="sampling rate")
    parser.add_argument(
        "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
    args = parser.parse_args(remaining)
    print(sd.query_devices(args.device, "input"))
    try:
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, "input")
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info["default_samplerate"]*4)
            print(device_info['default_samplerate'])

        if args.model is None:
            model = Model('./modelMedium',lang="en-us")
        else:
            model = Model(lang=args.model)

        if args.filename:
            dump_fn = open(args.filename, "wb")
        else:
            dump_fn = None

        with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device,
                               dtype="int16", channels=1, callback=callback):
            print("#" * 80)
            print("Press Ctrl+C to stop the recording")
            print("#" * 80)

            rec = KaldiRecognizer(model, args.samplerate)

            while True:
                start = time.time()
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = rec.Result()[14:-3]
                    match result:
                        case "open notepad":
                            end = time.time()
                            subprocess.Popen('notepad.exe')
                            print("opening")
                            print(end - start)
                        case "close notepad":
                            for proc in psutil.process_iter():
                                # check whether the process name matches
                                if proc.name() == "notepad.exe":
                                    proc.kill()
                                    break
                        case "terminate all notepad":
                            for proc in psutil.process_iter():
                                # check whether the process name matches
                                if proc.name() == "notepad.exe":
                                    proc.kill()
                        case "":
                            pass
                        case _:
                            print(result)





                if dump_fn is not None:
                    dump_fn.write(data)

    except KeyboardInterrupt:
        print("\nDone")
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ": " + str(e))