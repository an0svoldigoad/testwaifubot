class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6765826972"
    sudo_users = "5914304439"
    GROUP_ID = -1002133191051
    TOKEN = "6707490163:AAHZzqjm3rbEZsObRiNaT7DMtw_i5WPo_0o"
    mongo_url = "mongodb+srv://gotouhitoriii:7vzXrCihdSZfTtEs@haremgod.rxndc2y.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
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
