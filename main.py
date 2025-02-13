import requests
import os
from dotenv import load_dotenv
from send_email import send_email
import time

date=time.strftime('%Y-%m-%d')

load_dotenv()
api_key=os.getenv('API_KEY')

topic='tesla'

url=(f'https://newsapi.org/v2/everything?'
     f'q={topic}'
     f'&sortBy=publishedAt'
     f'&apiKey={api_key}'
     f'&language=en')

request=requests.get(url)
content=request.json()
head=f"Subject: Today's News {date}"
body=''
for article in content['articles'][:20]:
     body+=f"""
Title: {article['title']}
{article['description']}
Link: {article['url']}

     """

message=(head+body).encode('utf-8')

send_email(message)




