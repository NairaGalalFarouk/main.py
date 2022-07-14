import requests
import telebot
from telegram import *
api_id = "14681104"
api_hash = '48b5ee1310fecbac3f331ee24fb3eaef'
mainGroupID="naira_task"
token ="5589517522:AAFcBmK-XnPY6h5VfXAO4IFt1mPK8jIuuDc"
groupID ="testmsgfortask"
json = {"buy between":9000,"targets":1000, "stop loss":8800}
json_ =f'buy between : {json.get("buy between")}                                                                                                ' \
       f'targets: {json.get( "targets")}                                                                                               '\
       f'stop loss: {json.get( "stop loss")}'
msg= f'buy : {json.get("buy between")}                                                                                                ' \
     f'sell: {json.get( "targets")}                                                                                               '\
     f'stop: {json.get( "stop loss")}'

def send(message,group):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{group}&text={message}'
    response = requests.get(url)
    if response.status_code == 200:
         print('Successfully sent')
    else:
         print('ERROR: Could not send Message')


send(json_,mainGroupID)
send(msg,groupID)

