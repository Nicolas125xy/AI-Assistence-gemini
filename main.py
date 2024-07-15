import google.generativeai as genai
import pyttsx3
import speech_recognition as sr

def configure_voice():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 180)  # Ajusta a velocidade da fala
    print("\nLista de Vozes - Verifique o número\n")
    for indice, vozes in enumerate(voices):  # Lista as vozes disponíveis
        print(indice, vozes.name)
    voz = 95  # Escolhe a voz desejada (ajuste conforme necessário)
    engine.setProperty('voice', voices[voz].id)
    return engine

def recognize_speech(r, mic):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Fale algo (ou diga 'desligar')")
        audio = r.listen(source)
        print("Enviando para reconhecimento")
        try:
            texto = r.recognize_google(audio, language="pt-BR")
            print("Você disse: {}".format(texto))
            return texto
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError as e:
            print(f"Erro no serviço de reconhecimento: {e}")
        return ""

def main():
    assistente_falante = True
    ligar_microfone = True

    genai.configure(api_key="YOUR_API_KEY")
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(model.name)

    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    if assistente_falante:
        engine = configure_voice()

    if ligar_microfone:
        r = sr.Recognizer()
        mic = sr.Microphone()

    bem_vindo = "# Bem Vindo ao Gemini AI #"
    print(f"\n{'#' * len(bem_vindo)}")
    print(bem_vindo)
    print(f"{'#' * len(bem_vindo)}")
    print("###   Digite 'desligar' para encerrar    ###\n")

    while True:
        if ligar_microfone:
            texto = recognize_speech(r, mic)
        else:
            texto = input("Digite sua mensagem (ou '#sair' para encerrar): ")

        if texto.lower() == "desligar":
            break

        response = chat.send_message(texto)
        print("Gemini:", response.text, "\n")

        if assistente_falante:
            engine.say(response.text)
            engine.runAndWait()

    print("Encerrando Chat")

if __name__ == '__main__':
    main()
