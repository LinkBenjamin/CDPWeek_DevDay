import sys
import os

[candy_rant] = sys.argv[1:]

import openai
openai.api_key = os.environ["OPENAI_API_KEY"]


system_message=f"""
You are fun dad.

You are going to be told what candy the trick or treaters have received, so that you can purchase their favorites next year.

It is going to be a long rant, but there is valuable information and sentiment that you will summarize.

The user will provide you with a fast rant, try to pull out the candy information.
"""

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": candy_rant},

    ]
)
print(completion["choices"][0]["message"]["content"])
