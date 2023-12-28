# Direct Text to Command Module with arguments
# Process text into command, including consumption of arguments


class TextToCommand:
    def __init__(self, commands):
        self.commands = commands
    words = [1, 2, 3]
    capture = ""
    def getCommand(self, text):
        # convert a text into a list of commands
        # however if multi command is not activated, then default to return when first if is broken
        words = text.split(" ")
        captures = []
        wakeup = ""
        argument = ""
        argSearch = False
        # search each word, if in dict, then keep combining until not in dict, then search each word individually
        # combining each word, until a single word is in dict, then append combined word as argument
        # command, command, arg - append both command, because command could have no args
        # command, arg, command - append both command, because command could have no args
        # command, arg, arg - append first command with arg+arg because it's user error that 2 args are present
        # command, arg, command, arg - append both commands
        # args, command, arg - append first command
        # search until word is in dict, then try to combine next words to see if still in dict
        # if not argSearch then abandon current word if not found word in dict
        # this should be done via C++ because of iterations
        # add requirement, first word has to be in command, otherwise it's recognised as normal speech
        # assume 1st word is in commands

        for word in words:
            capture = "".join([capture, word])
            print(f'test: ',capture)

            if " ".join([wakeup, word]).strip() in self.commands:
                wakeup = " ".join([wakeup, word]).strip()
            elif not argSearch:
                wakeup = word
            else:
                argSearch = True
                argument = " ".join([argument, word]).strip()
                if wakeup:
                    captures.append(wakeup)
                    capture = word
                    print(capture)  # return None or token for signaling that there's no command matched
        return captures
