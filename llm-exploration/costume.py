import os

import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You're are a helpful assistant."},
        {"role": "user", "content": "I'm a fun dad and I need a costume for Halloween for passing out candy to kids at the door. What do you suggest?"},
        {"role": "assistant", "content": """That sounds like a fantastic idea! Here are a few costume suggestions that could make you the fun dad of the neighborhood this Halloween:\n\n1. Superhero Dad: Dress up as your favorite superhero! Whether it's Superman, Spider-Man, or Batman, kids will love seeing a real superhero handing out candy at the door.\n\n2. Funny Clown: Embrace your inner clown and make kids laugh with a colorful and silly clown costume. Add some oversized shoes and a red nose for some extra fun!\n\n3. Pirate Dad: Channel your inner pirate captain with a pirate-themed costume. Don an eye patch, bandana, and a pirate hat to complete the look. You can also have a treasure chest full of candy as a prop.\n\n4. Ghostbuster Dad: Be a ghostbuster and turn heads with your unique costume! Wear the iconic jumpsuit, a proton pack, and carry a ghost-catching device. This costume is sure to bring excitement to the trick-or-treaters.\n\n5. Mad Scientist Dad: Become the eccentric scientist for Halloween! Don a lab coat, crazy messy hair, and carry test tubes or beakers filled with candy. You can also use dry ice to create a spooky effect.\n\nRemember, the key is to have fun and make the kids smile. Choose a costume that fits your personality and enjoy the Halloween festivities!"""},
        {"role": "user", "content": "Ooh tell me about the Superhero but let's make it very DIY. Let's keep it cheap"},

    ]
)

print(completion["choices"][0]["message"]["content"])
