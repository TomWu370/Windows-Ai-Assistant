def split_string_into_commands(s, d):
    result = []
    words = s.split()
    if words[0] not in d:
        return result
    current_command = words[0]
    current_arg = ""
    i = 1
    argSearch = False
    for word in words[1:]:
        if not argSearch:
            if " ".join([current_command, word]).strip() in d:
                current_command = " ".join([current_command, word]).strip()
                continue

            else:
                argSearch = True
                current_arg = ""
                if not word in d:
                    current_arg = word
                else:
                    result.append([current_command, current_arg])
                    current_command = word
                    argSearch = False
        else:
            if word in d:
                result.append([current_command, current_arg])
                current_command = word
                argSearch = False
            else:
                print(current_arg)
                current_arg = " ".join([current_arg, word]).strip()
    else:
        if current_command and current_arg:
            result.append([current_command, current_arg])
    print(current_command)
    print(argSearch)
    # problem, multi is not recognised as in multi word command
    # therefore multi word has to be based on existing commands
    print(current_arg)

    return result

# Example usage:
command_dict = {'print', 'echo', 'run', 'multi word command', 'multi', 'multi word'}
input_string = 'print Hello World echo OpenAI run GPT-3 multi word command hi multi word test'
output = split_string_into_commands(input_string, command_dict)
print(output)