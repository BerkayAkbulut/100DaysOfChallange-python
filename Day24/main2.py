

with open("my_file.txt", mode="w+r") as file:
    content=file.read()
    file.write("How are you?")
    print(file,"-",content)
