import datetime
import matplotlib.pyplot as plt
from score_logic import score_run_conditions

def get_best_times(forecast_data, aqi_level):
    scored = []

    for item in forecast_data['list'][:16]:
        dt = datetime.datetime.fromtimestamp(item['dt'])
        temp = item['main']['temp']
        wind = item['wind']['speed']
        weather_desc = item['weather'][0]['description']

        score = score_run_conditions(temp, aqi_level, wind, weather_desc)

        scored.append({
            'time': dt,
            'temp': temp,
            'wind': wind,
            'weather': weather_desc,
            'score': score
        })

    best_times = sorted(scored, key=lambda x: x['score'], reverse=True)[:2]
    return best_times

def plot_scores_matplotlib(best_times):
    times = [item['time'] for item in best_times]
    scores = [item['score'] for item in best_times]

    plt.figure(figsize=(8,4))
    plt.plot(times, scores, marker='o', linestyle='-', color='blue')
    plt.title('Running Time Recommendation Score')
    plt.xlabel('Time')
    plt.ylabel('Score')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
