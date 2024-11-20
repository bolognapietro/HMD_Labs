# Natural Language Understanding

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

