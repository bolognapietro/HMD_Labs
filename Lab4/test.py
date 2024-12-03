import ollama

prompt = '''
        How are you doing today?
        '''

response = ollama.chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': prompt
    }
])

print(response['message']['content'])