import requests

# Replace 'YOUR_API_KEY' with your osu! API key
api_key = 'YOUR_API_KEY'

# Fetch data for multiple users
user_count = 30
users_data = []

for i in range(1, user_count + 1):
    user_url = f'https://osu.ppy.sh/api/get_user?k={api_key}&u=user{i}'
    user_response = requests.get(user_url)

    if user_response.status_code == 200:
        user_data = user_response.json()
        users_data.append(user_data)

# Fetch data for multiple beatmaps
beatmap_count = 100
beatmaps_data = []

for i in range(1, beatmap_count + 1):
    beatmap_url = f'https://osu.ppy.sh/api/get_beatmaps?k={api_key}&b=beatmap{i}'
    beatmap_response = requests.get(beatmap_url)

    if beatmap_response.status_code == 200:
        beatmap_data = beatmap_response.json()
        beatmaps_data.append(beatmap_data)

# Fetch data for multiple scores
score_count = 200
scores_data = []

for i in range(1, score_count + 1):
    score_url = f'https://osu.ppy.sh/api/get_scores?k={api_key}&s=score{i}'
    score_response = requests.get(score_url)

    if score_response.status_code == 200:
        score_data = score_response.json()
        scores_data.append(score_data)

# Process and work with the collected user, beatmap, and score data as needed
print(f'Users Data: {users_data}')
print(f'Beatmaps Data: {beatmaps_data}')
print(f'Scores Data: {scores_data}')
