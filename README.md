<p align="center"><img src="https://github.com/devliftz/lift.bot/blob/main/img/lift.bot.png?raw=true" width=200px" alt="project-image"></p>

<h1 align="center" id="title">lift.bot</h1>


<p id="description">Best discord.py customized library. With easier usage less time to spend on reading docs and mobile status built in.</p>

<p align="center"><img src="https://img.shields.io/discord/1065186413865357343?color=5865F2&amp;label=Discord&amp;logo=discord&amp;logoColor=white&amp;style=for-the-badge" alt="shields">
<img src="https://img.shields.io/youtube/channel/subscribers/UCty3ao3DSrd7_qxAiRbCGEg?color=red&amp;label=Youtube&amp;logo=youtube&amp;style=for-the-badge" alt="shields">
<img src="https://img.shields.io/github/downloads/devliftz/lift.bot/total?color=000000&amp;label=downloads&amp;logo=github&amp;logoColor=white&amp;style=for-the-badge" alt="shields"></p>

<h2>Project Screenshots:</h2>
<h2 style="color: 000000;"></h2>

#### Console Formatting

<img src=".github/scr.pnh.png" alt="project-screenshot"/>

<h2>Installation Guide</h2>

- Install lift.bot library `pip install lift.bot`
- Create `main.py`

<h2>Examples</h2>

```py
import liftcord
from liftcord.ext import commands

bot = liftcord.Bot(command_prefix="?")

# Example command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.login("token")
```
