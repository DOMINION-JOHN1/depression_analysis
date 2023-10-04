import requests

# Define the URL of your FastAPI application
url = 'http://localhost:2000/predict'  # Replace with your actual URL

# Define the input texts as a list
input_texts = [
    "I am tired",
    "I feel like sleeping",
    "I love food"
]

# Send a POST request with JSON data
response = requests.post(url, json={"texts": input_texts})

# Check the response
if response.status_code == 200:
    data = response.json()
    if 'prediction' in data:
        prediction = data['prediction']
        print(f'Combined Prediction: {prediction}')
    else:
        print('Response does not contain "prediction" field.')
else:
    print(f'Request failed with status code {response.status_code}')
    print(f'Response content: {response.text}')
