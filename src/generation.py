from transformers import AutoTokenizer, AutoModelForCausalLM
model_id = "EleutherAI/gpt-neo-1.3B"
tok = AutoTokenizer.from_pretrained(model_id)
gen = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", load_in_4bit=True)

def generate_answer(context, question):
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    inputs = tok(prompt, return_tensors="pt").to(gen.device)
    out = gen.generate(**inputs, max_new_tokens=150)
    return tok.decode(out[0], skip_special_tokens=True)
