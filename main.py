import environs
import telebot
from pycoingecko import CoinGeckoAPI
from Comandos import Servicos

env = environs.Env()
env.read_env('.env')
BOT_TOKEN = env('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
coin_client = CoinGeckoAPI()
servicos = Servicos(bot)
servicos.register_handlers()

if __name__ == "__main__":
    bot.polling()
