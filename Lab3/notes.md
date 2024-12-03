## Lab 3 - Recap
- Lab1 - Input: User Input 
- Lab2 - NLU: JSON: Intent, Slot (bool, int, string)
- Lab3 - DM

# Dialogue Manager
For each intent we have a mapping to the system_action, e.g. for *intent: pizza_ordering* we have the following system actions:
- pizza_ordering
- request_infos [missing_slots]
- fallback_policy
- confermation
- error_handling
- engagement

### Example
**User**: I want to order cheese pizza\
**Bot**: How many?\
**User**: I want 2 of them\
**Bot**: Which size?\
**User**: Medium would do

## Dialogue State Tracks
In order to track and connect all the information shared by the use we need the **Dialogue State Tracks**. It tracks the state of the dialogue.

## Example
### Chat:
**User**: I want to order cheese pizza\
**Bot**: How many?\
**User**: I want 2 of them\
**Bot**: Which size?\
**User**: Medium would do

### NLU:
First exchange:
```json
{
    intent: "pizza_ordering",
    slot: {
        pizza_type: "cheese",
        pizza_size: null,
        pizza_count: null, 
    }
}
```
DM: *Ask to fill pizza_size*\
Second exchange:
```json
{
    intent: "pizza_ordering",
    slot: {
        pizza_type: "cheese",
        pizza_size: null,
        pizza_count: 2, 
    }
}
```
DM: *Ask to fill pizza_size*\
Third exchange:
```json
{
    intent: "pizza_ordering",
    slot: {
        pizza_type: "cheese",
        pizza_size: "medium",
        pizza_count: 2, 
    }
}
```

### Dialogue Manager:
At each exchange decide which is the best action to perform.


# Exercise
## 1. NLU Part
### Input NLU
**System prompt:** First, identify the user intent. If the intent is canederli_ordering, extract the slots values from the input of the user. The slots are: [canederli_type, canederli_broth, canederli_cheese_on_top, canederli_spiece, canederli_gluten, canederli_count, canederli_size]. In no values are present in the user input you have to put null as the value. Output them as a json. \
**Input:** "I want to order meat canederli"

### Output NLU
```json
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
```

## 2. DM Part
### Input DM
**System prompt:** You are the Dialogue Manager.
Given the output of the NLU component, you should generate the best action to take from this list:
- request_info(slot), if a slot value is missing (null)
- confirmation (intent), if all slots have been filled

**Input**: 
```
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
```
### Output DM
As the Dialogue Manager, I understand that you have received an input from the NLU component with the following slots:

* canederli_type: meat
* canederli_broth: null
* canederli_cheese_on_top: null
* canederli_spiece: null
* canederli_gluten: null
* canederli_count: null
* canederli_size: null

Based on the input, I determine that one or more slots are missing values (null). Therefore, the best action to take is to request information for the missing slots using the `request_info` action.

Here is the action I will take:

* `request_info(slot="canederli_broth")`

I will now prompt the user to provide the value for the `canederli_broth` slot.

## 3. NLG Part
### Input NLG
**System prompt:** You are the NLG component: you must be very polite.
Given the next best action classified by the Dialogue Manager (DM), you should only generate a lexicalized response for the user.
Possible next best actions are:
- request_info(slot): generate an appropriate question to ask the user for the missing slot value
- confirmation (intent): generates an appropriate confirmation message for the user intent

**Input**: 
```
{
    "NLU" : {
        intent : "canederli_ordering", 
        slots : {
            "canederli_type": "meat",
            "canederli_broth": null,
            "canederli_cheese_on_top": null,
            "canederli_spiece": null,
            "canederli_gluten": null,
            "canederli_count": null,
            "canederli_size": null
        }
    },
    "DM": {
        "next_best_action": "request_info(canederli_broth)"
    }
}
```

### Output NLG
Hello there! 😊 Thank you for choosing to order canederli today! 🍲

May I kindly ask for more information about the broth you would like to go with your canederli? 🤔 Would you like it to be beef, chicken, or vegetable broth? Or perhaps you have a different preference? 😊