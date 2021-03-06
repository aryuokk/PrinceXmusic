import os
from PrinceXmusic.config import SOURCE_CODE
from PrinceXmusic.config import ASSISTANT_NAME
from PrinceXmusic.config import PROJECT_NAME
from PrinceXmusic.config import SUPPORT_GROUP
from PrinceXmusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello ๐ [{}](tg://user?id={})!**\n\n๐ค I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\nโ Send me /help for more info."
      HELP_MSG = [
        ".",
f"""
**Hey ๐ Welcome back to {PROJECT_NAME}

๏ธโ๏ธ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

๏ธ๏ธโ๏ธAssistant name ยปยป @{ASSISTANT_NAME}\n\nClick next for instructions๐**
""",

f"""
**โ๏ธSetting upโ๏ธ**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group
""",
f"""
**Commands**

**=ยปยป Song Playing ๐ง**

๐ /play: Play the requestd song
๐ /play [yt url] : Play the given yt url
๐ /play [reply yo audio]: Play replied audio
๐ /splay: Play song via jio saavn
๐ /ytplay: Directly play song via Youtube Music

**=ยปยป Playback โฏ**

๐ /player: Open Settings menu of player
๐ /skip: Skips the current track
๐ /pause: Pause track
๐ /resume: Resumes the paused track
๐ /end: Stops media playback
๐ /current: Shows the current Playing track
๐ /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",

f"""
**=ยปยป Channel Music Play ๐ **

โ๏ธ For linked group admins only! โ๏ธ

๐ /cplay [song name] - play song you requested
๐ /csplay [song name] - play song you requested via jio saavn
๐ /cplaylist - Show now playing list
๐ /cccurrent - Show now playing
๐ /cplayer - open music player settings panel
๐ /cpause - pause song play
๐ /cresume - resume song play
๐ /cskip - play next song
๐ /cend - stop music play
๐ /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

โช๏ธ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",

f"""
**=>> More tools ๐งโ๐ง**

๐ /musicplayer [on/off]: Enable/Disable Music player
๐ /admincache: Updates admin info of your group. Try if bot isn't recognize admin
๐ /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
f"""
**=>> Song Download ๐ธ**

๐ /video [song mame]: Download video song from youtube
๐ /song [song name]: Download audio song from youtube
๐ /saavn [song name]: Download song from saavn
๐ /deezer [song name]: Download song from deezer

**=>> Search Tools ๐**

๐ /search [song name]: Search youtube for songs
๐ /lyrics [song name]: Get song lyrics
""",

f"""
**=>> Commands for Sudo Users โ๏ธ**

 ๐ /userbotleaveall - remove assistant from all chats
 ๐ /broadcast <reply to message> - globally brodcast replied message to all chats
 ๐ /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
