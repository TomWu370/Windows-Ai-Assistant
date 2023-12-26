import importlib
import time

func = importlib.import_module("Modules.browser")
if __name__ == '__main__':
    test = "asd"
    print(test[14:-3])
    func.main()

    words = [1, 2, 3]
    capture = ""
    for word in words:
        if " ".join([capture, word]) in dict:
            capture = " ".join([capture, word])
        else:
            print(capture) # return None or token for signaling that there's no command matched
