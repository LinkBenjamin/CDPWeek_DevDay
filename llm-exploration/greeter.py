import sys
import os

[dad_costume, trick_or_treaters] = sys.argv[1:]

import openai
openai.api_key = os.environ["OPENAI_API_KEY"]


system_message=f"""
You are fun dad.

You are dressed as {dad_costume} for Halloween and are greeting trick or treaters at your door.

You should remain in the character of {dad_costume}.

The user is going to tell you what the trick or treaters are dressed as.

You should greet the trick or treaters specifically based on their costume.
"""

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": trick_or_treaters},

    ]
)
print(completion["choices"][0]["message"]["content"])
