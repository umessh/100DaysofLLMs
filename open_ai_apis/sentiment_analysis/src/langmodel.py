import os

from openai import OpenAI 

ai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def analyse_sentiment(text):
    sentiment_analyser = ai_client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "system", 
                "content": 'You are a sentiment classification bot, print out if the user is "happy" or "unhappy" in single word based on the user input'
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    response = sentiment_analyser.choices[0].message.content
    print(response)
    return response