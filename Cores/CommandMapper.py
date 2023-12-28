# Strictly Mapping Commands to Functions, with alias, no extra functionalities
# commands should look like this:
# [command, functionHeader, [aliases]]
# functionHeader is also the filename, use importlib to import a string name
import importlib


class CommandMapper:

    def __init__(self):
        self.commandAlias = {}
        self.commandToFunc = {}
        self.mapCommands(self.getCommands())

    def getCommands(self):
        # read commands from file
        return [["openCommand", "open", ["open", "moveto"]], ["pause", "pause", ["p"]], ["resume", "resume", ["r"]]]

    def mapCommands(self, commands, pathHeader="Modules."):
        for command, func, aliases in commands:
            print(f'command: {command}, func: {func}, aliases: {aliases}')
            for alias in aliases:
                self.commandAlias[alias] = command
            # might have issues with importing from different directories, therefore might need to use absolute path
            self.commandToFunc[command] = importlib.import_module(pathHeader + func)
            break
        return None

    def loadPlugins(self, commands):
        # sometimes command might conflict with existing commands, warn user after replacing command with plugin
        return self.mapCommands(commands, "Plugins.")

    def readCommands(self):
        for command in self.commandToFunc.keys():
            print(command)


if __name__ == '__main__':
    commandMapper = CommandMapper()
    commandMapper.commandToFunc["openCommand"].launch('notepad')
    commandMapper.commandToFunc["openCommand"].launch('notepad')