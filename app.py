from nextcord.ext import commands
import json
import Functions

with open('config.json', 'r') as f: # config 변수 안에 config.json 불러오기
    config = json.load(f)

bot = commands.Bot(command_prefix='$') 

@bot.event
async def on_message(message):
    if message.content == "급식":
        await message.reply(Functions.getTodayMeal())
    if "급식" in message.content and "내일" in message.content :
        await message.reply(Functions.getTomorrowMeal())

bot.run(config['token'])