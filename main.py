from os import getenv
from dotenv import load_dotenv
from bot import bot


load_dotenv()

token = getenv("BOT_TOKEN")
if token is None or token == "":
    raise Exception("Bot token not set.")

bot.run(token)
