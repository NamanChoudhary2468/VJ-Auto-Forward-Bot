from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "145bcbc424d1c1ffe04f3e607ea55c9a")
      API_ID = int(getenv("API_ID", "25163484"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7034951863:AAEM1IPG7KxGd0atadlY1zZ6MWot-2tJGok")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002088192873:-1002087386412").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
