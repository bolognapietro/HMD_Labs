# Lab 4 - Pipeline

User input -> [NLU] -> Meaning representation -> [DM] -> NBA -> [NLG] -> System response
- *NLU* (info extraction): 
    - intent classification
    - slot values extraction 
    
- *DM* (decision making):
    - NBA prediction
    - System action
- *NLG* (lexicalization):
    - Response generation

### Example
user input -> req_for_info -> confirmation

#### Input1
First, identify the user intent. 
If the intent is canederli_ordering, extract the slots values from the input of the user. 
The slots are: [canederli_type, canederli_broth, canederli_cheese_on_top, canederli_spiece, canederli_gluten, canederli_count, canederli_size]. 
In no values are present in the user input you have to put null as the value. 
Output them as a json, I want JUST the json in the following format and no other words.
{
    "intent": "",
    "slots": {
        "": ,
        "": 
    }
}

#### Output 1 = Input2
{
    "intent": "canederli_ordering",
    "slots": {
        "canederli_type": "meat",
        "canederli_broth": null,
        "canederli_cheese_on_top": null,
        "canederli_spiece": null,
        "canederli_gluten": null,
        "canederli_count": null,
        "canederli_size": null
    }
}


## Question
### User input 
"I want to order **3** **meat canederli** with **vegetable broth**, ***no cheese on top*** and **pepper as spiece**. They should be ***gulten free*** and of **small size**."

### NLU
```json
{
    "intent": "canederli_ordering",
    "slots": {
        "type": "meat",
        "broth": "vegetable",
        "cheese_on_top": null,
        "spiece": "pepper",
        "gluten": null,
        "count": 3,
        "size": "small"
    }
}
```

### DM
```json
{
    "NLU": {
        "intent": "canederli_ordering",
        "slots": {
            "type": "meat",
            "broth": "vegetable",
            "cheese_on_top": null,
            "spiece": "pepper",
            "gluten": null,
            "count": 3,
            "size": "small"
        }
    },
    "DM": {
        "next_best_action": "confirmation(intent=canederli_ordering)"
    }
}
```

### NLG
"Would you like to add cheese on top of your Canederli? (yes/no)"