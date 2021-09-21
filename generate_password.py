# Diceware method: https://en.wikipedia.org/wiki/Diceware
# input number of words in passphrase, Print string of random words
# Using secrets python module: https://docs.python.org/3/library/secrets.html
# wordlist, copy and save the text, else file deleted by AV: https://theworld.com/~reinhold/diceware.wordlist.asc

import secrets


def generate_passphrase(num_words):
    with open('wordlist.txt', 'r') as file:
        lines = file.readlines()

        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)

password = generate_passphrase(3)
print('\nYour Password is: {}'.format(password))



