import pyperclip

board = pyperclip.paste()
words = board.split()
result = ''

for word in words:
    result = result + ' ' + word

pyperclip.copy(result)
