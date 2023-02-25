from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

ACCESS_TOKEN = "W8MM2N0fL5rSAB268oYYAXt2BBme+/Y9wa499rvFJAROLnguOwTs9dTLUjzsQOSqsc/ATyIjBoZGIelYDeT6Sv20PwM0LH6gJUTJXed8UiObpyOMDleAz/A61/3p4dYhrNmd5OmTy3vDucli2ll6iwdB04t89/1O/w1cDnyilFU="
SECRET = "e655fb3f5226000a616e5ea54f14c35b"

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)