import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


while True:
    user_input = input("Say something:")
    if user_input.lower() == "exit":
        break

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {'role': 'system' , 'content' : 'You are a helpful assistant.'},
                {'role': 'user' , 'content' : user_input}
            ]
        )
        ai_response = response.choices[0].message.content
        print("AI:", ai_response)
    except Exception as e:
        print("Error:", str(e))