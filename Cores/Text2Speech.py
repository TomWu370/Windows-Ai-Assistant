import threading
import time

from RealtimeTTS import TextToAudioStream, SystemEngine, AzureEngine, ElevenlabsEngine


class TextToSpeech:
    def __init__(self, voice):
        self.voice = voice
        system = SystemEngine(voice=voice, print_installed_voices=True)  # replace with your TTS engine
        self.engine = TextToAudioStream(system)

    def _say(self, text):
        print(self.voice)
        self.engine.engine.set_voice(self.voice)
        self.engine.feed(text)
        self.engine.play()
        # while self.engine.is_playing(): will only work with Notification interruption when using play_async
        # otherwise using play() without while self.engine.is_playing() will work


    def say(self, text):
        threading.Thread(target=self._say, args=(text,)).start()
        # my_thread.join() # not needed because it locks until completion, needed for Notification interruption

    def pause(self):
        self.engine.pause()

    def resume(self):
        self.engine.resume()
    def test(self):
        print("at test")

    class b:
        pass
        # activate pause


# tts = TextToSpeech("a")
# print("hi")
# tts.say("Hello world! How are you today?")
# print(tts.engine.is_playing())
# time.sleep(3)
# tts.pause()
# print("hi here")
# time.sleep(5)
# tts.resume()
# print("hi final")
