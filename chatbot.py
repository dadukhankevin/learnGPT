import openai

openai.api_key = "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"

system_prompt = "You are LearnGPT, an AI with incredible knowledge on every topic."


prompt = """write a quizlet study set about topic and keep it in this json format:
"item1": {
    "term": "term",
    "definition": "definition"
  },
  """

def create_set(topic):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt.replace("topic", topic)}
        ]
    )
    return response
print(create_set('quantum_physics'))