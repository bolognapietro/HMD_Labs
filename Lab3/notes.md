## Recap
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



# TODO
**Slots**\
[canederli_type, canederli_broth, canederli_cheese_on_top canederli_spiece, canederli_gluten, canederli_count, canederli_size]

