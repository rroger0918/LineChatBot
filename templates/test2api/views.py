from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text

                    if mtext == '@彈性配置':
                        func.sendFlex(event)
    

                    elif mtext == '誰是昂哥':
                        func.sendFlex(event)
                    
                    elif mtext == '你好':
                        func.hi(event)
                    
                    elif mtext == 'Hi':
                        func.hi(event)

                    elif mtext == 'hi':
                        func.hi(event)
                    
                    elif mtext == '嗨':
                        func.hi(event)
    
                    elif mtext == '可以讓我看看昂哥有多屌嗎':
                        func.sendImage(event)
    
                    # elif mtext == '@傳送貼圖':
                    #     func.sendStick(event)
    
                    elif mtext == '我想買昂哥系列貼圖':
                        func.sendMulti(event)
                    
                    elif mtext == '我想買茗爺家傳肉乾':
                        func.meatgood(event)
                    
                    elif mtext == '我想買黑狗軒免運布朗尼':
                        func.tks(event)
    
                    elif mtext == '同學會辦在哪':
                        func.sendPosition(event)
                    
                    elif mtext == '班導的話':
                        func.teachertalk(event)
                    
                    elif mtext == '想加入張育仁之家':
                        func.yuhome(event)

                    elif mtext == '學長姐分享':
                        func.share(event)
    
                    elif mtext == '我們最愛的師長':
                        func.thuai(event)

                    elif mtext == '更多服務+':
                        func.sendQuickreply(event)
                    
                    else:
                        func.error(event)

   

                    
        return HttpResponseBadRequest()
              

    else:
        return HttpResponseBadRequest()
