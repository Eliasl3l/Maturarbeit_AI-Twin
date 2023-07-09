import openai
openai.api_key = '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'  # Replace with your OpenAI API key
language = 'en'

def get_chatgpt_response(query):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=query,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()

print(get_chatgpt_response("What's the weather like today?"))