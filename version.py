import requests

# Define the URL of your FastAPI application
url = 'http://localhost:2000/predict'  # Replace with your actual URL

# Define the input texts as a list
input_texts = [
    "I am tired ",
    "i feel like sleeping",
    "i love food",

]

# Loop through the input texts and send POST requests
for input_text in input_texts:
    # Send a POST request with JSON data
    response = requests.post(url, json={"text": input_text})

    # Check the response
    if response.status_code == 200:
        data = response.json()
        if 'prediction' in data:
            prediction = data['prediction']
            print(f'Prediction for "{input_text}": {prediction}')
        elif 'error' in data:
            error = data['error']
            print(f'Error for "{input_text}": {error}')
        else:
            print(f'Unexpected response format for "{input_text}": {data}')
    else:
        print(f'Request for "{input_text}" failed with status code {response.status_code}')
        print(f'Response content: {response.text}')
