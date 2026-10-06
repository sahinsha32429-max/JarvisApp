from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>JARVIS AI</title>

<style>
body {
    background: #020817;
    color: #00d9ff;
    text-align: center;
    font-family: Arial;
    padding: 25px;
}
h1 {
    margin-top: 50px;
    text-shadow: 0 0 15px #00d9ff;
}
button {
    background: #007bff;
    color: white;
    border: 0;
    padding: 18px 30px;
    border-radius: 30px;
    font-size: 18px;
    margin: 10px;
}
#status {
    color: white;
    margin-top: 30px;
}
</style>
</head>

<body>

<h1>J.A.R.V.I.S</h1>
<h2>Welcome Sahin!</h2>

<p id="status">Assistant is ready.</p>

<button onclick="startJarvis()">START JARVIS</button>
<button onclick="stopJarvis()">STOP</button>

<script>
let recognition;
let running = false;
let speaking = false;

function speak(message) {
    speaking = true;

    let voice = new SpeechSynthesisUtterance(message);
    voice.lang = "en-IN";

    voice.onend = function() {
        speaking = false;

        if (running) {
            setTimeout(listenAgain, 800);
        }
    };

    speechSynthesis.cancel();
    speechSynthesis.speak(voice);
}

function listenAgain() {
    if (!running || speaking) return;

    try {
        recognition.start();
    } catch (e) {
        setTimeout(listenAgain, 1000);
    }
}

function startJarvis() {
    let SR = window.SpeechRecognition ||
             window.webkitSpeechRecognition;

    if (!SR) {
        document.getElementById("status").innerText =
        "Speech recognition is not supported.";
        return;
    }

    running = true;

    recognition = new SR();
    recognition.lang = "en-IN";
    recognition.interimResults = false;
    recognition.continuous = false;

    recognition.onstart = function() {
        document.getElementById("status").innerText =
        "Listening... Speak now.";
    };

    recognition.onresult = function(event) {
        let text = event.results[0][0].transcript.toLowerCase();

        let reply = "Sorry Sahin, I don't understand.";

        if (text.includes("hello") || text.includes("hi")) {
            reply = "Hello Sahin! How can I help you?";
        } else if (text.includes("who are you")) {
            reply = "I am Jarvis, your personal assistant.";
        } else if (text.includes("who am i")) {
            reply = "You are Sahin.";
        } else if (text.includes("how are you")) {
            reply = "I am fine, thank you!";
        } else if (text.includes("thank")) {
            reply = "You are welcome, Sahin!";
        } else if (text.includes("bye")) {
            reply = "Goodbye Sahin!";
            running = false;
        }

        document.getElementById("status").innerText =
        "You said: " + text + "\\nJarvis: " + reply;

        speak(reply);
    };

    recognition.onerror = function(event) {
        document.getElementById("status").innerText =
        "Microphone: " + event.error;
    };

    recognition.onend = function() {
        if (running && !speaking) {
            setTimeout(listenAgain, 800);
        }
    };

    listenAgain();
}

function stopJarvis() {
    running = false;

    if (recognition) {
        recognition.stop();
    }

    speechSynthesis.cancel();

    document.getElementById("status").innerText =
    "Jarvis stopped.";
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
