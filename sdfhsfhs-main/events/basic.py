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

    text_message = TextSendMessage(text='''$ Master SPA $
專業海綿低能出身，融合東西方智障手法

-嚴格把關：所有用品皆有智障或派大星用過。

-設備齊全：夏天有蟹寶王，冬天有海之霸和樹屋。

-獨立空間：專業乾淨高品質獨立蟹保空間。''', emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id='8522',
        sticker_id='16581271'
    )

    about_us_img = 'https://i.imgur.com/33pk0Iw.jpeg'

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