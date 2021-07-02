import requests
from apscheduler.schedulers.blocking import BlockingScheduler

from stockAPIProcess import *

botToken = "1896593387:AAFe8u8IvN6SCKohb_K1_uK3mHW3WV8G5yg"
#chatId = "-1001581392547"
chatId = "1750572919"

def telegramBotSendText(bot_Message) :
    sendText = "https://api.telegram.org/bot" + botToken + "/sendMessage?chat_id=" + chatId + "&parse_mode=HTML&text=" + bot_Message
    response = requests.get(sendText)
    return response.json

def runScheduler() :
    telegramBotSendText(niftyOverview())
    telegramBotSendText(niftyIndexDetails())
    telegramBotSendText(topGainers())
    telegramBotSendText(topLosers())

runScheduler()