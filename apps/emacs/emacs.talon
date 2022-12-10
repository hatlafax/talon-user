app: emacs
app: Emacs
app: emacs.exe
app: Emacs.exe
-
switch buffer:
    key(ctrl-x)
    key(b)

test action:
    user.test_action()

test buffer:
    insert("hello world")
    key(ctrl-c)

emacs [<user.text>]:
    insert(user.text or "")

#
# <user.letter>        is a list mapping words like 'plex' or 'gust' to latin letters like 'x' or 'g'
# <user.number_string> is a capture mapping words like 'five' to number strings like '5'
# <digits>             is a capture that maps a variable length phrase like "one two three" onto an integer 123
#

key(ctrl-f8): app.notify("f8 key pressed")
