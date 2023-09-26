import requests
# Define the URL of your FastAPI application
url = 'http://0.0.0.0:2000/predict'  # Replace with your actual URL

# Define the input text
input_text =input('Your input text: ')

# Send a POST request with JSON data
response = requests.post(url, json={"text": input_text})

# Check the response
if response.status_code == 200:
    data = response.json()
    if 'prediction' in data:
        prediction = data['prediction']
        print(f'Prediction: {prediction}')
    elif 'error' in data:
        error = data['error']
        print(f'Error: {error}')
else:
    print(f'Request failed with status code {response.status_code}')