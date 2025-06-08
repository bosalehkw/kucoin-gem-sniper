import requests
from telegram import Bot

TOKEN = '7877459972:AAHKKtCobSHCmntDyQOhB4PZKY5B_UPlEPg'  # توكن البوت
CHAT_ID = '5812540828'  # آي دي تيليجرامك

bot = Bot(token=TOKEN)

def send_alert(msg):
    bot.send_message(chat_id=CHAT_ID, text=msg)

def check_hlg_volume():
    url = "https://api.kucoin.com/api/v1/market/stats?symbol=HLG-USDT"
    response = requests.get(url).json()
    vol = float(response["data"]["volValue"])
    if vol > 100000:
        send_alert(f"🚨 ضخ سيولة على HLG! الحجم الآن: {vol:.0f}$")

check_hlg_volume()
