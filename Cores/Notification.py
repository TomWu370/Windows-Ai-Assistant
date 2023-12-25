



class Notification:

    def __init__(self, tts):
        self.tts = tts


    def Notify(self, message):
        print(message)
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

