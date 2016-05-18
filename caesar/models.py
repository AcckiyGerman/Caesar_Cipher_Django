# from django.db import models
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


# My class will not store any data in database,
# actually, here is nothing to store, we just
# encoding message, not saving it.
class Coder():
    def __init__(self, message):
        self.message = message.lower()  # we don't use capitals

    def encode(self, rotate):
        """
        Shifting every symbol in 'message' by 'rotate', if symbol is in ALPHABET.
        Shift is circled
        """
        encoded = []
        for symbol in self.message:
            if symbol in ALPHABET:
                # shift is circled to avoid 'index out of range' exception
                # and also that operation is a part of Caesar cipher :)
                shift = (ALPHABET.find(symbol) + rotate) % len(ALPHABET)
                encoded.append(ALPHABET[shift])
            else:
                encoded.append(symbol)
        return ''.join(encoded)

    def decode(self, rotate):
        return self.encode(-rotate)

    def frequency_dict(self):
        """
        Calculates frequency of symbols in text (only symbols from ALPHABET)
        :return: dict{ symbol: frequency, symbol2: frequency2, ...}
        """
        return {symbol: self.message.count(symbol) for symbol in self.message
                if symbol in ALPHABET}

    def frequency_list(self):
        """returns list of letters presented in text, sorted by frequency"""
        frequencyDict = self.frequency_dict()
        # sorting symbols by value
        sortedFrequencyDict = sorted(frequencyDict.items(), key=lambda x: x[1], reverse=True)
        # now we have dict with symbols and values, like that: [('c', 3), ('b', 2), ('a', 1)]
        # let's return only list of letters (and it is now sorted)
        return [s for (s, _) in sortedFrequencyDict]

    def is_english(self):
        """ trying to recognize english text. :return: True or False """
        F = self.frequency_list()
        if len(F) < 4:
            return False
        length = len(self.message) if len(self.message) > 30 else 30
        # we using 4 most frequent words and 2 most frequent symbols in English
        P = 0  # Probability
        P += self.message.count('the') * 1.6
        P += self.message.count('and') * 0.7
        P += self.message.count(' a ') * 0.7
        P += self.message.count('you') * 0.5
        if F[0] == 'e' or F[1] == 'e': P += 0.7
        if F[1] == 't' or F[2] == 't': P += 0.5
        # my probability function :)
        return (P * length/40) >= 1