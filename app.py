from flask import Flask, render_template
from tasks.sign_in import run_sign_in

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run")
def run():
    run_sign_in({
        "url": "https://example.com/login",
        "username": "test",
        "password": "123456",
        "username_id": "username",
        "password_id": "password",
        "login_id": "login"
    })
    return "任务已执行"

if __name__ == "__main__":
    app.run(debug=True)
