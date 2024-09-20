import google.generativeai as genai

genai.configure(api_key="sua-api-key")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

print("\nOlá! Bem-vindo ao assistente virtual.")
print("Digite 'sair' a qualquer momento para encerrar o chat.")
print("Como posso ajudar você hoje?")

while True:
    
    user_ask = input("Você: ").lower()
    if user_ask.lower() == "sair":
            print("Obrigado por usar o assistente virtual. Até logo!")
            break

    response = chat.send_message(user_ask)
    print("Gemini:", response.text, "\n")

