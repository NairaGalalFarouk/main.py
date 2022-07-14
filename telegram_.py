from telethon import TelegramClient, events, sync
import requests
api_id = 14681104
api_hash = '48b5ee1310fecbac3f331ee24fb3eaef'
client = TelegramClient('naira', api_id, api_hash)
token ="5589517522:AAFcBmK-XnPY6h5VfXAO4IFt1mPK8jIuuDc"
groupID ="testmsgfortask"
json = {"buy between":9000,"targets":1000, "stop loss":8800}
json_ =f'buy between : {json.get("buy between")}                                                                                                ' \
       f'targets: {json.get( "targets")}                                                                                               '\
       f'stop loss: {json.get( "stop loss")}'
msg= f'buy : {json.get("buy between")}                                                                                                ' \
     f'sell: {json.get( "targets")}                                                                                               '\
     f'stop: {json.get( "stop loss")}'
channalID="t.me/telegratask_channel"
def send(message,group):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{group}&text={message}'
    response = requests.get(url)
    if response.status_code == 200:
        print('Successfully sent')
    else:
        print('ERROR: Could not send Message')

@client.on(events.NewMessage(chats='telegram task channel'))
async def my_event_handler(event):
    message =event.raw_text
    file1 =open(r"E:\python sql\telegramget.txt","w")
    file1.write(message)
    file1 =open(r"E:\python sql\telegramget.txt","rt")
    file2 =open(r"E:\python sql\telegrampost1.txt","wt")
    for w in file1:
        file2.write(w.replace('buy', 'buy between'))
    file1.close()
    file2.close()
    file2 =open(r"E:\python sql\telegrampost1.txt","r")
    messageUpdated =file2.readline()
    send(messageUpdated,groupID)

client.start()
client.run_until_disconnected()