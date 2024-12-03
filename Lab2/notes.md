# Lab 2 - Natural Language Understanding

## Example

### Utterance:
* **UTT**: "I want a cheese pizza"
* **INTENT**: Pizza ordering
* **SLOT required for intent**: *pizza_type*
                                *pizza_count*
                                *pizza_size*
                                *pizza_dough*

### Structure:
```json
{
    intent: "pizza_ordering",
    slot: {
        pizza_type: "cheese",
        pizza_count: one,
        pizza_size: null
    }
    sentiment: "",
}
```

### Prompt:
*WHAT*:\
a. Classify intention (pre_defines)\
b. Extract slot values (also detect null)\
c. Return JSON\
d. Sentiment

*HOW*:\
a. examples *{0,1,few}-shot*\
b. closed/open questions


## Canederli
**Extract slot**

* broth o not,
* type of canederli: speck, herbs, mushrooms
* vegetarian or not
* cheese on top
* count, number of canederli

```json
{
    intent: "canederli_ordering",
    slot: {
        canederli_type: {"speck", "cheese", "herb", "mushroom"},
        canederli_broth: {"vegetable", "meat", null},
        canederli_cheese_on_top: {"yes", "no"},
        canederli_spiece: {"black pepper", "smoked paprika", "cumin", null}
        canederli_gluten: {"yes", "no"},
        canederli_count: {1, 2, ...},
        canederli_size: {"small", "medium", "large"},
    }
}
```

**Prompt**


First, identify the user intent.
If the intent is canederli_ordering, extract the slots values from the input of the user.
The slots are: [canederli_type, canederli_broth, canederli_cheese_on_top, canederli_spiece, canederli_gluten, canederli_count, canederli_size].
In no values are present in the user input you have to put null as the value.
Output them as a json.
