from flask import Flask, jsonify, request, render_template
from game_logic import new_game, make_guess
import uuid

app = Flask(__name__)

games = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/new-game', methods=['POST'])
def start_new_game():
    game_id = str(uuid.uuid4())
    games[game_id] = new_game()
    return jsonify({
        'game_id': game_id,
        'guessed_word': games[game_id]['guessed_word'],
        'attempts': games[game_id]['attempts']
    })

@app.route('/api/guess', methods=['POST'])
def guess():
    data = request.get_json()
    game_id = data.get('game_id')
    guess_word = data.get('guess')

    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404

    result = make_guess(games[game_id], guess_word)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)