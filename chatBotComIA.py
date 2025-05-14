import openai


#insira sua chave API da Open AI aqui
openai.api_key = "#"


def perguntar_gpt(pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente muito educado!"},
            {"role": "user", "content": pergunta}
        ]
    )

    return resposta.choises[0].messages['content']

def comecar_chatbot():
    print("Chatbot: Olá Digite 'sair para encerrar a conversa")
    while True:
        user = input("Você: ")
        if user.lower() == 'sair':
            print("Chatbot: Tchau até a proxima conversa!")
            break
        resposta = perguntar_gpt(user)
        print(f"Chatbot:{resposta}")

if __name__ == "__main__":
    comecar_chatbot()
