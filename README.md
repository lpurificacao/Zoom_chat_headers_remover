
<img align="right" src="python_logo/python-logo@2x.png">

${\huge{\textsf{\textcolor{#0A1589}{Zoom chat headers remover}}}}$

Zoom allows us to save the chat of a meeting onto a text file.

It creates for every chat a structure with a folder named with the timestamp.

As you keep saving chats, this structure will grow.

However, we find headers in those text files that make the reading troublesome.

${\large{\textsf{\textcolor{#0A1589}{What does it do?}}}}$

The 'zoom_header_remover.py' script goes through that structure of folders and files to find the most recent chat based on its modification timestamp.

Once it's found, it removes those headers as well as emojis for you.

An output file ${\textbf{\textsf{\textcolor{ProcessBlue}{'last_chat_cleared_of_headers.txt'}}}}$ is created for you.

${\large{\textsf{\textcolor{#0A1589}{How to use it?}}}}$

1. Install the emoji module with "pip install emoji"
2. Just copy the script to the directory where you want to create your Python project.
3. Run it from your shell or IDE. That's it.


${\large{\textsf{\textcolor{#0A1589}{Suggestion}}}}$

Get to the repository 'Python_setup' and copy that script.

It creates the virtual environment and installs the emoji module for you.

You can then copy the 'zoom_header_remover.py' and run it from there.

