document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') sendMessage();
});

function sendMessage() {
    let userInput = document.getElementById('user-input').value;
    if (!userInput.trim()) return;

    appendMessage('You', userInput);
    document.getElementById('user-input').value = '';

    fetch('http://127.0.0.1:8000/chat/', {  // Ensure FastAPI is running on port 8000
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_message: userInput })
    })
    .then(response => response.json())
    .then(data => appendMessage('AI', data.bot_response))
    .catch(error => console.error('Error:', error));
}

function appendMessage(sender, message) {
    let chatBox = document.getElementById('chat-box');
    let messageDiv = document.createElement('div');
    messageDiv.className = sender === 'You' ? 'user-message' : 'bot-message';
    messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
