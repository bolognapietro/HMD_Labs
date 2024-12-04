import ollama

prompt = """
        Dialogue state are the values the NLU extracts from user turns.
        A turn is one utterance from either the user or the system
        Generate a dialogue of 4 turns (2 user turns and 3 system turns) 
        that has the following dialogue state bu the end of the 4 turns.
"""

input = """ dialogue_state = {
            "intent": "canederli_ordering",
            "slot": {
                "canederli_type": "meat",
                "canederli_broth": "vegetable",
                "canederli_count": 3
            }
        }
"""