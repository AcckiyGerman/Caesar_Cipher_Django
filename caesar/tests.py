from django.test import TestCase
from django.utils import timezone
from .models import Message, ALPHABET
# Create your tests here.

now = timezone.now()

class MessageMethodTests(TestCase):

    def test_encode(self):
        message = Message(text='a-z0-9', rotate=1, date=now)
        self.assertEqual(message.encode(), 'b-a0-9')

        message2 = Message(text='abz0-9', rotate=-1, date=now)
        self.assertEqual(message2.encode(), 'zay0-9')

        message3 = Message(text='a-z', rotate=len(ALPHABET)*200 - 2, date=now)
        self.assertEqual(message3.encode(), 'y-x')

        message4 = Message(text='veni, vidi, vici', rotate=0, date=now)
        self.assertEqual(message4.encode(1), 'wfoj, wjej, wjdj')
        self.assertEqual(message4.encode(0), 'veni, vidi, vici')
        self.assertEqual(message4.encode(len(ALPHABET)*10 + 1),
                         'wfoj, wjej, wjdj')

    def test_decode(self):
        message = Message(text='b-a', rotate=1, date=now)
        self.assertEqual(message.decode(), 'a-z')

        message2 = Message(text='wfoj, wjej, wjdj', rotate=1, date=now)
        self.assertEqual(message2.decode(), 'veni, vidi, vici')

    def test_frequency_dict(self):
        message = Message(text='aaabbc', rotate=0, date=now)
        self.assertEqual(message.frequency_dict(), {'a': 3, 'b': 2, 'c': 1})

        message2 = Message(text='zzzy5ww\n\t буквы не из алфавита', rotate=0,
                           date=now)
        self.assertEqual(message2.frequency_dict(), {'z': 3, 'y': 1, 'w': 2})

    def test_frequency_list(self):
        message1 = Message(text='aaabbc', rotate=0, date=now)
        message2 = Message(text='zzz--99977 bb y', rotate=0, date=now)

        self.assertEqual(message1.frequency_list(), ['a', 'b', 'c'])
        self.assertEqual(message2.frequency_list(), ['z', 'b', 'y'])

    def test_restore_message(self):
        message = Message(text='pda ckkz wjz pda xwz', rotate=12, date=now)
        self.assertEqual(message.restore_message()[0], 'the good and the bad')