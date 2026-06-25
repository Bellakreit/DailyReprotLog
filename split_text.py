import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"
model_path = "ibm-granite/granite-4.1-30b"
tokenizer = AutoTokenizer.from_pretrained(model_path)
# drop device_map if running on CPU
model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device)
model.eval()
# change input text as desired
chat = [
    { "role": "user", "content": "
    Rewrite the paragraph below into the exact labeled sections shown, using the same information and a professional tone.
    Do not invent facts, and preserve the meaning of the original content. 
    Use the section labels exactly as shown, and format the output like this:\n\n
    Description: ...\n\n
    Safety: ...\n
    PPE: ...\n\n
    Workers and hours:\n
    jose - 8 hours\n
    maria - 7 hours\n 
    " },
]
chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
# tokenize the text
input_tokens = tokenizer(chat, return_tensors="pt").to(device)
# generate output tokens
output = model.generate(**input_tokens, 
                        max_new_tokens=100)
# decode output tokens into text
output = tokenizer.batch_decode(output)
# print output
print(output[0])
