import pytesseract
from PIL import Image
import os
import openai
import google.generativeai as genai
from datetime import datetime
import json

# Set your OpenAI API key (ensure the environment variable is set)
"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""



genai.configure(api_key="")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
 
)

chat_session = model.start_chat(
  history=[]
)

# response = chat_session.send_message(" brother kese ho")


try:
    #user file is the file which is inserted by the user
    userFile = genai.upload_file('blue2.jpg')
    response = model.generate_content([userFile,'''context = {strictly just provide the json string format else not a single 
                                       word in your prompt and format is this result = {"status": 200,"response": {"supplier_name": None,
                "gst_number": None, "products":[{"product_name":"test","quantity":2,"rate":250.00,"item_total":500.00},{"product_name":"test","quantity":2,"rate":250.00,"item_total":500.00}]
                "date_of_purchase": None,"grand_total": None,"cgst": None,"sgst": None,"igst": None,"total_amount": None}}
        also set the date_of_purchase format as date/month/year  for example if the date is 11.09.24 set 11/09/24
        also total amount is not the total tax amount so if there is no total amount just take the grand total as the total amount
        go through the text carefully and check the last total amount which the user had to pay and see the sgst and igst and cgst carefully map it }'''])
    #display the response
    response_text = response.text
    print(type(response_text), end='\n')
    #triming the extra string part if any to convert the main content in form of json
    json_start = response_text.find("{")
    json_end = response_text.rfind("}") + 1
    cleaned_response = response_text[json_start:json_end]
    try:
        #loading the json file
    
        result_dict = json.loads(cleaned_response)
        print(type(result_dict))  
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    #converting normal string date to epoch date and updating the new date format
    strDate = result_dict['response']['date_of_purchase']
    strDate = datetime.strptime(strDate, '%d/%m/%Y')
    purchaseDate = int(strDate.timestamp())
    result_dict['response']['date_of_purchase'] = purchaseDate
    print(result_dict)
except Exception as e:
    errorResponse = {'status': 401, 'boolean_status':True, 'message': f'Something went wrong. Error: {str(e)}'}
    print (errorResponse)