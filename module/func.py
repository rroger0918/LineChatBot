from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
from linebot.models import TextSendMessage, BubbleContainer, ImageComponent, BoxComponent, TextComponent, IconComponent, ButtonComponent, SeparatorComponent, FlexSendMessage, URIAction
from linebot.models import TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

#你好
def hi(event):
    
    try:
        message = [  # 串列
            
            TextSendMessage(  # 傳送y文字
                text="Hi，你好啊"
            ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))
# 誰是昂哥
def sendFlex(event):
    
    try:
        message = [  # 串列
            ImageSendMessage(  # 傳送圖片
                original_content_url="https://upload.cc/i1/2021/06/29/eF4fvj.jpg",
                preview_image_url="https://upload.cc/i1/2021/06/29/eF4fvj.jpg"
            ),
            TextSendMessage(  # 傳送y文字
                text="\U0001F409東海龍王昂哥，是現任高雄苗栗屏東花蓮及新北三重蘆洲地方大老、企業公安管理顧問師、海軍陸戰隊培訓師、職業演說家、並經營一間AI砂石場，每年吸引超過20億的資金投資。\n\n☠真槍實彈實戰經驗23年，商業經營15年。從陌生派系開發一路經營到社會上流，專精於地方營運、公安設計、組織經營與管理。\n\n☢服務過的客戶包含伊拉克、美國蛙人部隊、俄羅斯北極熊生擒小隊、亞馬遜食人魚活烤三吃小隊、越南科摩多龍生擒小隊、中國新冠肺炎生擒小隊、…等百大特殊單位。\n\n\U0001F479昂哥公司協助各級組織創建永續發展的地方經營策略，致力於訓練、建立、指導高績效團隊。他以其專業領域「戰鬥哲學」為基礎，設計出獨特的指導手法，以最簡單直白的方式，協助各行各業中埋伏的內賊及地方樁腳大幅提升資產，廣受好評。"
            ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))
#學長姐分享
def share(event):
    try:
        message = TemplateSendMessage(
            alt_text='正偉帥帥',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://upload.cc/i1/2022/03/11/z0n2UD.jpg',
                        action=MessageTemplateAction(
                            label='AI研討會資訊&報名',
                            uri='https://thuform20211220233251.azurewebsites.net/'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://upload.cc/i1/2022/03/11/0hTPS2.jpg',
                        action= URITemplateAction(
                            label='系友知識分享交流',
                            uri='https://sharethu.azurewebsites.net/'
                            ),
                    ),
                    ImageCarouselColumn(
                        image_url='https://upload.cc/i1/2022/03/11/eQrIvZ.jpg',                    
                        action= URITemplateAction(
                            label='保險知識Q&A機器人',
                            uri='https://insthu.azurewebsites.net/'
                            ),
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#正偉圖文
def thuai(event):  #圖片轉盤
    try:
        message = TemplateSendMessage(
            alt_text='正偉帥帥',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://upload.cc/i1/2021/05/13/viL3nz.jpg',
                        action=MessageTemplateAction(
                            label='班導的話',
                            text='班導的話'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://upload.cc/i1/2021/05/13/gK5sLk.jpg',
                        action= URITemplateAction(
                            label='訂閱姜老師🄰🄸頻道',
                            uri='https://liff.line.me/1656959733-5gyYdjQx'
                            ),
                    ),
                    ImageCarouselColumn(
                        image_url='https://upload.cc/i1/2021/05/13/pg4liH.jpg',                    
                        action= URITemplateAction(
                            label='看看心淳老師教學多棒♥',
                            uri='https://liff.line.me/1656959733-PWgpqDv3'
                            ),
                    ),
                    ImageCarouselColumn(
                        image_url='https://upload.cc/i1/2021/05/13/NHpqTj.jpg',
                        action=MessageTemplateAction(
                            label='想加入張育仁之家',
                            text='想加入張育仁之家'
                        )
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#班導的話
def teachertalk(event):  # 多項傳送
    try:
        message = [  # 串列
            TextSendMessage(  # 傳送y文字
                text="'  '  '  '  '  '  '  '\n希望我們的同學畢業後，能夠發揮所長，齁\U0001f618\n\n發揮所長並不表示你只能做資管相關的工作，齁，發揮所長，代表的是全人的發揮，齁\U0001f44a\n\n比如說同學可能外燴經營很有興趣\U0001f373、有的同學想要當健身教練\U0001f4aa、或是買賣保險\U0001f4b9，這都是會很有成就的，齁，只要你發揮所長，齁 !\n\n那我們在東海求學呢，學問其實只是一個基礎，就是你多讀一些書\U0001f4D6，對你將來會產生比較好的想法並進行規劃，齁。\n\n這是我身為你們導師所希望看到的齁，而不是說今天讀資管就一定要做資管相關工作，一定要做programmer\U0001f4BB，不是這樣的，齁\U0001f616\n\n我希望大家都能發揮所長，那我會非常的proud of everybody。那記得如果你發揮所長了，記得多參加同學會與昔日的好友們多多交流，或是回來學校看看老師，齁\U0001f64F\n\n不要覺得甚麼，唉呦我發揮所長後跟資管無關跟同學沒話題或是愧對老師，不要醬啦，齁\U0001f612\n\n其實只要你發揮所長，我們都是資管的學生，我們都會非常以你為榮，齁 ✌✌✌\n\n'  '  '  '  '  '  '  '"
            ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))

#張育仁之家
def yuhome(event):
    
    try:
        message = [  # 串列
            
            TextSendMessage(  # 傳送y文字
                text="自己去問系辦啦廢物"
            ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))

#昂哥尊容
def sendImage(event):  # 傳送圖片
    try:
        message = ImageSendMessage(
            original_content_url="https://upload.cc/i1/2021/06/27/Xo3sVY.jpg",
            preview_image_url="https://upload.cc/i1/2021/06/27/Xo3sVY.jpg"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


#昂哥貼圖
def sendMulti(event):  # 多項傳送
    try:
        message = [  # 串列
            # StickerSendMessage(  #傳送貼圖
            #     package_id='1',
            #     sticker_id='5'
            # ),
            ImageSendMessage(  # 傳送圖片
                original_content_url="https://upload.cc/i1/2021/04/30/TWEnvk.png",
                preview_image_url="https://upload.cc/i1/2021/04/30/TWEnvk.png"
            ),
            TextSendMessage(  # 傳送y文字
                text="https://line.me/S/sticker/14627819"
            )

        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))

# 茗翔肉乾
def meatgood(event):
    try:
        bubble = BubbleContainer(
            direction='ltr',  # 項目由左向右排列
            header=BoxComponent(  # 標題
                layout='vertical',
                contents=[
                    TextComponent(text='滋美珍 Since1975',
                                  weight='bold', size='xxl'),
                ]
            ),
            hero=ImageComponent(  # 主圖片
                url='https://www.foodstar.com.tw/product_image/_thumbs/images/IMG_6966.JPG',
                size='full',
                aspect_ratio='792:555',  # 長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(  # 主要內容
                layout='vertical',
                contents=[
                    TextComponent(text='評價', size='md'),
                    BoxComponent(
                        layout='baseline',  # 水平排列
                        margin='md',
                        contents=[
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                        ]
                    ),
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(
                                        text='營業地址:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(
                                        text='台北市錦州街222號松江市場1F', color='#666666', size='sm', flex=5)
                                ],
                            ),
                            SeparatorComponent(color='#0000FF'),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(
                                        text='交通指引:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(
                                        text="捷運行天宮站4號出口", color='#666666', size='sm', flex=5),
                                ],
                            ),
                        ],
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=URIAction(
                                     label='Line官方帳號', uri='https://liff.line.me/1645278921-kWRPP32q?accountId=rcf5071r&openerPlatform=native&openerKey=qrcode'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=URIAction(
                                    label='官網訂購', uri="https://www.foodstar.com.tw/products.aspx?type=cate&id=2&gclid=Cj0KCQjw1a6EBhC0ARIsAOiTkrHRSNbkJg6fPIOnmmY1cPjBWQ1yjbZNAmHQn53n1dXcuxKPtK8iesMaAmg1EALw_wcB")
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(  # 底部版權宣告
                layout='vertical',
                contents=[
                    TextComponent(text='蒜味肉紙，茗爺真心推薦 !',
                                  color='#888888', size='sm', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="蒜味肉紙，茗爺真心推薦", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))

# 孟軒外匯
def tks(event):  # 多項傳送
    try:
        bubble = BubbleContainer(
            direction='ltr',  # 項目由左向右排列
            header=BoxComponent(  # 標題
                layout='vertical',
                contents=[
                    TextComponent(text='提克斯國際 TKs', weight='bold', size='xxl'),
                ]
            ),
            hero=ImageComponent(  # 主圖片
                url='https://www.wunme.com/a01/wunmea001/tks/fimages/26588/sdryvmvxky.png',
                size='full',
                aspect_ratio='1000:555',  # 長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(  # 主要內容
                layout='vertical',
                contents=[
                    TextComponent(text='評價', size='md'),
                    BoxComponent(
                        layout='baseline',  # 水平排列
                        margin='md',
                        contents=[
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                            IconComponent(
                                size='lg', url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"),
                        ]
                    ),
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(
                                        text='品牌門市:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(
                                        text='THE T café - 樹德科大門市', color='#666666', size='sm', flex=5)
                                ],
                            ),
                            SeparatorComponent(color='#0000FF'),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(
                                        text='交通指引:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(
                                        text="高雄市燕巢區橫山路59號", color='#666666', size='sm', flex=5),
                                ],
                            ),
                        ],
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=URIAction(
                                    label='Line官方客服', uri='https://line.me/ti/p/6ykS4T68B0'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=URIAction(
                                    label='蝦皮賣場', uri="https://shopee.tw/feddle")
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(  # 底部版權宣告
                layout='vertical',
                contents=[
                    TextComponent(text='免運布朗尼，黑狗軒真心推薦 !',
                                  color='#888888', size='sm', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="免運布朗尼，黑狗軒真心推薦", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))

#同學會位址
def sendPosition(event):  # 傳送位置
    try:
        message = LocationSendMessage(
            title='3/26 苗栗 愛在甜心',
            address='364 苗栗縣苗栗市苗栗縣大湖鄉富興村七鄰八寮灣33-5號',
            latitude=24.441221490905843,  # 緯度
            longitude=120.8743075203372  # 經度
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))

#快速選單
def sendQuickreply(event):  # 快速選單
    try:
        message = TextSendMessage(
            text='請點擊選項，查看更多內容 !',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="昂哥經歷與偉業?", text="誰是昂哥")
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label="昂哥尊容?", text="可以讓我看看昂哥有多屌嗎")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="同學會資訊?", text="同學會辦在哪")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="昂哥系列貼圖?", text="我想買昂哥系列貼圖")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="茗爺家傳肉乾?", text="我想買茗爺家傳肉乾")
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label="黑狗軒免運布朗尼?", text="我想買黑狗軒免運布朗尼")
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label="周邊網頁?", text="周邊網頁介紹")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))

#也許你想了解
def error(event):  # 傳送錯誤文字
    try:
        message = TextSendMessage(
            text="我不懂你的訊息QQ\n也許你是想了解~",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="昂哥經歷與偉業?", text="誰是昂哥")
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label="昂哥尊容?", text="可以讓我看看昂哥有多屌嗎")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="同學會資訊?", text="同學會辦在哪")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="昂哥系列貼圖?", text="我想買昂哥系列貼圖")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="茗爺家傳肉乾?", text="我想買茗爺家傳肉乾")
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label="黑狗軒免運布朗尼?", text="我想買黑狗軒免運布朗尼")
                    ),
                    QuickReplyButton(
                        action=MessageAction(
                            label="周邊網頁?", text="周邊網頁介紹")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))
