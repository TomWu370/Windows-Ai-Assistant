# Direct Text to Command Module with arguments
# Process text into command, including consumption of arguments


class TextToCommand:
    def __init__(self, commands):
        self.commands = commands
    words = [1, 2, 3]
    capture = ""

    def singleCommand(self, text):
        if text[0] in self.commands:
            return [text[0], text[1:]]
        else:
            return []

    def singleMultiWordCommand(self, text):
        pass
        '''std::vector<std::string> func(const std::string& input, const std::unordered_map<std::string, int>& myMap) {
    std::vector<std::string> result = {"", ""};
    std::istringstream iss(input);
    std::vector<std::string> words;
    std::string word;

    while (iss >> word) {
        words.push_back(word);
    }


    for (int i = words.size(); i >= 0; i--) {
        std::vector<std::string> wordsUpToWord(words.begin(), words.begin()+i);
        std::string wordsUpToStr = "";
        for (const auto& w : wordsUpToWord) {
            wordsUpToStr += w + " ";
        }
        if (!wordsUpToStr.empty()) {
            wordsUpToStr = wordsUpToStr.substr(0, wordsUpToStr.length() - 1);
        }
        // cout << wordsUpToStr;
        // auto test = myMap.find(wordsUpToStr);
        // cout << (myMap.find(wordsUpToStr) != myMap.end());
        if (myMap.find(wordsUpToStr) != myMap.end()) {
            std::vector<std::string> wordsAfterI(words.begin() + i, words.end());
            std::string wordsAfterStr = "";
            for (const auto& w : wordsAfterI) {
                wordsAfterStr += w + " ";
            }

            result[0] = wordsUpToStr;
            result[1] = wordsAfterStr;
            return result;
        }
    }


    return result;
}

int main() {
    std::unordered_map<std::string, int> myMap = {{"hi", 1}, {"hello", 2}, {"helloworld", 3}, {"hello i am you", 4}};;

    // Test cases
    auto result1 = func("hellow", myMap);
    std::cout << "Case 1: " << result1[0] << ", " << result1[1] << std::endl;

    auto result2 = func("hello w", myMap);
    std::cout << "Case 2: " << result2[0] << ", " << result2[1] << std::endl;

    auto result3 = func("asd hi", myMap);
    std::cout << "Case 3: " << result3[0] << ", " << result3[1] << std::endl;

    auto result4 = func("hello i am you next hello", myMap);
    std::cout << "Case 4: " << result4[0] << ", " << result4[1] << std::endl;


    return 0;
}'''

    def multiSingleWordCommand(self, text):
        pass

    def multiLMultiWordCommand(self, text):
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
