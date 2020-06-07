#newspaper reading
from win32com.client import Dispatch
import requests
import json

def speak(str):
	speak = Dispatch("SAPI.SpVoice")
	speak.speak(str)

if __name__ == "__main__":
	your_api="6e727aa31357452c909529c5cfb557c3"
	url = (f"http://newsapi.org/v2/top-headlines?country=in&apiKey={your_api}")
	response = requests.get(url)
	text = response.text
	my_json = json.loads(text)
	# print(my_json["articles"])
	arts = my_json['articles']
	
	for article in arts:
		print(article["title"])
		speak(article['title'])
		speak("Moving to next")