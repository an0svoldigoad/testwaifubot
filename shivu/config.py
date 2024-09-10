class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6765826972"
    sudo_users = "5914304439"
    GROUP_ID = -1002133191051
    TOKEN = "6384445315:AAF1exVSDGdykV_GIGhCXmgoSlf6ZWPiQ98"
    mongo_url = "mongodb+srv://gotouhitoriii:7vzXrCihdSZfTtEs@haremgod.rxndc2y.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fdazai-osamu-pfp--61572719898392305%2F&psig=AOvVaw0u6uFI8ZwkyRwOg_Kdq0by&ust=1726050701833000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJjR55iWuIgDFQAAAAAdAAAAABAx"]
    SUPPORT_CHAT = "anime_kingdom_group_chat"
    UPDATE_CHAT = "anime_kingdom_group_chat"
    BOT_USERNAME = "GrabThemBot"
    CHARA_CHANNEL_ID = "-1001782672183"
    api_id = 21531216
    api_hash = "f1ff78d3d0b3eaa825294af918318ac7"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
