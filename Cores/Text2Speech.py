import threading
import time

from RealtimeTTS import TextToAudioStream, SystemEngine, AzureEngine, ElevenlabsEngine


class TextToSpeech:
    PLAY = 0
    PAUSE = 1
    RESUME = 2

    def __init__(self):
        system = SystemEngine()  # replace with your TTS engine
        self.engine = TextToAudioStream(system)
        self.state = self.PLAY
        self.interruption = {1: self.pause, 2: self.resume}

    def _say(self, text):
        self.engine.feed(text)
        self.engine.play_async()
        while self.engine.is_playing():
            pass
            # if self.state in self.interruption:
            #     self.interruption[self.state]()


    def say(self, text):
        my_thread = threading.Thread(target=self._say, args=(text,))
        my_thread.start()
        # my_thread.join() # check if this is needed

    def pause(self):
        self.state = self.PAUSE
        self.engine.pause()
        self.state = self.PLAY

    def resume(self):
        self.state = self.RESUME
        self.engine.resume()
        self.state = self.PLAY

    class b:
        pass
        # activate pause


tts = TextToSpeech()
print("hi")
tts.say(
    "Hello world! How are you today? Hello world! How are you today? Hello world! How are you today? Hello world! How are you today?")
print(tts.engine.is_playing())
time.sleep(3)
tts.pause()
print("hi here")
time.sleep(2)
tts.resume()
print("hi final")
