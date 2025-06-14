def score_run_conditions(temp, aqi_level, wind_speed, weather_desc):
    score = 0

    # 温度评分 (0 ~ 40)
    if 20 <= temp <= 26:
        score += 40
    else:
        diff = abs(temp - 23)  # 23°C 是理想点
        temp_score = max(0, 40 - diff * 5)
        score += temp_score

    # AQI 评分 (0 ~ 30)
    if aqi_level == 1:
        score += 30
    elif aqi_level == 2:
        score += 20
    elif aqi_level == 3:
        score += 10
    else:
        score += 0  # 等级 4/5 太差

    # 风速评分 (0 ~ 20)
    if wind_speed <= 3:
        score += 20
    elif wind_speed <= 6:
        score += 10
    else:
        score += 0

    # 天气评分 (0 ~ 10)
    bad_keywords = ['rain', 'snow', 'storm', 'thunder']
    if any(bad in weather_desc.lower() for bad in bad_keywords):
        score += 0
    else:
        score += 10

    return round(score, 1)
