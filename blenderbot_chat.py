import gradio as gr
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load model
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Chat function
def chat(message, history):
    inputs = tokenizer([message], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    history.append((message, reply))
    return history, ""   # return empty string to clear textbox

# Gradio UI
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Type your message here...")
    clear = gr.Button("Clear")

    # return history (for chatbot) and "" (to reset textbox)
    msg.submit(chat, [msg, chatbot], [chatbot, msg])
    clear.click(lambda: ([], ""), None, [chatbot, msg])  # clears both

demo.launch()
