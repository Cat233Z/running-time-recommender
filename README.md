# running-time-recommender
A web app for recommending running time based on weather and air quality using Streamlit

# 🏃 Running Time Recommender

A Streamlit-powered weather and AQI-based tool to recommend optimal time slots for outdoor running.

---

## 📌 Features
- Fetch 3-hour interval weather forecasts for any global city
- AQI level check for real-time air pollution awareness
- Score and rank the best time slots for outdoor running
- Interactive line chart with Matplotlib
- Clean, web-based interface via Streamlit

---

## 🔧 Technologies Used

| Category        | Tools / Libraries           |
|----------------|-----------------------------|
| Language        | Python                      |
| API             | OpenWeatherMap API          |
| Data Handling   | `requests`, `datetime`      |
| Visualization   | `matplotlib`, `streamlit`   |

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Cat233Z/running-time-recommender.git
   cd running-time-recommender
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenWeatherMap API key inside `app.py`.

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## ✍️ Author

**Xinyi Zhu**  
Computational Data Science @ Penn State  
GitHub: [github.com/Cat233Z](https://github.com/Cat233Z)