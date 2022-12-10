from talon import  Module, actions, registry
import sys, os

def list_to_markdown_table(file, list_name):

    file.write(f"# {list_name} \n\n")
    command_list = registry.lists[list_name][0].items()
    file.write(f">\n")
    file.write(f"> command word  {list_name}   \n\n")
    for key, value in command_list:
        file.write( "> **" + key + "** *" + value + "*\n>\n")

    file.write("\n\n")

def write_alphabet(file):
    list_to_markdown_table(file, 'user.letter')

def write_numbers(file):
    list_to_markdown_table(file, 'user.number_key')

def write_modifiers(file):
    list_to_markdown_table(file, 'user.modifier_key')

def write_special(file):
    list_to_markdown_table(file, 'user.special_key')

def write_symbol(file):
    list_to_markdown_table(file, 'user.symbol_key')

def write_arrow(file):
    list_to_markdown_table(file, 'user.arrow_key')

def write_punctuation(file):
    list_to_markdown_table(file, 'user.punctuation')

def write_function(file):
    list_to_markdown_table(file, 'user.function_key')

def write_formatters(file):
    file.write(f"# formatters \n\n")
    command_list = registry.lists['user.formatters'][0].items()
    file.write("> command word  user.formatters  \n")
#    file.write("|------|-----|\n")
    for key, value in command_list:
        file.write( "> **"+ key + "** `" + actions.user.formatted_text(f"example of formatting with {key}", key) + "` \n>\n")

def write_context_commands(file, commands): 
    # write out each command and it's implementation
    for key in commands:
        try:
            rule = commands[key].rule.rule

            file.write("\n - **" + rule + "**\n")

            implementation = commands[key].target.code
            l = implementation.split('\n')
            for s in l:
                if not s.startswith('#') and len(s) > 0:
                    file.write(f"- *{s}*\n")
        except Exception:
            continue

def pretty_print_context_name(file, name):
    ## The logic here is intended to only print from talon files that have actual voice commands.  
        splits = name.split(".")
        index = -1
        
        os = ""
        
        if "mac" in name:
            os = "mac"
        if "win" in name: 
            os = "win"
        if "linux" in name:
            os = "linux"

        if "talon" in splits[index]:
            index = -2
            short_name = splits[index].replace("_", " ")
        else:
            short_name = splits[index].replace("_", " ")

        if "mac" == short_name or "win" == short_name or "linux" == short_name:
            index = index - 1
            short_name = splits[index].replace("_", " ")

        file.write("\n\n\n" + "# " + os + " " + short_name + "\n\n")


def write_org_preamble(file):
    file.write(":PROPERTIES:" + "\n")
    file.write(":ID:       8a1f85d9-e1bc-4c88-b15e-5dcab581f0a2" + "\n")
    file.write(":END:" + "\n")
    file.write("#+title: Talon Cheatsheet" + "\n")
    file.write("\n")
    file.write("#+exclude_tags: noexport" + "\n")
    file.write("\n")
    file.write("#+include: ../../OptionsPreamble.org" + "\n")
    file.write("#+include: ../../LatexPreamble.org" + "\n")
    file.write("#+include: ../../HtmlPreamble.org" + "\n")
    file.write("#+include: ../../ThemeDakrone.org" + "\n")
    file.write("\n")
    file.write(r"#+latex_header: \shorttitle{}" + "\n")
    file.write(r"#+latex_header: \abstract{}" + "\n")
    file.write(r"#+latex_header: \keywords{}" + "\n")
    file.write("\n")
    file.write(r"#+latex_header: \DeclareUnicodeCharacter{FF5C}{|}" + "\n")
    file.write("\n")
    file.write("#+filetags: Cortex" + "\n")
    file.write("\n")

def write_org_footer(file):
    file.write("\n")
    file.write(r"#+csl-style: apa-numeric-superscript-brackets.csl" + "\n")
    file.write(r"#+csl-locale: en-US" + "\n")
    file.write("\n")
    file.write(r"#+begin_export org" + "\n")
    file.write(r"bibliographystyle:apacite" + "\n")
    file.write(r"#+end_export" + "\n")
    file.write(r"bibliography:../../../bibliography/bibliography.bib" + "\n")
    file.write("\n")

def list_to_org_table(file, list_name):

    command_list = registry.lists[list_name][0].items()

    file.write(f"* {list_name}" +  "\n")
    file.write("\n")
    file.write(f"| command word | {list_name} |" + "\n")
    file.write(f"|--------------|-------------|" + "\n")
    for key, value in command_list:
        if value == "|":
            value = "｜"
        file.write(f"| ={key}= | {value} |" + "\n")
    file.write("\n")

def write_org_alphabet(file):
    list_to_org_table(file, 'user.letter')

def write_org_numbers(file):
    list_to_org_table(file, 'user.number_key')

def write_org_modifiers(file):
    list_to_org_table(file, 'user.modifier_key')

def write_org_special(file):
    list_to_org_table(file, 'user.special_key')

def write_org_symbol(file):
    list_to_org_table(file, 'user.symbol_key')

def write_org_arrow(file):
    list_to_org_table(file, 'user.arrow_key')

def write_org_punctuation(file):
    list_to_org_table(file, 'user.punctuation')

def write_org_function(file):
    list_to_org_table(file, 'user.function_key')

def write_org_formatters(file):
    command_list = registry.lists['user.formatters'][0].items()

    file.write(f"* formatters" + "\n")
    file.write("\n")
    file.write(f"| command word | user.formatters |" + "\n")
    file.write(f"|--------------|-----------------|" + "\n")
    for key, value in command_list:
        text = f"example of formatting with {key}"
        file.write(f"| ={key}= | {actions.user.formatted_text(text, key)} |" + "\n")
    file.write("\n")

def write_org_context_commands(file, commands): 
    # write out each command and it's implementation
    for key in commands:
        try:
            rule = commands[key].rule.rule

            file.write("\n")
            file.write(f"- ={rule}= \n\n")
            file.write("  #+begin_example\n")

            implementation = commands[key].target.code
            l = implementation.split('\n')
            for s in l:
                if not s.startswith('#') and len(s) > 0:
                    file.write(f"{s}\n")

            file.write("  #+end_example\n")
        except Exception:
            continue

    file.write("\n")

def pretty_print_org_context_name(file, name):
    ## The logic here is intended to only print from talon files that have actual voice commands.  
        splits = name.split(".")
        index = -1
        
        os = ""
        
        if "mac " in name:
            os = "mac"
        if "win "in name: 
            os = "win"
        if "linux " in name:
            os = "linux"

        if "talon" in splits[index]:
            index = -2
            short_name = splits[index].replace("_", " ")
        else:
            short_name = splits[index].replace("_", " ")

        if "mac" == short_name or "win" == short_name or "linux" == short_name:
            index = index - 1
            short_name = splits[index].replace("_", " ")

        if len(os) > 0:
            file.write(f"* {os} {short_name}" + "\n")
        else:
            file.write(f"* {short_name}" + "\n")

        file.write("\n")

mod = Module()

@mod.action_class
class user_actions:
        def cheatsheet():
            """Print out a sheet of talon commands"""
            #open file

            this_dir  = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(this_dir, 'cheatsheet.md')

            with open(file_path,"w") as file:
                write_alphabet(file)
                write_numbers(file)
                write_modifiers(file)
                write_special(file)
                write_symbol(file)
                write_arrow(file)
                write_punctuation(file)
                write_function(file)
                write_formatters(file)

                #print out all the commands in all of the contexts

                list_of_contexts = registry.contexts.items()
                for key, value in list_of_contexts:
                    
                    commands= value.commands #Get all the commands from a context
                    if len(commands) > 0:
                        pretty_print_context_name(file, key)
                        write_context_commands(file,commands)

            this_dir  = r'c:\Users\Joe\Dropbox\emacs\psimacs\emacs\content\org\roam\cortex'
            file_path = os.path.join(this_dir, '2022-12-10-talon_cheatsheet.org')

            with open(file_path,"w") as file:
                write_org_preamble(file)

                write_org_alphabet(file)
                write_org_numbers(file)
                write_org_modifiers(file)
                write_org_special(file)
                write_org_symbol(file)
                write_org_arrow(file)
                write_org_punctuation(file)
                write_org_function(file)
                write_org_formatters(file)

                #print out all the commands in all of the contexts

                list_of_contexts = registry.contexts.items()
                for key, value in list_of_contexts:
                    
                    commands= value.commands #Get all the commands from a context
                    if len(commands) > 0:
                        pretty_print_org_context_name(file, key)
                        write_org_context_commands(file,commands)

                write_org_footer(file)