file_to_compile = "main.sus"
compiled_file = "comp.py"

line_list = []


#Equivalents
print_ = "imprime "


with open(file_to_compile, "r") as file:
    for line in file:
        line_list.append(line)


with open(compiled_file, "a") as file:
    for line in line_list:

        if line[:len(print_)] == print_:
            args = line[len(print_):]
            file.write(f"print({args})")