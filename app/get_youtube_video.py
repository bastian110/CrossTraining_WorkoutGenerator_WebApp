from googleapiclient.discovery import build
import re

import os
from dotenv import load_dotenv
from app import df

load_dotenv()

api_key = os.getenv('YOUTUBE_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

df['Video_URL'] = ''

crossfit_channel_id = 'UCtcQ6TPwXAYgZ1Mcl3M1vng'  # CrossFit's YouTube channel ID

for index, row in df.iterrows():
    search_query = f"{row['Name']} site:youtube.com/channel/{crossfit_channel_id}"
    
    search_request = youtube.search().list(
        part='snippet',
        type='video',
        q=search_query,
        maxResults=1,
        fields='items(id(videoId))'
    )
    search_response = search_request.execute()
    
    if search_response['items']:
        video_id = search_response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        df.at[index, 'Video_URL'] = video_url

df.to_csv("/Users/bastianchuttarsing/Documents/Crosstraining_WebApp/data-science/dataset/dataset_exercices_crosstraining_with_description_and_video.csv", index=False)
