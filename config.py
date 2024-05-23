from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
      API_ID = int(getenv("API_ID", "20389440"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "......U")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001722984461:-1001623633000").replace("\n", " ").split(' '))


