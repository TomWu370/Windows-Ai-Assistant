import time

from RealtimeTTS import TextToAudioStream, SystemEngine, AzureEngine, ElevenlabsEngine

engine = SystemEngine() # replace with your TTS engine
stream = TextToAudioStream(engine)
print("hi")
stream.feed("Hello world! How are you today?")
stream.play_async()
while stream.is_playing():
    time.sleep(0.4)
    stream.pause()
    time.sleep(0.4)
    stream.resume()

