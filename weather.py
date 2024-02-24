from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = "814888a61de4b880b167379590024635"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        if weather_data['cod'] == 200:
            weather = {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon']
            }
            return render_template('weather.html', weather=weather)
        else:
            error_message = "City not found. Please try again."
            return render_template('index.html', error=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()