import openai

openai.api_key = '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'

prompt = "\"\"\"\nCreate an array of weather temperatures for Paris \n\"\"\""

response = openai.Completion.create(
        model = 'text-davinci-002',
        prompt = prompt,
        max_tokens = 256,
        temperature = 0,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )

print(response)
