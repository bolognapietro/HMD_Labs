# Evaluation

Two categories:
1. Intrinsic
2. Extrinsic

### 1. Intrinsic
Evaluate the internal performance of the pipeline. Some are:
- Accuracy (for the DM - next best action accuracy)
- F1 score

Generate with an LLM --> (istruction/example/meaning_representation, dialogue state) --> |Simulator - LLM| --> text generation (4 or 6 term dialogue)   (x50)

If you don't have LLM use **String Injection**:
- give a template and brute force all contiributions
- number: 50

### 2. Extrinsic
We see only one type:
- Human evaluation (evaluate user experience)

**How we can evaluate the performance?**
User experience (UX) questions\
--> at least 5 questions for 5 user

It affects all the 5 components:
- 1 question NLU
- 1 question DM
- 1 question NLG
- 1 question engagement
- 1 overall question (*would you use it again?*)

USE THIS AS A SUGGESTION (from 0 to 5)\
Use a critical thinking about the range of marks (0.5, 0-1)

**NOTE: First implement extrinsic evaluation**