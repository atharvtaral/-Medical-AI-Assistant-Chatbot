# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# # Load .env file
# load_dotenv()

# # Get API key
# api_key = os.getenv("OPENAI_API_KEY")

# # Create OpenAI client
# client = OpenAI(api_key=api_key)

# print("Simple AI Chatbot")
# print("Type 'exit' to stop.\n")

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         print("Chatbot: Goodbye!")
#         break

#     # Send message to OpenAI
#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful AI teacher."},
#             {"role": "user", "content": user_input}
#         ]
#     )

#     # Extract response
#     bot_reply = response.choices[0].message.content

#     print(f"Chatbot: {bot_reply}\n")





# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# # 1. Load .env file
# load_dotenv()

# # 2 load api key
# my_api_key=os.getenv("OPENAI_API_KEY")

# # 3. create client
# client = OpenAI(api_key=my_api_key)
# # OpenAI() = class constructor
# # client = object

# print("Simple AI Chatbot")
# print("Type exit to stop.\n")

# while True:
#     user_input = input("you: ")

#     if user_input.lower()=="exit":
#         print("Chatbot:goodbey")
#         break

#     else:
#         # send msg to openai
#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             messages=[
#                 {"role":"system","content":"you are a helpful AI teacher"},
#                 {"role":"user","content":user_input}
#             ]
#         )
#         #extract response
#         ext_res = response.choices[0].message.content

#         print(f"Chatbot: {ext_res}\n")



# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# # 1. load .env file 
# load_dotenv()

# #2. aoi_key
# api_key = os.getenv("OPENAI_API_KEY")

# # 3. create client connection
# client = OpenAI(api_key=api_key)

# print("Simple  AI  Chatbot")
# print("Type exit to stop \n")

# while True:
#     user_input=input("you: ")

#     if user_input.lower()=="exit":
#         print(f"Chatbot:goodbey")
#         break

#     else:
#         response =client.chat.completions.create(
#             model = "gpt-4.1-mini",
#             messages=[
#                 {"role":"system","content":"you are a healpful ai assistant"},
#                 {"role":"user","content":user_input}
#             ]
#         )

#         ext_res = response.choices[0].message.content
#         print(f"Chatbot: {ext_res}")
    








# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# # 1. load .env file
# load_dotenv()

# # 2. Api key
# api = os.getenv("OPENAI_API)KEY")

# # 3. create client connection
# client = OpenAI(api_key = api)

# print("Simple AI Chatbot")
# print("Type 'exit' to stop\n")

# while True:
# 	user_input = input("you: ")

# 	if user_input.lower()=="exit":
# 		print("Chatbot : Good Bey")
# 		break
	
# 	else:
# 		response = client.chat.completions.create(
# 			model = "gpt-4.1-mini",
# 			temperature=0.7,
# 			messages = [
# 				{ "role":"system","content":"You are a helpful AI assistant"},
# 				{"role":"user","content":user_input}
# 				]
# 			)
			
# 		ext_output = response.choices[0].message.content
# 		print(f"Chatbot: {ext_output}\n")




# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# # 1. load .env file
# load_dotenv()

# # 2. load api key
# open_ai_api_key = os.getenv("OPENAI_API_KEY")

# # 3. create connection
# client = OpenAI(api_key=open_ai_api_key)

# print("Simple AI Chatbot")
# print("type exit when close.\n")

# while True:
# 	user_input = input("You: ")

# 	if user_input.lower()=="exit":
# 		print("Chatbot:GoodBey!!!")
# 		break

# 	else:
# 		response = client.chat.completions.create(
# 			model="gpt-4o-mini",
# 			temperature=0.5,
# 			messages=[
# 				{"role":"system","content":"Act as a professional Medical Consultant. Analyze my symptoms, provide empathetic health advice, and at the end of your response, always provide a structured prescription including recommended precautions and general medication."},
# 				{"role":"user","content":user_input}
# 			]
# 		)

# 		extract = response.choices[0].message.content

# 		print(f"Chatbot: {extract}.\n")




#### Adding Chatbot History ####

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()
# api = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=api)

# message_history = [
# 	{
# 		"role":"system",
#   		"content":("Act as a professional Medical Consultant. Analyze my symptoms, provide empathetic health advice, and at the end of your response, always provide a structured prescription including recommended precautions and general medication."
# 	)
#   }
# ]

# print("--- Medical AI Chatbot (with Memory) ---")
# print("Type 'exit' to close.\n")

# while True:

# 	user_input=input("You: ")

# 	if user_input.lower()=="exit":
# 		print("Chatbot:GoodBey!!!")
# 		break

# 	else: 
# 		message_history.append(
# 			{
# 				"role":"user","content":user_input
# 			} 
# 		)

# 		response = client.chat.completions.create(
# 				model = "gpt-4o",
# 				temperature=0.5,
# 				messages=message_history
# 		)

# 		extract = response.choices[0].message.content

# 		message_history.append({"role":"assistant","content":extract})
		
# 		print(f"CHatbot: {extract}.\n")
# 		print("-"*100)


### Deploy on Gradio this chatbot ###
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_message = {
    "role": "system",
    "content": (
        "Act as a professional Medical Consultant. Analyze my symptoms, "
        "provide empathetic health advice, and at the end of your response, "
        "always provide a structured prescription including recommended "
        "precautions and general medication."
    )
}

def medical_chatbot(user_input, chat_history):
    if not user_input:
        return "", chat_history
        
    messages = [system_message]
    
    for msg in chat_history:
        messages.append({"role": msg["role"], "content": msg["content"]})

    new_user_message = {"role": "user", "content": user_input}
    messages.append(new_user_message)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.5,
        messages=messages
    )

    bot_message_text = response.choices[0].message.content
    new_bot_message = {"role": "assistant", "content": bot_message_text}

    chat_history.append(new_user_message)
    chat_history.append(new_bot_message)

    return "", chat_history

with gr.Blocks() as demo:
    gr.Markdown("# 🏥 Medical AI Assistant")
    gr.Markdown("Describe your symptoms to get a professional medical consultation.")

    chatbot = gr.Chatbot(label="Doctor's Consultation")
    
    # Using gr.Row to put Textbox and Submit button on the same line
    with gr.Row():
        msg = gr.Textbox(
            label="Enter Symptoms / Query", 
            placeholder="e.g. I have a mild fever since yesterday...",
            scale=4  # Makes the textbox wider
        )
        submit_btn = gr.Button("Submit", variant="primary", scale=1) # "primary" makes it colorful (blue)

    clear = gr.Button("Clear Chat")

    # Action 1: When user presses Enter
    msg.submit(medical_chatbot, [msg, chatbot], [msg, chatbot])
    
    # Action 2: When user clicks the Submit button
    submit_btn.click(medical_chatbot, [msg, chatbot], [msg, chatbot])
    
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft(), share=True)





