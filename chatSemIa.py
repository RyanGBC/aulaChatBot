def responder(pergunta):
    pergunta = pergunta.lower()

    if "oi" in pergunta or "ola papi" in pergunta:
        return "Oiee como podemos ajuda-lo?"
    elif "tudo bem" in pergunta or "show namoral" in pergunta:
        return "Tudo na paz e com voce?"
    elif "com quem eu falo" in pergunta:
        return "Voce fala com o chat que mais ajuda no brasil!"
    elif "ajuda" in pergunta:
        return "Claro o que voce precisa?"
    elif "tchau!" in pergunta:
        return "Tchau até mais, se precisar de mais alguma coisa só volta aqui"
    else:
        return "Desculpa não consegui entender o que voce quer, pode repetir?"


def comecar_chatbot():
    print("Chatbot: Olá Digite 'sair para encerrar a conversa")
    while True:
        user = input("Você: ")
        if user.lower() == 'sair':
            print("Chatbot: Tchau até a proxima conversa!")
            break
        resposta = responder(user)
        print(f"Chatbot:{resposta}")


## Iniciar o chatbot
    
if __name__ == "__main__":
    comecar_chatbot()