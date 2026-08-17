from flask import Flask, request, render_template_string
import random
import string
app = Flask(__name__)
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">
    <title>Password Generator</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: Arial, sans-serif;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background:
                linear-gradient(135deg, #0f172a, #1e293b);
            color: white;
        }
        .container {
            width: 450px;
            padding: 35px;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            box-shadow:
                0 20px 50px rgba(0, 0, 0, 0.4);
        }
        .title {
            text-align: center;
            margin-bottom: 8px;
            font-size: 30px;
        }
        .subtitle {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 30px;
        }
        .password-box {
            display: flex;
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 25px;
        }
        .password-box input {
            flex: 1;
            background: transparent;
            border: none;
            outline: none;
            color: white;
            padding: 15px;
            font-size: 17px;
        }
        .password-box button {
            border: none;
            background: #2563eb;
            color: white;
            padding: 0 18px;
            cursor: pointer;
            font-size: 14px;
        }
        .password-box button:hover {
            background: #1d4ed8;
        }
        .section {
            margin-bottom: 25px;
        }
        .section-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 12px;
            color: #cbd5e1;
        }
        #lengthValue {
            color: #60a5fa;
            font-weight: bold;
        }
        input[type="range"] {
            width: 100%;
            cursor: pointer;
        }
        .requirements {
            background: rgba(15, 23, 42, 0.7);
            padding: 18px;
            border-radius: 12px;
            margin-bottom: 25px;
        }
        .requirements h3 {
            margin-bottom: 12px;
            font-size: 16px;
        }
        .requirement {
            display: flex;
            justify-content: space-between;
            padding: 7px 0;
            color: #cbd5e1;
        }
        .check {
            color: #22c55e;
        }
        .strength {
            margin-bottom: 25px;
        }
        .strength-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            color: #cbd5e1;
        }
        .strength-bar {
            height: 8px;
            background: #334155;
            border-radius: 10px;
            overflow: hidden;
        }
        .strength-fill {
            height: 100%;
            width: 0%;
            background: #22c55e;
            transition: 0.3s;
        }
        .buttons {
            display: flex;
            gap: 10px;
        }
        .generate {
            flex: 1;
            padding: 14px;
            border: none;
            border-radius: 10px;
            background: #2563eb;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        .generate:hover {
            background: #1d4ed8;
        }
        .regenerate {
            padding: 14px 18px;
            border: 1px solid #475569;
            border-radius: 10px;
            background: transparent;
            color: white;
            cursor: pointer;
        }
        .regenerate:hover {
            background: #334155;
        }
        .footer {
            text-align: center;
            margin-top: 25px;
            color: #64748b;
            font-size: 13px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1 class="title">
        🔐 Password Generator
    </h1>
    <p class="subtitle">
        Create a strong and secure password
    </p>
    <div class="password-box">
        <input
            type="password"
            id="password"
            value="{{ password }}"
            readonly
        >
        <button onclick="copyPassword()">
            Copy
        </button>
    </div>
    <form method="POST" id="passwordForm">
        <div class="section">
            <div class="section-header">
                <span>Password Length</span>
                <span id="lengthValue">
                    16
                </span>
            </div>
            <input
                type="range"
                id="length"
                name="length"
                min="4"
                max="50"
                value="{{ length }}"
                oninput="updateLength()"
            >
        </div>
        <div class="requirements">
            <h3>Password Requirements</h3>
            <div class="requirement">
                <span>Uppercase Letter</span>
                <span class="check">✓</span>
            </div>
            <div class="requirement">
                <span>Lowercase Letter</span>
                <span class="check">✓</span>
            </div>
            <div class="requirement">
                <span>Number</span>
                <span class="check">✓</span>
            </div>
            <div class="requirement">
                <span>Symbol</span>
                <span class="check">✓</span>
            </div>
        </div>
        <div class="strength">
            <div class="strength-header">
                <span>Password Strength</span>
                <span id="strengthText">
                    Strong
                </span>
            </div>
            <div class="strength-bar">
                <div
                    class="strength-fill"
                    id="strengthFill">
                </div>
            </div>
        </div>
        <div class="buttons">
            <button
                type="submit"
                class="generate">
                Generate Password
            </button>
            <button
                type="button"
                class="regenerate"
                onclick="generateAgain()">
                ↻
            </button>
        </div>
    </form>
    <div class="footer">
        Password Generator • Python Flask
    </div>
</div>
<script>
function updateLength() {
    let slider =
        document.getElementById("length");
    let value =
        document.getElementById("lengthValue");
    value.innerText =
        slider.value;
    updateStrength(
        Number(slider.value)
    );
}
function updateStrength(length) {
    let strengthText =
        document.getElementById("strengthText");
    let strengthFill =
        document.getElementById("strengthFill");
    if (length < 8) {
        strengthText.innerText =
            "Weak";
        strengthFill.style.width =
            "30%";
        strengthFill.style.background =
            "#ef4444";
    }
    else if (length < 12) {
        strengthText.innerText =
            "Medium";
        strengthFill.style.width =
            "60%";
        strengthFill.style.background =
            "#f59e0b";
    }
    else if (length < 18) {
        strengthText.innerText =
            "Strong";
        strengthFill.style.width =
            "80%";
        strengthFill.style.background =
            "#22c55e";
    }
    else {
        strengthText.innerText =
            "Very Strong";
        strengthFill.style.width =
            "100%";
        strengthFill.style.background =
            "#10b981";
    }
}
function copyPassword() {
    let password =
        document.getElementById("password");
    if (password.value === "") {
        alert("Generate a password first!");
        return;
    }
    navigator.clipboard.writeText(
        password.value
    );
    alert("Password copied!");
}
function generateAgain() {
    document
        .getElementById("passwordForm")
        .submit();
}
updateStrength(
    Number(
        document.getElementById("length").value
    )
);
</script>
</body>
</html>
"""
def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%&*"
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(symbols)
    ]
    all_characters = (
        uppercase
        + lowercase
        + numbers
        + symbols
    )
    for i in range(length - 4):
        password.append(
            random.choice(all_characters)
        )
    random.shuffle(password)
    return "".join(password)
@app.route("/", methods=["GET", "POST"])
def home():
    password = ""
    length = 8
    if request.method == "POST":
        length = int(
            request.form["length"]
        )
        if length < 4:
            length = 4
        password = generate_password(
            length
        )
    return render_template_string(
        HTML_PAGE,
        password=password,
        length=length
    )
if __name__ == "__main__":
    app.run(debug=True)