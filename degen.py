from redbot.core import commands
import discord
import requests
import json
from imageio import imread
from requests.structures import CaseInsensitiveDict




class Degen(commands.Cog):
    """If you know, you knows"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def fur(self, ctx):
        """UwU"""
        # Your code will go here
        await ctx.send("Hewwo! UwU")
     
    @commands.command()
    async def foxfact(self, ctx):
        """A fact about foxes with a cute fox image to boot!"""
        # actual command
        await ctx.send("cute as fuck")

        # Fox image
        imgurl = "https://randomfox.ca/floof/"
        imgresp = requests.get(imgurl)
        foximg = imgresp.json()["image"]
        await ctx.send(foximg)

        # Fox fact
        facturl = "https://some-random-api.ml/facts/fox"
        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        resp = requests.get(facturl, headers=headers,)

        fact = resp.json()["fact"]
        await ctx.send(fact)
    @commands.group()
    async def furry(self, ctx):
        """All commands furry and floofy"""
        if ctx.invoked_subcommand is None:
            await ctx.send('You need to specify a subcommand')

    @furry.command()
    async def blep(self, ctx):
        """A blep picture"""
        # actual command
        await ctx.send("*Blep*")
        url = "https://v2.yiff.rest/animals/blep"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @commands.command()
    async def cheeta(self, ctx):
        """A cheeta picture"""
        # actual command
        await ctx.send("*fast*")
        url = "https://v2.yiff.rest/animals/cheeta"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621.net)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @commands.command()
    async def dik(self, ctx):
        """A picture of a Dik Dik"""
        # actual command
        await ctx.send("what is a Dik Dik?")
        url = "https://v2.yiff.rest/animals/dikdik"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        

    @commands.command()
    async def lynx(self, ctx):
        """A cute lynx picture"""
        # actual command
        await ctx.send("Floppa cousin")
        url = "https://v2.yiff.rest/animals/lynx"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @commands.command()
    async def wolf(self, ctx):
        """A wolf picture"""
        # actual command
        await ctx.send("dog but raw")
        await ctx.send("Sorry, but the wolf api endpoint is currently down")
        #url = "https://v2.yiff.rest/animals/wolf"

        #headers = CaseInsensitiveDict()
        #headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        #headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        #resp = requests.get(url, headers=headers,).json()
        #yiff = json.dumps(resp)
        #url = json.loads(yiff)
        #blep = url.get("images")
        #uwu = blep[0].get("url")
        #await ctx.send(uwu)
        
    @furry.command()
    async def boop(self, ctx):
        """A picture of a boop"""
        # actual command
        await ctx.send("*Boop*")
        url = "https://v2.yiff.rest/furry/boop"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @furry.command()
    async def cuddle(self, ctx):
        """mm cuddly"""
        # actual command
        await ctx.send("cozy")
        url = "https://v2.yiff.rest/furry/cuddle"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @furry.command()
    async def floppy(self, ctx):
        """floopy"""
        # actual command
        await ctx.send("*floop*")
        url = "https://v2.yiff.rest/furry/flop"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @furry.command()
    async def fursuit(self, ctx):
        """A cool fursuit picture"""
        # actual command
        await ctx.send("neat!")
        url = "https://v2.yiff.rest/furry/fursuit"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @furry.command()
    async def hold(self, ctx):
        """floof hold"""
        # actual command
        await ctx.send("warm")
        url = "https://v2.yiff.rest/furry/hold"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @furry.command()
    async def howl(self, ctx):
        """A howling picture"""
        # actual command
        await ctx.send("*ahem* *howl*")
        url = "https://v2.yiff.rest/furry/howl"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @furry.command()
    async def hug(self, ctx):
        """were having soft tacos later"""
        # actual command
        await ctx.send("thas cute")
        url = "https://v2.yiff.rest/furry/hug"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @furry.command()
    async def kiss(self, ctx):
        """floof kiss"""
        # actual command
        await ctx.send(":eyes:")
        url = "https://v2.yiff.rest/furry/kiss"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @furry.command()
    async def lick(self, ctx):
        """a lick"""
        # actual command
        await ctx.send("**mlem**")
        url = "https://v2.yiff.rest/furry/lick"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @furry.command()
    async def propose(self, ctx):
        """floof proposal"""
        # actual command
        await ctx.send("wedding menace mac")
        url = "https://v2.yiff.rest/furry/propose"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @commands.group()
    async def yiff(self, ctx):
        """Yiff and related subcommands"""
        if ctx.invoked_subcommand is None:
            await ctx.send('You need to specify a subcommand')

    @yiff.command()
    async def bulge(self, ctx):
        """bulge noticed"""
        # actual command
        await ctx.send("*owo*")
        url = "https://v2.yiff.rest/furry/bulge"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @yiff.command()
    async def andromorph(self, ctx):
        """Andromorphic Yiff"""
        # actual command
        await ctx.send("*Blep*")
        url = "https://v2.yiff.rest/furry/yiff/andromorph"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @yiff.command()
    async def gay(self, ctx):
        """Gay Yiff"""
        # actual command
        await ctx.send("real degen hours")
        url = "https://v2.yiff.rest/furry/yiff/gay"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @yiff.command()
    async def gynomorph(self, ctx):
        """Gynomorphic Yiff"""
        # actual command
        url = "https://v2.yiff.rest/furry/yiff/gynomorph"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @yiff.command()
    async def lesbian(self, ctx):
        """Lesbian Yiff"""
        # actual command
        await ctx.send("*Blep*")
        url = "https://v2.yiff.rest/furry/yiff/lesbian"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @yiff.command()
    async def straight(self, ctx):
        """Straight Yiff"""
        # actual command
        await ctx.send("*Blep*")
        url = "https://v2.yiff.rest/furry/yiff/straight"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @yiff.command()
    async def futa(self, ctx):
        """futa yiff"""
        # actual command
        await ctx.send("*Blep*")
        url = "https://v2.yiff.rest/furry/yiff/dickgirl"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        await ctx.send(uwu)
        
    @commands.group()
    async def e6(self, ctx):
        """e621.net commands for all the secret degenerates out there"""
        if ctx.invoked_subcommand is None:
            await ctx.send('You need to specify a subcommand')
        # actual command
    @e6.command()

    async def straight(self, ctx):
        """straight yiff from e621.net"""
        url = "https://e621.net/posts.json?tags=favcount%3A>100+male/female&limit=1"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("posts")
        uwu = blep[0].get("sample")
        img = uwu.get("url")
        await ctx.send(img)

    @e6.command()
    async def gay(self, ctx):
        """gay yiff from e621.net"""
        url = "https://e621.net/posts.json?tags=favcount%3A>100+male/male&limit=1"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("posts")
        uwu = blep[0].get("sample")
        img = uwu.get("url")
        await ctx.send(img)

    @e6.command()
    async def lesbian(self, ctx):
        """lesbian yiff from e621.net"""
        url = "https://e621.net/posts.json?tags=favcount%3A>100+female/female&limit=1"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("posts")
        uwu = blep[0].get("sample")
        img = uwu.get("url")
        await ctx.send(img)

    @e6.command()
    async def mawshot(self, ctx):
        """mawshot yiff from e621.net"""
        url = "https://e621.net/posts.json?tags=favcount%3A>100+mawshot&limit=1"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("posts")
        uwu = blep[0].get("sample")
        img = uwu.get("url")
        await ctx.send(img)

    @e6.command()
    async def paw(self, ctx):
        """gay yiff from e621.net"""
        url = "https://e621.net/posts.json?tags=favcount%3A>100+foot_play&limit=1"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("posts")
        uwu = blep[0].get("sample")
        img = uwu.get("url")
        await ctx.send(img)

    @e6.command()   
    async def good(self, ctx):
        """high favorited yiff from e621.net"""
        url = "https://e621.net/posts.json?tags=favcount%3A>100&limit=1"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("posts")
        uwu = blep[0].get("sample")
        img = uwu.get("url")
        await ctx.send(img)
