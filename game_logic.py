import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']

def new_game():
    word = random.choice(word_bank)
    return {
        'word': word,
        'guessed_word': ['_'] * len(word),
        'attempts': 10,
        'won': False,
        'lost': False
    }

def make_guess(game_state, guess):
    word = game_state['word']
    guess = guess.lower()

    if len(guess) != len(word):
        return {'error': f'Guess must be {len(word)} letters long'}

    correct_positions = 0
    for i in range(len(word)):
        if guess[i] == word[i]:
            game_state['guessed_word'][i] = guess[i]
            correct_positions += 1

    if guess == word:
        game_state['won'] = True
    else:
        game_state['attempts'] -= 1
        if game_state['attempts'] == 0:
            game_state['lost'] = True

    return {
        'guessed_word': game_state['guessed_word'],
        'attempts': game_state['attempts'],
        'correct_positions': correct_positions,
        'won': game_state['won'],
        'lost': game_state['lost'],
        'word': word if (game_state['won'] or game_state['lost']) else None
    }