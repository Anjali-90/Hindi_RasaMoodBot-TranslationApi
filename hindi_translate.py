import requests

sender = input("Please tell me your name : \n")

bot_message =" "

while bot_message !="Bye":
    
    message = input("Type your message : \n")
    
    print("Sending now")
    
    r=requests.post('http://localhost:5005/webhooks/rest/webhook' , json={"sender": sender, "message":message})
    
    print("Bot says,", end='')

    data = r.json()

    params = ""

    for i in data:
        dictionary = i
        
        if 'text' in dictionary.keys():
            params = i['text']

            url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

            API_KEY = 'trnsl.1.1.20210715T151841Z.4cd2f70ac75bd979.f84120818b8bbc44b792d510e0594a57afffd67f'

            params = dict(key=API_KEY, text=params,lang='hi')
            res = requests.get(url, params=params)
            print(res.json()['text'][0])

        else:
            print(i['image'])