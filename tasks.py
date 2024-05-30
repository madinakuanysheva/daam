import transformers
import torch
import json

f = open("custom_insutrctions.txt", "r")
content = f.read()

model_id = "meta-llama/Meta-Llama-3-70B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="auto",
)

def get_task(social_problem: str, topics: str):
    messages = [
        {"role": "system", "content": content},
        {"role": "user", "content": f"Want to learn {topics}. Social problem: {social_problem}"},
    ]

    prompt = pipeline.tokenizer.apply_chat_template(
            messages, 
            tokenize=False, 
            add_generation_prompt=True
    )

    terminators = [
        pipeline.tokenizer.eos_token_id,
        pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = pipeline(
        prompt,
        max_new_tokens=256,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
    
    generated_text = outputs[0]["generated_text"][len(prompt):]
    return generated_text


def check_task(task_itself: str, submitted_code: str) :
    messages = [
        {"role": "system", "content": content},
        {"role": "system", "content": f"{task_itself}."},
        {"role": "user", "content": submitted_code + "\nGive the result in the json format like {'result': True/False}"}
    ]

    prompt = pipeline.tokenizer.apply_chat_template(
            messages, 
            tokenize=False, 
            add_generation_prompt=True
    )

    terminators = [
        pipeline.tokenizer.eos_token_id,
        pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = pipeline(
        prompt,
        max_new_tokens=256,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
    
    generated_text = outputs[0]["generated_text"][len(prompt):]
    return json.loads(generated_text)