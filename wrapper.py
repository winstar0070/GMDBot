from aiohttp import ClientSession
from discord import Embed


async def fetch_meal(date: str):
    url = f"https://school.ch1ck.xyz/api/meal?edu=J10&school=7530892&date={date}"  # &date=20211220 와 같이 &date=YYYYMMDD 형식으로 리퀘 보낼 경우, 특정 일자 급식 정보 받아올 수 있음.

    async with ClientSession() as session:
        async with session.get(url) as resp:
            school_menu = await resp.json(encoding="utf-8")

    embed = Embed()

    try:
        embed.title = f"{date}의 {school_menu[0]['code'][1]}은 놀랍게도 {school_menu[0]['calorie']} 이에요!"
        meal_message = ""

        for meal in school_menu[0]["menu"]:  # 향상된 for문
            meal_message += f"{str(meal['name'])} "
            allergy_all = ", ".join(meal["allergy"])  # 각 메뉴당 알러지 정보 추가.

            if not allergy_all == "":
                meal_message += f"({allergy_all})"  # 각 급식 메뉴마다 알러지 정보 추가

            meal_message += "\n"  # 그리고 \n (Enter)

        embed.description = meal_message.replace("**", "*")  # MarkDown 때문에 이상하게 됨.

    except:

        if (school_menu["message"]) == "급식 정보가 없습니다":
            embed.title = "오늘은 급식이 없어요!"

        else:
            embed.title = "알 수 없는 오류가 발생했어요!"

    return embed
