import openai
# Set up your OpenAI API credentials
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []
sys_msg = {"role": "system", "content": "You are a helpful coding assistant."}
messages. append (sys_msg)

while True:
    usr_content = input ("> ")
    usr_msg = {"role": "user", "content": usr_content}
    messages.append (usr_msg)
    response = openai. ChatCompletion. create (model="gpt-3.5-turbo", messages=messages)
    reply = response["choices"][0]["message"]["content"]
    print ("\n"+ reply + "\n")
    assistant_msg = {"role": "assistant", "content":reply}
    messages.append (assistant_msg)
#run at prompt enter >Please explain thi line to me: user_content = input(">")