import openai

openai.api_key = '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'

prompt = """
What are lyrics of DJ Tiesto 10:35 song?
"""

response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 100,
        temperature = 0
    )

print(response)
