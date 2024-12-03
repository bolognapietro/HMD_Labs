import subprocess
import time
import re
import os
import json

def extract_json_block(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        # Find the start of the JSON block (assumes it starts with '{')
        start_index = content.find('cpu.')
        if start_index != -1:
            # Write the JSON block to the output file
            outfile.write(content[start_index+5:])

def convert_out_to_txt(out_file, txt_file):
    try:
        with open(out_file, 'r') as infile, open(txt_file, 'w') as outfile:
            content = infile.read()
            outfile.write(content)
        print(f"Converted '{out_file}' to '{txt_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{out_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def wait_file(file_path, interval=2):
    while 1:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                print("Checking file content...")
                print(content)
                
                match = re.search(r'\{', content, re.DOTALL)
                if match:
                    return 
        except Exception as e:
            print(f"Error reading the file: {e}")
            
        time.sleep(interval)

    print("Timeout reached. Dictionary not found.")
    return None

def run_bash_script(script_path, file1, file2):
    try:
        # Run the Bash script with the file arguments
        result = subprocess.run(['bash', script_path, file1, file2], check=True, text=True, capture_output=True)
        print("Script output:")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the script: {e}")
        print("Script error output:")
        print(e.stderr)

#! First Iteration
# Paths to your Bash script and text files
bash_script_path = 'Lab4/run.sh'
file1 = 'Lab4/sys_prompt_NLU.txt'
file2 = input("Enter the user input: ")
# Run the Bash script
id = run_bash_script(bash_script_path, file1, file2)

#! Second Iteration
match = re.search(r'Submitted batch job (\d+)', id)
id = match.group(1)
out_file = f"hmd_example-{id}.out"
txt_file = f"hmd_example-{id}-nc.txt"
wait_file(out_file)

convert_out_to_txt(out_file, txt_file)
extract_json_block(txt_file, f"hmd_example-{id}.txt")
os.remove(txt_file)

# Paths to your Bash script and text files
file1 = 'Lab4/sys_prompt_DM.txt'
file2 = f"hmd_example-{id}.txt"
# Run the Bash script
id = run_bash_script(bash_script_path, file1, file2)
os.remove(file2)

#! Third Iteration
match = re.search(r'Submitted batch job (\d+)', id)
id = match.group(1)
out_file = f"hmd_example-{id}.out"
txt_file = f"hmd_example-{id}-nc.txt"
wait_file(out_file)

convert_out_to_txt(out_file, txt_file)
extract_json_block(txt_file, f"hmd_example-{id}.txt")
os.remove(txt_file)

# Paths to your Bash script and text files
file1 = 'Lab4/sys_prompt_NLG.txt'
file2 = f"hmd_example-{id}.txt"
# Run the Bash script
id = run_bash_script(bash_script_path, file1, file2)
os.remove(file2)