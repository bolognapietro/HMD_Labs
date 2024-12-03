import os
import ollama

def query_model(model_name, system_prompt, input_text, max_seq_len=128):


    messages = [{
                    'role':'system',
                    'content': system_prompt
                }]
    if input_text:
        messages.append({
            'role': 'user',
            'content': input_text
        })

    # print(messages)
    response = ollama.chat(model=model_name, messages=
        messages
    )
    return response['message']['content']



if __name__ == '__main__':
    
    with open('Lab4/sys_prompt_NLU.txt', 'r') as file:
        NLU_system_prompt = file.read()
    with open('Lab4/sys_prompt_DM.txt', 'r') as file:
        DM_system_prompt = file.read()
    with open('Lab4/sys_prompt_NLG.txt', 'r') as file:
        NLG_system_prompt = file.read()

    while True:
        input_NLU = input("User input: ")# "I want to order meat canederli"
        input_DM = query_model("llama3.2", NLU_system_prompt, input_NLU)
        input_NLG = query_model("llama3.2", DM_system_prompt, input_DM)
        output = query_model("llama3.2", NLG_system_prompt, input_NLG)
        print(output)