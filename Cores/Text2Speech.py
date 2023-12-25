import threading
import time

from RealtimeTTS import TextToAudioStream, SystemEngine, AzureEngine, ElevenlabsEngine


class TextToSpeech:
    def __init__(self):
        system = SystemEngine()  # replace with your TTS engine
        self.engine = TextToAudioStream(system)

    def _say(self, text):
        self.engine.feed(text)
        self.engine.play()
        # while self.engine.is_playing(): will only work with Notification interruption when using play_async
        # otherwise using play() without while self.engine.is_playing() will work


    def say(self, text):
        my_thread = threading.Thread(target=self._say, args=(text,))
        my_thread.start()
        # my_thread.join() # check if this is needed

    def pause(self):
        self.engine.pause()

    def resume(self):
        self.engine.resume()

    class b:
        pass
        # activate pause


tts = TextToSpeech()
print("hi")
#tts.say("Hello world! How are you today? Hello world! How are you today? Hello world! How are you today? Hello world! How are you today?")
print(tts.engine.is_playing())
time.sleep(3)
tts.pause()
print("hi here")
time.sleep(10)
tts.resume()
print("hi final")
