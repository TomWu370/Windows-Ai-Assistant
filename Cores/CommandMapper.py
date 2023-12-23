# Strictly Mapping Commands to Functions, with alias, no extra functionalities
# commands should look like this:
# [command, functionHeader, [aliases]]
# functionHeader is also the filename, use importlib to import a string name
import importlib

commandAlias = {}
commandToFunc = {}

def mapCommands(commands, pathHeader = "Modules."):
    for command, func, aliases in commands:
        for alias in aliases:
            commandAlias[alias] = command
        # might have issues with importing from different directories, therefore might need to use absolute path
        commandToFunc[command] = importlib.import_module(pathHeader + func)
    return commandAlias, commandToFunc

def loadPlugins(commands):
    # sometimes command might conflict with existing commands, warn user after replacing command with plugin
    return mapCommands(commands, "Plugins.")

def readCommands():
    for command in commandToFunc.keys():
        print(command)