import openai

openai.api_key = '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'

response = openai.Image.create(
    prompt = "Small letters PATRI STYLE in fire",
    n = 1,
    size = "1024x1024"
)

image_url = response['data'][0]['url']

print(image_url)
