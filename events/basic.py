from line_bot_api import *


def about_us_event(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        },
        {
            "index": 13,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        }
    ]

    text_message = TextSendMessage(text='''$ 哈哈傻瓜蛋 $
海綿寶寶
                                   
派大星

章魚哥

蟹老闆。''', emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id='8521',
        sticker_id='16581272'
    )

    about_us_img = 'https://i.imgur.com/70A4WdI.jpg'

    image_message = ImageSendMessage(
        original_content_url=about_us_img,
        preview_image_url=about_us_img
    )

    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message, image_message])
    
def location_event(event):
    location_message = LocationSendMessage(
        title='哈哈傻瓜蛋',
        address='台北地下街1號',
        latitude=25.034563695,
        longitude=121.5738839
    )

    line_bot_api.reply_message(
        event.reply_token,
        location_message)