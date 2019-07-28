from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('BX5oIi5F0iZh0mDf4Kv3rU6WBFd373mZedmsJ9NBD6gmE+EzQhtlm/WqojvN9UEM94hu1E3lKuIAN6oyb4dLRuuui6azce444lQ5YYeZYzHePglJ/rLGrjhCYYwvrz2Bc5meUvhOwShf2wFHfCmd0gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c41e73ff3987dfff6ae5c6491f02ca4a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = 'sorry i cant understand'

    if msg == 'hi'
        r = 'hi'
    elif msg == 'Have you had you lunch?'
        r = 'not yet'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()