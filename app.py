import pickle
from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)

# Load the model from the pickle file
with open('depression_analyzer.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the text input from the pickle file
with open('chat_input.pkl', 'rb') as chat_input_file:
    chat_input = pickle.load(chat_input_file)



# Define a route for predicting depression
@app.route('/predict', methods=['POST'])
def predict_depression():
    try:
        # Get the text data from the request
        data = request.json
        text = data['text']

        # Make predictions using the loaded model
        prediction = model.predict([text])

        # Return the prediction as JSON response
        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
