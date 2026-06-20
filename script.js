let gameId = null;

async function startNewGame() {
    const res = await fetch('/api/new-game', { method: 'POST' });
    const data = await res.json();

    gameId = data.game_id;
    document.getElementById('word-display').textContent = data.guessed_word.join(' ');
    document.getElementById('attempts').textContent = `Attempts left: ${data.attempts}`;
    document.getElementById('message').textContent = '';
}

async function makeGuess() {
    const guessInput = document.getElementById('guess-input');
    const guess = guessInput.value.trim();

    if (!guess) return;

    const res = await fetch('/api/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ game_id: gameId, guess: guess })
    });

    const data = await res.json();

    if (data.error) {
        document.getElementById('message').textContent = data.error;
        return;
    }

    document.getElementById('word-display').textContent = data.guessed_word.join(' ');
    document.getElementById('attempts').textContent = `Attempts left: ${data.attempts}`;
    guessInput.value = '';

    if (data.won) {
        document.getElementById('message').textContent = `🎉 You won! The word was "${data.word}"`;
    } else if (data.lost) {
        document.getElementById('message').textContent = `💀 Game over! The word was "${data.word}"`;
    } else {
        document.getElementById('message').textContent = `${data.correct_positions} letter(s) in correct spot.`;
    }
}

document.getElementById('guess-btn').addEventListener('click', makeGuess);
document.getElementById('new-game-btn').addEventListener('click', startNewGame);
document.getElementById('guess-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') makeGuess();
});

// Start the first game automatically
startNewGame();