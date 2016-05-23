# from django.db import models
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class Coder():
    def __init__(self, message):
        self.message = message.lower()

    def encode(self, rotate):
        """
        Shifting every symbol in 'message' by 'rotate', if symbol is in
        ALPHABET. Shift is circled.
        """
        encoded_message = []
        for symbol in self.message:
            if symbol in ALPHABET:
                encoded_symbol_index = (ALPHABET.find(symbol) + rotate) %\
                    len(ALPHABET)
                encoded_message.append(ALPHABET[encoded_symbol_index])
            else:
                encoded_message.append(symbol)
        return ''.join(encoded_message)

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
        # for example: self.message = 'abbccc'
        frequency_dict_items = list(self.frequency_dict().items())
        # [('b', 2), ('a', 1), ('c', 3)]
        frequency_dict_items.sort(key=lambda x: x[1], reverse=True)
        # [('c', 3), ('b', 2), ('a', 1)]
        return [symbol for (symbol, _) in frequency_dict_items]
        # ['c', 'b', 'a']

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

    def unravel_text(self):
        """ Trying to restore text from caesar cipher (stored in self.message)
        :return: text
        """
        # First, checking, if message is encoded:
        if self.is_english():
            return self.message

        # Second method, based on finding most frequent letter in cipher
        # (most frequent letter in English is 'e'):
        M = self.frequency_list()[0]  # most frequent letter
        pRot = ALPHABET.index(M) - ALPHABET.index('e')  # probably rotate value
        self.originalMessage = self.message  # remember message
        self.message = self.decode(pRot)
        if self.is_english():
            return self.message + '\nFINDING "E" METHOD, ROTATE = ' + str(pRot)

        # Third method - brute forcing:
        self.message = self.originalMessage
        for pRot in range(len(ALPHABET)):
            self.message = self.decode(1)
            if self.is_english():
                return self.message + '\nBRUTE FORCE METHOD, ROTATE = ' + str(pRot+1)
        # we cant decode message, so let's restore it back
        self.message = self.originalMessage
        return "CANT RECOGNIZE MESSAGE :(".upper()