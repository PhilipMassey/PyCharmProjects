import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    question = input("\033[34mWhat is your question?\n\033[0m")

    if question.lower() == "exit":
        print("\033[31mGoodbye!")
        break

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Answer the given question."},
            {"role": "user", "content": question}
        ]
    )

    print(question)

    print("[32m" + completion.choices[0].message.content + "\n")
