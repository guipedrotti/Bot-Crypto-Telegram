import telebot
from pycoingecko import CoinGeckoAPI

class Servicos:
    def __init__(self, bot: telebot.TeleBot) -> None:
        self.bot = bot
        self.coin_client = CoinGeckoAPI()

    def start(self, message: telebot.types.Message) -> None:
        self.bot.send_message(
            message.chat.id,
            f"""Olá, sou o CryptoDaily, como posso te ajudar, {message.from_user.first_name}?
            Escolha uma das seguintes opções:
            /criptos - lista de criptomoedas
            /cotacoes - cotação de moedas
            /historico - histórico de cotação
            /favoritos - favoritos
            /sobre - sobre o bot
            /consulta - consulta o preço de uma criptomoeda
            /help - ajuda
            /exit - sair do bot.""",            
        )

    def consulta(self, message: telebot.types.Message) -> None:
        try:
            if len(message.text.split()) < 2:
                self.bot.send_message(
                    message.chat.id,
                    """Por favor, forneça o nome da criptomoeda após o comando /consulta. 
                    Exemplo: /consulta bitcoin"""
                )
                return

            crypto_name = message.text.split()[1].lower()
            price = self.coin_client.get_price(ids=crypto_name, vs_currencies='brl')

            if price and crypto_name in price:
                self.bot.send_message(
                    message.chat.id,
                    f'O preço atual de {crypto_name} é R${price[crypto_name]["brl"]}'
                )
            else:
                self.bot.send_message(
                    message.chat.id,
                    f'Não consegui encontrar informações para {crypto_name}.'
                )
        except Exception as e:
            self.bot.send_message(
                message.chat.id,
                'Ocorreu um erro na consulta. Por favor, tente novamente.'
                )

    def help(self, message: telebot.types.Message) -> None:
        self.bot.send_message(
            message.chat.id, 
            """Aqui está a lista de comandos disponíveis: 
            /criptos - lista de criptomoedas
            /cotacoes - cotação de moedas
            /historico - histórico de cotação
            /favoritos - favoritos
            /sobre - sobre o bot
            /consulta - consulta o preço de uma criptomoeda
            /exit - sair do bot."""
            )

    def register_handlers(self) -> None:
        self.bot.message_handler(commands=['start'])(self.start)
        self.bot.message_handler(commands=['help'])(self.help)
        self.bot.message_handler(commands=['consulta'])(self.consulta)
