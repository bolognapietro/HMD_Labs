#!/bin/bash

# Check if a file name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: sh run.sh <prompt_file>"
    exit 1
fi

# Get the file name from the argument
PROMPT_FILE=$1

# Check if the file exists
if [ ! -f "$PROMPT_FILE" ]; then
    echo "Error: File '$PROMPT_FILE' not found!"
    exit 1
fi

# Run the sbatch command with the provided prompt file
sbatch example.sbatch --reservation=hmd-2024-tue --system-prompt "$(cat "$PROMPT_FILE")" llama2 "I want a cheese pizza" --max_seq_length 1000

# --reservation=hmd-2024-wed