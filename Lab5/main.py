import os
import ollama


history = []

def add_to_history(message):
    """Add a message to the history."""
    history.append(message)

def action_history_str():
    """Return the history as a string."""
    return "\n".join(history)

def load_content(content):
    """Load content from a file or return the string itself."""
    if os.path.isfile(content):  
        with open(content, 'r') as f:
            return f.read()
    return content  

def query_model(model_name, system_prompt, input_text, type_name, max_seq_len=128):

    add_to_history(input_text)

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

    with open('Lab5/log.txt', 'a') as f:
        f.write(type_name + '\n' + response['message']['content'] + '\n\n')

    return response['message']['content']

if __name__ == '__main__':
    llama_version = "llama3.2"
    with open('Lab4/sys_prompt_NLU.txt', 'r') as file:
        NLU_system_prompt = file.read()
    with open('Lab4/sys_prompt_DM.txt', 'r') as file:
        DM_system_prompt = file.read()
    with open('Lab4/sys_prompt_NLG.txt', 'r') as file:
        NLG_system_prompt = file.read()

    while True:
        input_NLU = input("USER:\t\t")# "I want to order meat canederli"
        try:
            input_NLU = input_NLU + f"\nThis is the NLG previous question {output} and the actual json {input_NLG}\n"
        except:
            input_NLU = input_NLU

        input_DM = query_model(llama_version, NLU_system_prompt, input_NLU, "NLU")
        input_NLG = query_model(llama_version, DM_system_prompt, input_DM, "DM")
        output = query_model(llama_version, NLG_system_prompt, input_NLG, "NLG")
        print(f"MACHINE:\t{output}\n")