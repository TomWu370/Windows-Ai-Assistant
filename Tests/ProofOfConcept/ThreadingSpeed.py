import time
from timeit import Timer

from Cores.Text2Speech import TextToSpeech
from Cores.Notification import Notification
import threading

def nonThread(tts, text):
    tts.say(text)

def thread(tts, text):
    thread = threading.Thread(target=tts.say, args=(text,))
    thread.start()
    thread.join()
tts = TextToSpeech()
start = time.perf_counter_ns()
thread(tts, "Hello world!")
end = time.perf_counter_ns()
tot2 = end - start
start = time.perf_counter_ns()
nonThread(tts, "Hello world!")
end = time.perf_counter_ns()
tot1 = end - start



print("Time for nonThread is: {}".format(tot1))
print("Time for thread is: {}".format(tot2))