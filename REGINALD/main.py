
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from data import personality_reginald
# Import for the GUI
from chatbot_gui import ChatbotGUI

chatbot = ChatBot("Reginald")

trainer_personality_reginald = ListTrainer(chatbot)
trainer_personality_reginald.train(personality_reginald)

''' ******************* GUI Below Engine Above **************** '''

# creating the chatbot app
app = ChatbotGUI(
    title="A Chat with Reginald",
    gif_path="skeleton.gif",
    show_timestamps=True,
    default_voice_options={
        "rate": 135,
        "volume": 1,
        "voice_id": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    }
)


# define the function that handles incoming user messages
@app.event
def on_message(chat: ChatbotGUI, text: str):

    # print the text the user entered to console
    print("User Entered Message: " + text)             
    
    ''' Here you can intercept the user input and override the bot
    output with your own responses and commands.'''
    # if the user send the "clear" message clear the chats
    if text.lower().find("erase chat") != -1:
        chat.clear()
    # user can say any form of bye to close the chat.
    elif text.lower().find("bye") != -1:
        def close():
            chat.exit()
        chat.send_ai_message("Finally! Leave me alone now!", callback=close)
    else:
        # offload chat bot processing to a worker thread and also send the result as an ai message
        chat.process_and_send_ai_message(chatbot.get_response, text)


# run the chat bot application
app.run()
