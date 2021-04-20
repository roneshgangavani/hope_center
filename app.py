from routes.auth import index,ask_help
from application import app
from flask import Flask, current_app

app.add_url_rule("/", "index", index)
app.add_url_rule("/ask_help/", "Asking help", ask_help)
# app.add_url_rule("/login", "login", login, methods=["GET", "POST"])
# app.add_url_rule("/register", "register", register, methods=["GET", "POST"])
# app.add_url_rule("/logout", "logout", logout)


from security.security import login_manger

login_manger.init_app(app)
import dashurls

if __name__ == "__main__":
    app.run()
