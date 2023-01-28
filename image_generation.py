################################################################################
#                                                                              #
#   Full video tutorial at: https://youtu.be/yNSo6cWpDSM                       #
#                                                                              #
#               Data Science Garage at Youtube.com                             #
#                 (vytautas.bielinskas@gmail.com)                              #
#                                                                              #
################################################################################

import openai

openai.api_key = '<YOUR_OPENAI_API_KEY'  # generate it at: https://beta.openai.com/account/api-keys

response = openai.Image.create(
    prompt = "Small letters PATRI STYLE in fire",
    n = 1,
    size = "1024x1024"
)

image_url = response['data'][0]['url']

print(image_url)
