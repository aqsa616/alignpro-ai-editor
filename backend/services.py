import openai

class AIFunctions:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def format_text(self, text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Please format the following text:\n" + text,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    def check_grammar(self, text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Check the grammar of the following text:\n" + text,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    def get_suggestions(self, text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Provide suggestions for improving the following text:\n" + text,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    def summarize_text(self, text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Summarize the following text:\n" + text,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    def rewrite_text(self, text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Rewrite the following text:\n" + text,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()