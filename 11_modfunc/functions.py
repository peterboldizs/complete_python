def center_text(text):
    text = str(text)
    left_margin = (40 - len(text)) // 2
    print("_" * left_margin, text)


def centre_text2(*args):
    """
    text centering function with variable arguments

    :param args: the text items to be centered
    :return:
    """
    text = ""
    for arg in args:
        text += str(arg) + " - "
    left_margin = (30 - len(text)) // 2
    print("_" * left_margin, text)


def centre_text3(*args, sep='-', end_char='\n', dest_file=None, flush_me=False):
    """
    improved text centering function with variable arguments
    :param args:
    :param sep:
    :param end_char:
    :param dest_file:
    :param flush_me:
    :return:
    """
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (30 - len(text)) // 2
    print("_" * left_margin, text, end=end_char, file=dest_file, flush=flush_me)


def center_text4(text):
    """

    :param text:
    :return:
    """
    text = str(text)
    left_margin = (40 - len(text)) // 2
    return "_" * left_margin + text


print("*" * 40)
center_text("This is my text")
center_text("this is a somewhat longer text")
center_text("short text")
center_text(123)

print("*" * 40)
centre_text2("this is a text", "short text", 123)
print("*" * 40)
centre_text3("this is a text", "short text", 123)
centre_text3("this is a text", "short text", 123, sep=':')

with open("textfile.txt", mode='w') as destination_file:
    centre_text3("this is a text", "short text", 123, sep=':', dest_file=destination_file)

print("*" * 40)
print(center_text4("my text to print"))
s4 = center_text4("assign to a variable")
print(s4)
