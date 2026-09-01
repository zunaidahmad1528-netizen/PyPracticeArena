const chatBox = document.getElementById("chatBox");
const input = document.getElementById("userInput");

function sendMessage() {
  const text = input.value.trim();
  if (text === "") return;

  addMessage(text, "user");
  input.value = "";

  setTimeout(() => botReply(text), 500);
}

function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.className = `message ${sender}`;
  msg.innerText = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function botReply(text) {
  let reply = "Sorry, I didn’t understand that.";

  text = text.toLowerCase();

  if (text.includes("hello") || text.includes("hi")) {
    reply = "Hello! How can I help you?";
  } 
  else if (text.includes("your name")) {
    reply = "I am an AI Chatbot created by a CSE student.";
  }
  else if (text.includes("what is ai")) {
    reply = "AI stands for Artificial Intelligence. It makes machines intelligent.";
  }
  else if (text.includes("html")) {
    reply = "HTML is used to create the structure of web pages.";
  }
  else if (text.includes("css")) {
    reply = "CSS is used to style web pages.";
  }
  else if (text.includes("javascript")) {
    reply = "JavaScript adds logic and interactivity to websites.";
  }
  else if (text.includes("bye")) {
    reply = "Goodbye! Have a great day 😊";
  }

  addMessage(reply, "bot");
}

/* 🎤 Voice Input */
function startVoice() {
  const recognition = new webkitSpeechRecognition();
  recognition.lang = "en-US";
  recognition.start();

  recognition.onresult = function(event) {
    input.value = event.results[0][0].transcript;
  };
}
