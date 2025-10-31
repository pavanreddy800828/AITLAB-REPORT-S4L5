Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import openai
... openai.api_key = "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"
... messages = []
... system_msg = input("What type of chatbot would you like to create?\n")
... messages.append({"role": "system", "content": system_msg})
... print("Your new assistant is ready! Type your query")
... while input != "quit()":
... message = input()
... messages.append({"role": "user", "content": message})
... response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
... reply = response["choices"][0]["message"]["content"]
... messages.append({"role": "assistant", "content": reply})
