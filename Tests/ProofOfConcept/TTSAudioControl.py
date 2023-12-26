import threading
import pyttsx3
import time
from RealtimeTTS import TextToAudioStream, SystemEngine, AzureEngine, ElevenlabsEngine

from Cores.Text2Speech import TextToSpeech
from Cores.Notification import Notification

tts = TextToSpeech("Zira")
notif = Notification(tts, "David")
print("hi")
text = "Hello world! How are you today? Hello world! How are you today? Hello world! How are you today? Hello world!"
tts.say(text)
time.sleep(2)
notif.Notify("Hi, this is me, and this is your world")