import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22190695"))
    API_HASH = os.environ.get("API_HASH", "92f12a17818d71c8784e98a64a164e9e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7311288614:AAHecPFp5NnBrs4dJiR_l9lh1GB3zBAP_Yo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzgBu8AuRw-vr8egwwFyNRuIlSQ-vzCqbFmiKf6043ED3msnSWgCQbU97xQiQUyjRSFV3hEcIWchtGg4Gw6t37Or3af4EdzUy_ShQb5SDrHK6CHcyjwfdJcqaCfDiEzUgOTxrSu04dhPIkFaquyy30sYnGnumiv_9AqxBlQxj2dZHFJTOyQrhxBUUTIe74DmGaOGSo75JZIdeJgMKDJgz_qfGVsqYvwsY1wE-IGfe_f_MSR9hvPIcwvdkk4PUNOMCNPe93_uvoz1uasyDF6STvzE6EBWanW-691RLlpFoxdX4CdIyQwKinM7pYLOvuNgi5GGKg705PkhjBUZspGO5n_RVrg=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Xmusiclabbot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/+EI-RtYpUzLAyMjM1") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/+EI-RtYpUzLAyMjM1") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6972264549")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
