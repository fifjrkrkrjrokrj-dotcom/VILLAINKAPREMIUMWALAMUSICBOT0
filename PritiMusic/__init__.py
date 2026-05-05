from PritiMusic.core.bot import Lucky
from PritiMusic.core.dir import dirr
from PritiMusic.core.git import git
from PritiMusic.core.userbot import Userbot
from PritiMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Lucky()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
