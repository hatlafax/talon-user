
from talon import Context, Module, actions
import logging
import winsound

mod = Module()

ctx = Context()
ctx.matches = r'''
app: emacs
app: Emacs
app: psimacs
app: Emacs.exe
app: emacs.exe
'''

@mod.action_class
class Actions:
    def find_reverse(): "Begins a reverse search."
    def test(s: str) -> str:
        "Mangles the input string in the appropriate manner."
        logging.warning(
            'bla'
        )

        return "_+_" + s
    def test_action() -> None:
        "My fancy test action"
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

        actions.list("edit")
