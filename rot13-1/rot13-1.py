import string
from codecs import encode as _dont_use_this_

def rot13(message):
    message = message.translate(string.maketrans('abcdefghijklmnopqrstuvwxyz','nopqrstuvwxyzabcdefghijklm'))
    return message.translate(string.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'NOPQRSTUVWXYZABCDEFGHIJKLM'))