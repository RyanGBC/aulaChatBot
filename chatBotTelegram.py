import telebot
from telebot import types

# Função de resposta a /start
def enviar_mensagem_boas_vindas(message):
    cid = message.chat.id
    print(f"Usuário iniciou o bot: {cid}")
    
    bot.send_message(cid, "Olá! Digite seu token para começar. 🔑")

# Verifica se o token é válido
def verificar_usuario(token):
    # Aqui você pode integrar com seu banco de dados ou sistema de validação
    if token == "seu_token_aqui":
        return True
    else:
        return False

@bot.message_handler(commands=['start'])
def start_handler(message):
    enviar_mensagem_boas_vindas(message)

@bot.message_handler(func=lambda m: True)
def receber_token(message):
    cid = message.chat.id
    token = message.text.strip()

    if verificar_usuario(token):
        bot.send_message(cid, "✅ Token válido. Seja bem-vindo ao chat!")
        # Aqui você pode configurar o menu, salvar estado, etc.
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📊 Ver relatórios")
        btn2 = types.KeyboardButton("⚙️ Configurações")
        markup.add(btn1, btn2)
        bot.send_message(cid, "Escolha uma opção abaixo:", reply_markup=markup)
    else:
        bot.send_message(cid, "❌ Token inválido. Tente novamente.")

# Inicializa o bot
token = "coloque_aqui_o_token_do_seu_bot"
bot = telebot.TeleBot(token)

print("Bot iniciado. 🚀")
bot.polling()
