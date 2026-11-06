import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {'role' : 'system' , 'content' : 'You are a helpful assistant.'},
]
while True:
    user_input = input("Say something:")
    if user_input.lower() == "exit":
        break

    messages.append({'role': 'user', 'content': user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages= messages
        )
        ai_response = response.choices[0].message.content
        print("AI:", ai_response)
        messages.append ({'role': 'assistant', 'content': ai_response})
    except Exception as e:
        print("Error:", str(e))