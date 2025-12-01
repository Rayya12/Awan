from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Halo, Kami dari kelompok 1 ini aplikasi kami"

if __name__ == "__main__":
    app.run()