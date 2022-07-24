"""
Implement a separate function for each of the formatters. It will keep your code structured. With functions,
you will also be able to find and fix a bug with ease if something is wrong.

The program should work in the following way:

Ask a user to input a formatter.
If the formatter doesn't exist, print the following error message: Unknown formatting type or command.
Ask a user to input a text that will be applied to the formatter: Text: <user's input>.
Save the text with the chosen formatter applied to it and print the markdown.
Each time you should print out the whole text in markdown accumulated so far.
"""
def bold():
    t = input("Text: ")
    out = f"**{t}**"
    return out

def ital():
    t = input("Text: ")
    out = f"*{t}*"
    return out

def header():
    cont = 'y'
    while cont == 'y':
        level = int(input("Level: "))
        if level in range(1,7):
            cont = 'n'
            text = input("Text: ")
            m = "#"*level
            out = f"{m} {text}\n"
            cont = 'n'
        else:
            print("The level should be within the range of 1 to 6")
            out = ""
    return out

def link():
    l = input("Label: ")
    url = input("URL: ")
    out = f"[{l}]({url})"
    return out

def inline():
    t = input("Text: ")
    out = f"`{t}`"
    return out

def line():
    out = "new"
    return out


def main():
    match choice:
        case "bold":
            user = bold()
        case "italic":
            user = ital()
        case "header":
            user = header()
        case "link":
            user = link()
        case "inline-code":
            user = inline()
        case "new-line":
            user = line()
        case "plain":
            user = input("Text: ")
        case default:
            user = ""
    return user

if __name__ == '__main__':
    msg = "Available formatters: plain bold italic header link inline-code new-line\nSpecial commands: !help !done"
    final = ""
    while True:
        choice = input("Choose a formatter")
        if choice == '!done':
            break
        elif choice == '!help':
            print(msg)
        elif choice not in ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "!help", "!done"]:
            print("Unknown formatting type or command")
        else:
            user = main()
            if user != 'new':
                final = final + user
                print(final)
            elif user == "":
                print(final)
            else:
                final = f"{final}\n"
                print(final)

"""
        user = input("Choose a formatter:")
        msg = "Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\nSpecial commands: !help !done"

        if user in ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]:
            pass
        elif user == "!help":
            print(msg)
        elif user == "!done":
            break
        else:
            print("Unknown formatting type or command")
"""
