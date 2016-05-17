# from django.db import models
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


# My class will not store any data in database,
# actually, here is nothing to store, we just
# encoding message, not saving it.
class Coder():
    def encode(self, message, rotate):
        """
        Shifting every symbol in 'message' by 'rotate', if symbol is in ALPHABET.
        Shift is circled
        """
        encoded = []
        for symbol in message.lower():  # we don't use capitals
            if symbol in ALPHABET:
                # shift is circled to avoid 'index out of range' exception
                # and also that operation is a part of Caesar cipher :)
                shift = (ALPHABET.find(symbol) + rotate) % len(ALPHABET)
                encoded.append(ALPHABET[shift])
            else:
                encoded.append(symbol)
        return ''.join(encoded)

    def decode(self, cipher, rotate):
        return self.encode(cipher, -rotate)

    def frequencyDict(self, text):
        """
        Calculates frequency of symbols in text (only symbols from ALPHABET)
        :return: dict{ symbol: frequency, symbol2: frequency2, ...}
        """
        return {symbol: text.count(symbol) for symbol in text if symbol in ALPHABET}
