#!/bin/bash

# Check the number of arguments
if [ "$#" -ne 2 ]; then
    exit 1
fi

PROMPT_FILE_OR_STRING=$1
INPUT_FILE_OR_STRING=$2

# Determine if the first argument is a file or a string
if [ -f "$PROMPT_FILE_OR_STRING" ]; then
    SYSTEM_PROMPT=$(cat "$PROMPT_FILE_OR_STRING")
else
    SYSTEM_PROMPT="$PROMPT_FILE_OR_STRING"
fi

# Determine if the second argument is a file or a string
if [ -f "$INPUT_FILE_OR_STRING" ]; then
    INPUT_CONTENT=$(cat "$INPUT_FILE_OR_STRING")
else
    INPUT_CONTENT="$INPUT_FILE_OR_STRING"
fi

# Run the sbatch command
sbatch example.sbatch --system-prompt "$SYSTEM_PROMPT" llama2 "$INPUT_CONTENT" --max_seq_length 1000
