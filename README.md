This project was made as a test job for an web-development company.

The task was to create an single-page application using AJAX and DJANGO in backend.
The app should be able to convert user message using 'Caesar cipher'
{
  Caesar cipher is one of the most ancient way to cover your message from an enemy
  eyes. Every letter in the message must be shifted in the alphabet for an fixed
  amount called ROT(rotate).
  For example, if the message is 'ABC Z' and ROT = 1
  Then encoded message would be  'BCD A'
}
Conventing process should run on server side.
Also the app can decode cipher with known ROT
And finally, the app tries to recognize if the message is encoded, and to decode it
automatically.

This project is an ordinary Django application, and you can run it in any environment
which can run django apps.
Don't forget to make migrations of DB. (or you can just download existing one)
