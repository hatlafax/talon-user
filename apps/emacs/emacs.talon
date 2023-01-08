app: emacs
app: Emacs
app: psimacs
app: emacs.exe
app: Emacs.exe
-

#
# Short forms
#

#
# ...basics
#
<user.modifiers> <user.unmodified_key>:
    user.emacs_keyboard_command("{modifiers}-{unmodified_key}")

prefix:
    user.emacs_prefix_event()

prefix <number_signed>:
    user.emacs_prefix_event(number_signed)



switch buffer:
    key(ctrl-x)
    key(b)

execute [<user.text>]$:
    user.emacs_start_command_event(user.text or "")

emacs do test:
    user.emacs_do_test()


#   Quitting
(quit  | cancel): user.emacs_keyboard_command("ctrl-g")
(reset | rescue): user.emacs_keyboard_command("esc esc esc")

undo: user.emacs_keyboard_command("ctrl-z")
redo: user.emacs_keyboard_command("ctrl-shift-z")
redo all: user.emacs_keyboard_command("super-ctrl-z")

key <user.modifiers> <user.unmodified_key>+:
    user.emacs_key("{modifiers}-{unmodified_key_list}")

work <user.word>:
    user.test(user.word)

test action:
    user.test_action()

test key:
    insert("x")
    key(option-x)


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
