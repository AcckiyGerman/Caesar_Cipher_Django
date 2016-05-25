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
        frequency_list = self.frequency_list()
        if len(frequency_list) < 3:
            return False
        probability = 0
        # Counting usage of 4 most frequent words
        # and 2 most frequent symbols in English
        # Coefficients taken from the Wikipedia.
        probability += self.message.count('the') * 1.6
        probability += self.message.count('and') * 0.7
        probability += self.message.count(' a ') * 0.7
        probability += self.message.count('you') * 0.5
        if frequency_list[0] == 'e' or frequency_list[1] == 'e':
            probability += 0.7
        if frequency_list[1] == 't' or frequency_list[2] == 't':
            probability += 0.5
        # We use message length in recognizing formula, but messages, which
        # are too short, makes formula do false results, so shortest length=30
        message_length = len(self.message) if len(self.message) > 30 else 30
        return (probability * message_length) >= 40
        # '40' taken from experience, after several tries

    def restore_message(self):
        """
        Trying to restore text from caesar cipher (stored in self.message)
        WARNING: This method will replace self.message, if it can decode one.
        :return: ('restored text', 'probably_rotate')
        """
        if self.is_english():
            return (self.message,
                    'seems, message is not encoded')
        original_message = self.message
        # First method based on finding most frequent letter in cipher
        # (most frequent letter in English is 'e'):
        most_frequent_letter = self.frequency_list()[0]
        probably_rotate = ALPHABET.index(most_frequent_letter) - ALPHABET.index('e')
        self.message = self.decode(probably_rotate)
        if self.is_english():
            return (self.message,
                    'probably, rotate = ' + str(probably_rotate))
        # Second method - brute forcing:
        self.message = original_message
        for probably_rotate in range(len(ALPHABET)):
            self.message = self.decode(1)
            if self.is_english():
                return (self.message,
                        'probably, rotate = ' + str(probably_rotate))
        # failed to decode message - restoring self.message
        self.message = original_message
        return (self.message,
                "can't recognize message")