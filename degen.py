from redbot.core import commands
import discord
import requests
import json

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
        imgurl = "https://some-random-api.ml/img/fox"
        # Fox image
        imgresp = requests.get(imgurl)

        foximg = imgresp.json()["link"]
        await ctx.send(foximg)
        
        facturl = "https://some-random-api.ml/facts/fox"
        # Fox fact
    
        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        resp = requests.get(facturl, headers=headers,)

        fact = resp.json()["fact"]
        await ctx.send(fact)

    @commands.command()
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
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

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
        
    @commands.command()
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
        
    @commands.command()
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
        
    @commands.command()
    async def flopp(self, ctx):
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
        
    @commands.command()
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
        
    @commands.command()
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
        
    @commands.command()
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
        
    @commands.command()
    async def hugg(self, ctx):
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
        
    @commands.command()
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
        
    @commands.command()
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
        
    @commands.command()
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
        
    @commands.command()
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
        
    @commands.command()
    async def andyiff(self, ctx):
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
        
    @commands.command()
    async def gyiff(self, ctx):
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
        
    @commands.command()
    async def gynoyiff(self, ctx):
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
        
    @commands.command()
    async def leyiff(self, ctx):
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
        
    @commands.command()
    async def styiff(self, ctx):
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
        
    @commands.command()
    async def fuyiff(self, ctx):
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
        
