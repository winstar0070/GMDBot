from discord.ext import commands
import json
from wrapper import fetch_meal
import datetime


bot = commands.Bot(command_prefix="")


def __calc_datetime(target: str) -> str:
    if target in ["어제", "오늘", "내일"]:

        if target == "어제":
            date = datetime.datetime.now() + datetime.timedelta(days=-1)
            return date.strftime("%Y%m%d")

        if target == "오늘":
            return datetime.datetime.now().strftime("%Y%m%d")

        if target == "내일":
            date = datetime.datetime.now() + datetime.timedelta(days=1)
            return date.strftime("%Y%m%d")

    return target  # YYYYMMDD 꼴


@bot.event
async def on_ready():
    print(f"Bot Ready. - {bot.user.name}")


@bot.event
async def on_command_error(context, exception):
    if isinstance(exception, commands.CommandNotFound):
        return


@bot.command(name="급식")
async def meal(ctx, args: str = "오늘"):
    meals = await fetch_meal(__calc_datetime(args))
    await ctx.reply(meals)


if __name__ == "__main__":
    with open("config.json", "r") as f:  # config 변수 안에 config.json 불러오기
        config = json.load(f)

    bot.run(config["token"])
