
import typing

from talon import Context, Module, actions
import logging
import winsound
import re
from emacs_porthole import call

mod = Module()

ctx = Context()
ctx.matches = r'''
app: emacs
app: Emacs
app: psimacs
app: Emacs.exe
app: emacs.exe
'''

modifier_keys = {
    "alt"       : "alt",
    "alter"     : "alt",
    "meta"      : "alt",
    "control"   : "ctrl",
    "shift"     : "shift",
    "super"     : "super",
    "hyper"     : "hyper",
}

ctx.lists["self.modifier_key"] = modifier_keys

emacs_command_tokens = dict()

@mod.action_class
class Actions:

    @staticmethod
    def initialize_command_tokens():
        "Initializes the emacs commands tokens"
        global emacs_command_tokens
        logging.info("Hello")
        if len(emacs_command_tokens) == 0:
            result = call(
                "psimacs-porthole-control-server", 
                method="psimacs/config/list-interactive-documented-commands", 
                params=[])

            result = list(set(result))
            result.sort()

            for token in result:
                token = token.replace('-', " ").replace('/', " ").replace('*','')

                tokens = token.split(' ')
                
                for t in tokens:
                    emacs_command_tokens[t.lower()] = t

            logging.info(str(emacs_command_tokens))

    @staticmethod
    def handle_emacs_command(cmd: str):
        "Send the given command to Emacs for execution."
        _ = call(
            "psimacs-porthole-control-server", 
            method="psimacs/config/handle-voice-command", 
            params=[cmd])

    @staticmethod
    def translate_modifier_keys(s: str):
        "Translate Emacs special key word"
        s = s.replace("hyper", "H")
        s = s.replace("super", "s")
        s = s.replace("alt",   "M")
        s = s.replace("meta",  "M")
        s = s.replace("ctrl",  "C")
        s = s.replace("shift", "S")
        return s

    def emacs_prefix_event(N: typing.Optional[int]=None):
        "Send a prefix command to the Emacs command queue."
        cmds = ['C-u']
        if N is not None:
            cmds.append(str(N))

        cmd = " ".join(cmds)
        logging.info("Send prefix command to Emacs: |"+cmd+"|")
        actions.user.handle_emacs_command(cmd)

    def emacs_keyboard_command(keycmd: str):
        "Send a keyboard command to emacs"

        cmd = actions.user.translate_modifier_keys(keycmd)

        logging.info("Send prefix command to Emacs: |"+cmd+"|")
        actions.user.handle_emacs_command(cmd)

    def emacs_start_command_event(cmd: str):
        "Start an Emacs command."

        actions.user.initialize_command_tokens()

        cmd = 'M-x' + " " + cmd.replace(" ", " SPC ")
        cmd = cmd.strip()

        logging.info("Start Emacs command: |"+cmd+"|")

        result = call(
            "psimacs-porthole-control-server", 
            method="psimacs/config/handle-voice-command", 
            params=[cmd])

    def emacs_command_event(cmds: list[str]):
        "Send a command to the Emacs command queue."

        cmd = " ".join(cmds)

        result = call(
            "psimacs-porthole-control-server", 
            method="psimacs/config/handle-voice-command", 
            params=[cmd])

    def emacs_test_command_event(cmd: str, N: typing.Optional[int]):
        "Send a command to the Emacs command queue."

        #cmd = " ".join(cmds)
        logging.info(cmd)
        #result = call(
        #    "psimacs-porthole-control-server", 
        #    method="psimacs/config/handle-voice-test-command", 
        #    params=[cmd])


    def emacs_do_test():
        "Experimenting..."
        result = call(
            "psimacs-porthole-control-server", 
            method="psimacs/config/list-interactive-documented-commands", 
            params=[])

        result = list(set(result))
        result.sort()

        logging.info(result)

    def find_reverse(): "Begins a reverse search."
    def test(s: str) -> str:
        "Mangles the input string in the appropriate manner."
        logging.warning(
            s
        )
        result = call("psimacs-porthole-control-server", method="insert", params=[s])

        return "_+_" + s
    def test_action() -> None:
        "My fancy test action"
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

        actions.list("edit")

    def emacs_log(s: str) -> None:
        "Just log string"
        logging.info(s)
