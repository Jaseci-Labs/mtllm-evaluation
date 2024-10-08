import ollama


prompt = """Given the fields `question`, produce the fields `answer`.

---

Follow the following format.

Question: ${question}
Reasoning: Let's think step by step in order to ${produce the answer}. We ...
Answer: ${answer} (Respond with a single int value)

---

Question: Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?
Reasoning: Let's think step by step in order to"""

client = ollama.Client(host="http://141.212.106.90:8080")
# ollama.set_config({"host": "http://141.212.106.90", "port": 8080})
response = client.chat(model='llama2:70b', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])
print(response['message']['content'])
