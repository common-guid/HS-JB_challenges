"""
Implement the help function (!help) that will print available syntax commands, which we have indicated above,
    as well as the special commands. When called, it should print the following:

Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done
Implement the exit function (!done) that exits the editor without saving.

Ask a user for input: Choose a formatter:.

If the input contains one of the correct formatters (plain, bold, italic, etc.), ask for the input once again.
If the input contains no formatters or unknown command is sent, print the following message and ask for input again: Unknown formatting type or command.
If the input contains !help, print the list of available commands, as shown in the example below. If the input contains !done, exit the editor without saving.
"""
while True:
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
  #  if user in ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
  #                  "new-line", "!help", "!done"]:
  #      print("Unknown formatting type or command")