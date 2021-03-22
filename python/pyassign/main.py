import random


def get_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [word.strip().upper() for word in f.readlines()]

def get_random_word(words):
    word = random.choice(words)
    words.remove(word)
    return word


words = get_words('words.txt')
print("Hello, let's play!")
while True:
    words = words if words else get_words('words.txt')
    answer = get_random_word(words)
    result_list = len(answer)*['_']
    attempts_remaining = 5

    print('Word: ', ' '.join(result_list))
    while attempts_remaining:
        guess = input('Make a guess: ').upper()
        if guess in answer:  # User made correct guess
            print(guess)
            for i, char in enumerate(answer):
                if char == guess:
                    result_list[i] = guess
            if ''.join(result_list) == answer:
                print(f'You win! The word is {answer}')
                break
        else:
            print(f'Sorry, {guess} is not in the word.')
            attempts_remaining -= 1

        print('Current result: ', ' '.join(result_list))
    else:
        print('Sorry, no attempts remaining, you lose!')
    print(get_words('words.txt'))
    print(words)
    print(answer)