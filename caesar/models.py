# from django.db import models
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


# My class will not store any data in database,
# actually, here is nothing to store, we just
# encoding message, not saving it.
class Coder():
    def __init__(self, message, rotate):
        self.message = message
        self.rotate = rotate

    def encode(self):
        """
        Shifting every symbol in 'message' by 'rotate', if symbol is in ALPHABET.
        Shift is circled
        """
        encoded = []
        for symbol in self.message.lower():  # we don't use capitals
            if symbol in ALPHABET:
                # shift is circled to avoid 'index out of range' exception
                # and also that operation is a part of Caesar cipher :)
                shift = (ALPHABET.find(symbol) + self.rotate) % len(ALPHABET)
                encoded.append(ALPHABET[shift])
            else:
                encoded.append(symbol)
        return ''.join(encoded)

    def frequencyDict(self):
        """
        Calculates frequency of symbols in text (only symbols from ALPHABET)
        :return: dict{ symbol: frequency, symbol2: frequency2, ...}
        """
        return {symbol: self.message.count(symbol) for symbol in self.message
                if symbol in ALPHABET}
