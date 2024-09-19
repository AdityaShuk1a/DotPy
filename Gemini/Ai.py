import json
import google.generativeai as genai
from datetime import datetime
import requests
import base64

'''

Modules to import:
                json is in-built
                pip install google.generativeai

'''
api_endpoint = "https://api.imagen.com/v1/generate"


headers = {
    "Authorization": f"Bearer {'api key'}"
}


#Add your own API key


genai.configure(api_key="api key")

# Create the model
generation_config = {
  "temperature": 0.1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

'''
    insert the file in string format
'''

# strictly provide the give format only and their should not be a single word instead of this format 
#                                        so i from the given pricture describe the image and give the description in the prompt of the data inside dictionary 
#                                        thats it data = {
#                                       "prompt": "A cat playing with a ball of yarn",
#                                       "style": "watercolor",
#                                       "resolution": "512x512"
#                                       } 
try:

    userFile = genai.upload_file('emoji.jpeg')

    response = model.generate_content([  ''' you guys have launched ImageGen so use it and generate a image using imagen and imagine a cow running on the streets of mumbai'''])

    response_text = response.text

    print(response_text)
    
    # json_start = response_text.find("{")
    # json_end = response_text.rfind("}") + 1
    # cleaned_response = response_text[json_start:json_end]

  

    # #loading the json file
    
    # result_dict = json.loads(cleaned_response)
    # print(result_dict)  
    
    # response = requests.post(api_endpoint, headers=headers, json=result_dict)

    # if response.status_code == 200:
    #     image_data = response.json()["image"]
    #     with open("generated_image.jpg", "wb") as f:
    #         f.write(base64.b64decode(image_data))
    #     print("Image generated successfully!")
    # else:
    #     print("Error generating image:", response.text)

 
   
except Exception as e:
    errorResponse = {'status': 401, 'boolean_status':True, 'message': f'Something went wrong. Error: {str(e)}'}
    print (errorResponse)
