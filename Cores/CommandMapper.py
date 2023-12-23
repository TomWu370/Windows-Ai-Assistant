# Strictly Mapping Commands to Functions, with alias, no extra functionalities

# commands should look like this:
# [command, functionHeader, [aliases]]
# functionHeader is also the filename
commandAlias = {}
commandToFunc = {}
def mapCommands(commands):
    commandAlias = {}
    commandToFunc = {}
    for command, func, aliases in commands:
        for alias in aliases:
            commandAlias[alias] = command
        commandToFunc[command] = func
    return commandAlias, commandToFunc

def loadPlugins(commands):
    # sometimes command might conflict with existing commands, warn user after replacing command with plugin
    commandAlias, commandToFunc = mapCommands(commands)
    return commandAlias, commandToFunc


def readCommands():
    for command in commandToFunc.keys():
        print(command)