import os

import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You're are a helpful assistant."},
        {"role": "user", "content": "..."},
    ]
)
print(completion)
