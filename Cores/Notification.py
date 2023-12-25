import threading

from RealtimeTTS import SystemEngine, TextToAudioStream

from Cores.Text2Speech import TextToSpeech


class Notification(TextToSpeech):

    def __init__(self, tts, voice):
        # initialise TextToSpeech class, to get engine object
        super().__init__(voice)
        self.tts = tts

    def Notify(self, message):
        # interrupts any currently playing tts, then play notification until completion, then resume tts
        self.tts.pause()
        notif_thread = threading.Thread(target=self._say, args=(message,))
        notif_thread.start()
        notif_thread.join()
        self.tts.resume()
        return None

    def Warn(self, message):
        print(message)
        return None

    def Alert(self, message):
        print(message)
        return None

    def pause(self):
        self.tts.pause()

    def resume(self):
        self.tts.resume()