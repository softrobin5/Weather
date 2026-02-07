from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("WEATHER_API_KEY", "PUT_YOUR_API_KEY_HERE")


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        data = get_weather(city)

        if data.get("cod") != 200:
            error = "City not found!"
        else:
            weather_data = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind": data["wind"]["speed"]
            }

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)