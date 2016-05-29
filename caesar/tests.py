from django.test import TestCase
from django.utils import timezone
from .models import Message, ALPHABET
# Create your tests here.

class MessageMethodTests(TestCase):

    def test_encode(self):
        now = timezone.now()

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
        now = timezone.now()

