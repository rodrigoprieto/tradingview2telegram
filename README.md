# TradingView 2 Telegram
This is a tradingview webhook designed to be free & open source.  Written using Python & Flask and is designed to run a free heroku server. 
It will allow you to create custom alerts in tradingview and send them directly to your own private telegram channel.

## How to Webhook Server on Heroku

1.) Clone Project to Desktop

2.) [Create a Heroku Account](https://www.heroku.com/)

*Heroku was free, now costs only $7*

3.) Set up a new Telegram Bot.

<ul>
<li>Create a Telegram Account: If you don't already have a Telegram account, you'll need to create one. You can download the Telegram app on your mobile device or use the Telegram Web version.</li>

<li>Open Telegram and Search for BotFather and Start a Chat with BotFather</li>

<li> Click the "Start" button or send a message to start a chat with BotFather.</li>

<li>Create a New Bot: Send the command /newbot to BotFather.
Follow the prompts to choose a name for your bot and a username. The username must end with "bot."</li>

<li>Get Your API Token: After successfully creating the bot, BotFather will provide you with an API token. This token is required to interact with the Telegram Bot API and send/receive messages.
Save Your API Token in config.json file. </li>
</ul>

4.) Edit config.json to add your own KEY to protect your server. You can use any number here.

5.) Create a new Telegram Channel and add your bot to be a member of your channel.

6.) Grab your private channel CHAT_ID and update it in your config.json file. [Need help?](https://stackoverflow.com/questions/33858927/how-to-obtain-the-chat-id-of-a-private-telegram-channel)   
	
7.) Open a terminal in the cloned directory:

8.) Install Heroku CLI so you can work connect you your webserver.

https://cli-assets.heroku.com/heroku-x64.exe

9.) Submit the following lines into the terminal and press ENTER after each one to proccess the code: 

``git init``

``heroku login``

``heroku create --region eu tv-trader-yourservernamehere``

``git add .``

``git commit -m "Initial Commit"``

``git push heroku master``


***Anytime you need to make a change to the code or the API keys, you can push a new build to Heroku:***

``git add .``

``git commit -m "Update message"``

``git push heroku master``

## How to send alerts from TradingView to your new Webserver

) After starting you server, you should see an address that will allow you to access it like below:

[https://yourserver.herokuapp.com/webhook](https://yourserver.herokuapp.com/webhook)

#### You will want to add this when you create a new alert like show below:

![image](https://i.imgur.com/hqG4kUr.png)

### TradingView JSON alert format 

```
{
	"key": "12345",
	"symbol": "{{ticker}}",
	"price": "{{close}}",
	"message": "Alert on Ethereum!"
}
```

---
| Constant | Settings Keys                                |
|----------|----------------------------------------------|
| key      | unique key that protects your webhook server |
| symbol   | Exchange symbol                              |
| price    | last price                                   |
| message  | Write your message                           |


Congratulations, you already have it.

Happy trading!

