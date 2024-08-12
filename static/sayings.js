function fetchRandomText() {
    fetch('')
        .then(response => response.json())
        .then(data => {
            document.getElementById('random-text').innerText=data.text;})
        .catch(error => console.error('Error:', error));
        }

fetchRandomText();

setInterval(fetchRandomText, 5000);