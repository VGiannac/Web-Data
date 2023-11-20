#api_handler.py
import requests
import pandas as pd

class ApiHandler:
    def __init__(self, base_url="https://opentdb.com/api.php"):
        self.base_url = base_url

    def get_data(self, amount=10, question_type="multiple"):
        params = {"amount": amount, "type": question_type}
        response = requests.get(self.base_url, params=params)
        data = response.json()
        return data

    def format_data(self, data):
        # Assuming the API response has a 'results' key containing a list of questions
        results = data.get('results', [])

        if not results:
            return pd.DataFrame()  # Return an empty DataFrame if there are no results

        # Extract questions and answers from the API response
        questions = [result.get('question', 'N/A') for result in results]
        answers = [result.get('correct_answer', 'N/A') for result in results]

        # Create a DataFrame
        formatted_df = pd.DataFrame({'Question': questions, 'Answer': answers})

        return formatted_df
