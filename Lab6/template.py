from itertools import product

template1 = [
            "I would like to order {} {} canederli with {} broth.",
            "I want {} {} canederli with {} broth.",
            "Could I have {} {} canederli and {} broth?",
            "Hi, can I get just {} {} canederli with {} broth?",
            "Excuse me, I would like to order {} {} canederli with {} broth.",
            ]

ds = {
        "intent": "canederli_ordering",
        "slot": {
            "canederli_type": "",
            "canederli_broth": "",
            "canederli_size": None,
            "canederli_count": ""
        }
    }

canederli_count = ["a", "one", "2", "two"]
canederli_type = ["meat", "cheese", "spinach"]
canederli_broth = ["chicken", "beef", "vegetable"]

for utt in template1:
    for count, ttype, broth in product(canederli_count, canederli_type, canederli_broth):
        filled_template = utt.format(count, ttype, broth) 
        ds["slot"]["canederli_count"] = count
        ds["slot"]["canederli_type"] = ttype
        ds["slot"]["canederli_broth"] = broth
        print(filled_template)
        # print(ds)
        print()