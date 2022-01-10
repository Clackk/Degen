from requests.models import REDIRECT_STATI
from redbot.core import commands
import discord
import requests
import json
from requests.structures import CaseInsensitiveDict
import random




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
      
        # Fox image
        imgurl = "https://randomfox.ca/floof/"
        imgresp = requests.get(imgurl)
        foximg = imgresp.json()["image"]
   
        # Fox fact
        facturl = "https://some-random-api.ml/facts/fox"
        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        resp = requests.get(facturl, headers=headers,)
        fact = resp.json()["fact"]
        # embed
        embed = discord.Embed(title="A fact about foxes!", description=fact, color=0x00ff00)
        embed.set_image(url=foximg)
        embed.set_footer(text="Powered by some-random-api.ml and randomfox.ca")
        await ctx.send(embed=embed)

     
    @commands.group()
    async def furry(self, ctx):
        """All commands furry and floofy"""
        if ctx.invoked_subcommand is None:
            await ctx.send('You need to specify a subcommand')

    @furry.command()
    async def blep(self, ctx):
        """A blep picture"""
        # actual command
        url = "https://v2.yiff.rest/animals/blep"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        embed = discord.Embed(title="A blep picture!", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def cheeta(self, ctx):
        """A cheeta picture"""
        # actual command
     
        url = "https://v2.yiff.rest/animals/cheeta"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621.net)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        embed = discord.Embed(title="A cheeta picture!", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

        
    @commands.command()
    async def dik(self, ctx):
        """A picture of a Dik Dik"""
        # actual command
      
        url = "https://v2.yiff.rest/animals/dikdik"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        embed = discord.Embed(title="A Dik Dik picture!", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        

    @commands.command()
    async def lynx(self, ctx):
        """A cute lynx picture"""
        # actual command
       
        url = "https://v2.yiff.rest/animals/lynx"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        embed = discord.Embed(title="A cute lynx picture!", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

        
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
        url = "https://v2.yiff.rest/furry/boop"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Boop*", description="hehehe", color=0x00ff00)
        embed.set_image(url=uwu)
        await ctx.send(embed=embed)
        
    @furry.command()
    async def cuddle(self, ctx):
        """mm cuddly"""
        # actual command
     
        url = "https://v2.yiff.rest/furry/cuddle"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Cuddle*", description="hehehe", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
        
    @furry.command()
    async def floppy(self, ctx):
        """floopy"""
        # actual command
     
        url = "https://v2.yiff.rest/furry/flop"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Flop*", description="hehehe", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

        
    @furry.command()
    async def fursuit(self, ctx):
        """A cool fursuit picture"""
        # actual command
    
        url = "https://v2.yiff.rest/furry/fursuit"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Fursuit*", description="bro I want one", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @furry.command()
    async def hold(self, ctx):
        """floof hold"""
        # actual command
    
        url = "https://v2.yiff.rest/furry/hold"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Hold*", description="mm warm floofs", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @furry.command()
    async def howl(self, ctx):
        """A howling picture"""
        # actual command
     
        url = "https://v2.yiff.rest/furry/howl"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Howl*", description="*ahem* *howl*", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

        
    @furry.command()
    async def hug(self, ctx):
        """were having soft tacos later"""
        # actual command
     
        url = "https://v2.yiff.rest/furry/hug"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Hug*", description="thas cute", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @furry.command()
    async def kiss(self, ctx):
        """floof kiss"""
        # actual command
        
        url = "https://v2.yiff.rest/furry/kiss"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Kiss*", description=":eyes:", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

        
    @furry.command()
    async def lick(self, ctx):
        """a lick"""
        # actual command
        
        url = "https://v2.yiff.rest/furry/lick"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Lick*", description="**mlem**", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @furry.command()
    async def propose(self, ctx):
        """floof proposal"""
        # actual command
        
        url = "https://v2.yiff.rest/furry/propose"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
        headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("url")
        ## create embed for picture
        embed = discord.Embed(title="*Propose*", description="wedding menace mac", color=0x00ff00)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @commands.group()
    async def yiff(self, ctx):
        """Yiff and related subcommands"""
 
  

    @yiff.command()
    async def bulge(self, ctx):
        """bulge noticed"""
        # check if user is in nsfw channel, stops command from running if not
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")
        
        else:
            url = "https://v2.yiff.rest/furry/bulge"

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("images")
            uwu = blep[0].get("url")
            ## create embed for picture
            embed = discord.Embed(title="*Bulge*", description="*owo*", color=0x00ff00)
            embed.set_image(url=uwu)
            embed.set_footer(text="Powered by yiff.rest")
            await ctx.send(embed=embed)

            
    @yiff.command()
    async def andro(self, ctx):
        """Andromorphic Yiff"""
        # actual command
        # check if user is in nsfw channel, stops command from running if not
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            
            url = "https://v2.yiff.rest/furry/yiff/andromorph"

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("images")
            uwu = blep[0].get("url")
            ## create embed for picture
            embed = discord.Embed(title="OWO", description="*Blep*", color=0x00ff00)
            embed.set_image(url=uwu)
            embed.set_footer(text="Powered by yiff.rest")
            await ctx.send(embed=embed)
        
    @yiff.command()
    async def g(self, ctx):
        """Gay Yiff"""
        # actual command
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            
            url = "https://v2.yiff.rest/furry/yiff/gay"

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("images")
            uwu = blep[0].get("url")
            ## create embed for picture
            embed = discord.Embed(title="*mlem*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=uwu)
            embed.set_footer(text="Powered by yiff.rest")
            await ctx.send(embed=embed)
        
    @yiff.command()
    async def gyno(self, ctx):
        """Gynomorphic Yiff"""
        # actual command
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://v2.yiff.rest/furry/yiff/gynomorph"

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("images")
            uwu = blep[0].get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=uwu)
            embed.set_footer(text="Powered by yiff.rest")
            await ctx.send(embed=embed)

            
    @yiff.command()
    async def lesb(self, ctx):
        """Lesbian Yiff"""
        # actual command
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            
            url = "https://v2.yiff.rest/furry/yiff/lesbian"

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("images")
            uwu = blep[0].get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=uwu)
            embed.set_footer(text="Powered by yiff.rest")
            await ctx.send(embed=embed)

        
    @yiff.command()
    async def strt(self, ctx):
        """Straight Yiff"""
        # actual command
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            
            url = "https://v2.yiff.rest/furry/yiff/straight"

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("images")
            uwu = blep[0].get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=uwu)
            embed.set_footer(text="Powered by yiff.rest")
            await ctx.send(embed=embed)
        
    @yiff.command()
    async def futaaaa(self, ctx):
        """futa yiff"""
        # actual command
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")
    
        else:
            
            url = "https://v2.yiff.rest/furry/yiff/dickgirl"

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "f93e5762a2f3aa861d60f2163dc111faff2669aa"
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)"

            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("images")
            uwu = blep[0].get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=uwu)
            embed.set_footer(text="Powered by yiff.rest")
            await ctx.send(embed=embed)
        
    @commands.group()
    async def e6(self, ctx):
        """e621.net commands for all the secret degenerates out there"""
        if ctx.invoked_subcommand is None:
            await ctx.send('You need to specify a subcommand')
        # actual command
    @e6.command()

    async def straight(self, ctx):
        """straight yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+male/female&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()
    async def gay(self, ctx):
        """gay yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+male/male&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()
    async def lesbian(self, ctx):
        """lesbian yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+female/female&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()
    async def mawshot(self, ctx):
        """mawshot yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+mawshot&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)


    @e6.command()
    async def paw(self, ctx):
        """gay yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+foot_play&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()   
    async def good(self, ctx):
        """high favorited yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>500&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()   
    async def canine(self, ctx):
        """Canine-centric or including yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+canine&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()   
    async def vulpine(self, ctx):
        """Fox-centric or including yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+vulpine&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()   
    async def feline(self, ctx):
        """Feline-centric or including yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+felid&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()   
    async def collar(self, ctx):
        """yiff including collars from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+collar&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()   
    async def goodboy(self, ctx):
        """what it says on the tin, man"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+pet_praise&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
            await ctx.send(embed=embed)

    @e6.command()   
    async def femboy(self, ctx):
        """femboy yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+girly+male&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))

    @e6.command()   
    async def latex(self, ctx):
        """getting adventurous, are we?"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+latex_transformation&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))

    @e6.command()   
    async def anal(self, ctx):
        """anal yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+anal&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))

    
    @e6.command()   
    async def licc(self, ctx):
        """cunnilingus yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>75+cunnilingus&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))
        
    @e6.command()   
    async def ass(self, ctx):
        """eat ass yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+rimming&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x00ff00)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))

    @e6.command()   
    async def oral(self, ctx):
        """oral yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+oral&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))

     @e6.command()   
    async def top(self, ctx):
        """top rated yiff from e621.net"""
        if ctx.channel.is_nsfw() == False:
            await ctx.send("This command is only available in NSFW channels.")

        else:
            url = "https://e621.net/posts.json?tags=favcount%3A>50+order:top&limit=50"
            select = random.randint(0, 49)
            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "Swiss-Discord-Bot/2.1.0 (caeden0452@gmail.com)(racketclack on e621)"
            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("posts")
            uwu = blep[select].get("sample")
            img = uwu.get("url")
            ## create embed for picture
            embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
            embed.set_image(url=img)
            embed.set_footer(text="Powered by e621.net" + " | " + "https://e621.net/post/show/" + str(blep[select].get("id")))

    
    
    
