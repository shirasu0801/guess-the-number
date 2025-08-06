function submitGuess() {
    const guess = document.getElementById('guessInput').value;
    fetch('/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ guess: guess })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = data.result;
    });
}