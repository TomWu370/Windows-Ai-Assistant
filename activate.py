# base script for utilising all the cores
import queue
import subprocess
import sys

from Cores.CommandMapper import CommandMapper
from Cores.Speech2Text import stt
from Cores.Text2Command import TextToCommand
from Cores.Text2Speech import TextToSpeech
import sounddevice as sound
import psutil

if __name__ == '__main__':
    try:
        # need to change path according to where file is run/ use os for absolute path
        commandMapper = CommandMapper()
        text2Command = TextToCommand(commandMapper.commandToFunc)
        speech2Text = stt(model_path="./Cores/modelMedium", language="en-us", log_level=-1)
        text2Speech = TextToSpeech()
        # create a wrapper that wraps all the cores together, then pass as argument, alowing plugins or modules to use
        # called context or something else
        with speech2Text.audio_stream:
            print("#" * 80)
            print("Press Ctrl+C to stop the recording")
            print("#" * 80)

            while True:
                text = speech2Text.get_transcript()
                # the whole match case will be replaced by a single function call to commandMapper
                # match case would then occur inside specific functions, on a small scale
                if text:
                    commands = text2Command.singleCommand(text)
                    print(commands)
                    if commands:
                        for command, args in commands:
                            # when finishing command, it may return a string to be said
                            # may pass the actual context object as argument1, passing by reference
                            resultSpeech = commandMapper.runCommand(command, args)
                            if resultSpeech:
                                text2Speech.say(resultSpeech)

                    text2Speech.say(text)

    except KeyboardInterrupt:
        print("\nDone")
        sys.exit()
    except Exception as e:
        sys.exit(type(e).__name__ + ": " + str(e))