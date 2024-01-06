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
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="A fact about foxes!", description=fact, color=color)
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
        url = "https://v2.yiff.rest/animals/blep?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## ramomize embed color
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="A blep picture!", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def cheeta(self, ctx):
        """A cheeta picture"""
        # actual command
     
        url = "https://v2.yiff.rest/animals/cheeta?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here(Clackk on e621.net)"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## ramomize embed color
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="A cheeta picture!", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

        
    @commands.command()
    async def dik(self, ctx):
        """A picture of a Dik Dik"""
        # actual command
      
        url = "https://v2.yiff.rest/animals/dikdik?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## ramomize embed color
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="A Dik Dik picture!", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        

    @commands.command()
    async def lynx(self, ctx):
        """A cute lynx picture"""
        # actual command
       
        url = "https://v2.yiff.rest/animals/lynx?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## ramomize embed color
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="A cute lynx picture!", color=color)
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
        #headers["Authorization"] = """
        #headers["User-Agent"] = "place headers here"

        #resp = requests.get(url, headers=headers,).json()
        #yiff = json.dumps(resp)
        #url = json.loads(yiff)
        #blep = url.get("images")
        #uwu = blep[0].get("url")
        #await ctx.send(uwu)
    
    @commands.command()
    async def status(self, ctx):
        """Check the status your API key"""
        # actual command
        url = "https://yiff.rest/status"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("status")
        uwu = blep.get("furry")
        await ctx.send(uwu)
        
    @furry.command()
    async def boop(self, ctx):
        """A picture of a boop"""
        # actual command
        url = "https://v2.yiff.rest/furry/boop?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Boop*", description="hehehe", color=color)
        embed.set_image(url=uwu)
        await ctx.send(embed=embed)
        
    @furry.command()
    async def cuddle(self, ctx):
        """mm cuddly"""
        # actual command
     
        url = "https://v2.yiff.rest/furry/cuddle?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Cuddle*", description="hehehe", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
        
    @furry.command()
    async def floppy(self, ctx):
        """floopy"""
        # actual command
     
        url = "https://v2.yiff.rest/furry/flop?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Flop*", description="hehehe", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

        
    @furry.command()
    async def fursuit(self, ctx):
        """A cool fursuit picture"""
        # actual command
    
        url = "https://v2.yiff.rest/furry/fursuit?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Fursuit*", description="bro I want one", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

                
    @furry.command()
    async def furbutt(self, ctx):
        """hehehe ;3"""
        # actual command
        # Check if user is in DM
        if ctx.guild is None:
            await ctx.send("You can't use NSFW commands in DMs! Sorry, its just the rules.")
            return
        # Check if user is in NSFW channel
        if ctx.channel.is_nsfw():
            url = "https://v2.yiff.rest/furry/butts?notes=disabled"

            headers = CaseInsensitiveDict()
            headers["User-Agent"] = "place user agent here"

            resp = requests.get(url, headers=headers,).json()
            yiff = json.dumps(resp)
            url = json.loads(yiff)
            blep = url.get("images")
            uwu = blep[0].get("yiffMediaURL")
            ## create embed for picture
            color = random.randint(0, 0xffffff)
            embed = discord.Embed(title="OwO", description="hey, you looked it up", color=color)
            embed.set_image(url=uwu)
            embed.set_footer(text="Powered by yiff.rest")
            await ctx.send(embed=embed)
        else:  
            await ctx.send("This command is only available in NSFW channels")



        
    @furry.command()
    async def hold(self, ctx):
        """floof hold"""
        # actual command
    
        url = "https://v2.yiff.rest/furry/hold?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Hold*", description="mm warm floofs", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @furry.command()
    async def howl(self, ctx):
        """A howling picture"""
        # actual command
     
        url = "https://v2.yiff.rest/furry/howl?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Howl*", description="*ahem* *howl*", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

        
    @furry.command()
    async def hug(self, ctx):
        """were having soft tacos later"""
        # actual command
     
        url = "https://v2.yiff.rest/furry/hug?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Hug*", description="thas cute", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @furry.command()
    async def kiss(self, ctx):
        """floof kiss"""
        # actual command
        
        url = "https://v2.yiff.rest/furry/kiss?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Kiss*", description=":eyes:", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

        
    @furry.command()
    async def lick(self, ctx):
        """a lick"""
        # actual command
        
        url = "https://v2.yiff.rest/furry/lick?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Lick*", description="**mlem**", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)

    @furry.command()
    async def propose(self, ctx):
        """floof proposal"""
        # actual command
        
        url = "https://v2.yiff.rest/furry/propose?notes=disabled"

        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "place user agent here"

        resp = requests.get(url, headers=headers,).json()
        yiff = json.dumps(resp)
        url = json.loads(yiff)
        blep = url.get("images")
        uwu = blep[0].get("yiffMediaURL")
        ## create embed for picture
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="*Propose*", description="wedding menace mac", color=color)
        embed.set_image(url=uwu)
        embed.set_footer(text="Powered by yiff.rest")
        await ctx.send(embed=embed)
        
    @commands.group()
    async def yiff(self, ctx):
        """Yiff and related subcommands"""
 
  

    @yiff.command()
    async def ybulge(self, ctx):
        """bulge noticed"""
        ## throw error if not in a server
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            # check if user is in nsfw channel, stops command from running if not
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")
            
            else:
                url = "https://v2.yiff.rest/furry/bulge?notes=disabled"

                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here"

                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("images")
                uwu = blep[0].get("yiffMediaURL")
                ## create embed for picture
                color = random.randint(0, 0xffffff)
                embed = discord.Embed(title="*Bulge*", description="*owo*", color=color)
                embed.set_image(url=uwu)
                embed.set_footer(text="Powered by yiff.rest")
                await ctx.send(embed=embed)

            
    @yiff.command()
    async def yandro(self, ctx):
        """Andromorphic Yiff"""
        # actual command
        ## throw error if not in a server
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            # check if user is in nsfw channel, stops command from running if not
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                
                url = "https://v2.yiff.rest/furry/yiff/andromorph?notes=disabled"

                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here"

                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("images")
                uwu = blep[0].get("yiffMediaURL")
                ## create embed for picture
                color = random.randint(0, 0xffffff)
                embed = discord.Embed(title="OWO", description="*Blep*", color=color)
                embed.set_image(url=uwu)
                embed.set_footer(text="Powered by yiff.rest")
                await ctx.send(embed=embed)
        
    @yiff.command()
    async def ygay(self, ctx):
        """Gay Yiff"""
        ## throw error if command is not run in a server
        if ctx.guild is None:
            await ctx.send("This command is not available in DM's")
        else:
            # actual command
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                
                url = "https://v2.yiff.rest/furry/yiff/gay?notes=disabled"

                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here"

                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("images")
                uwu = blep[0].get("yiffMediaURL")
                ## create embed for picture
                color = random.randint(0, 0xffffff)
                embed = discord.Embed(title="*mlem*", description="*real degen hours*", color=color)
                embed.set_image(url=uwu)
                embed.set_footer(text="Powered by yiff.rest")
                await ctx.send(embed=embed)
        
    @yiff.command()
    async def ygyno(self, ctx):
        """Gynomorphic Yiff"""
        # actual command
        ## throw error if not in a server
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://v2.yiff.rest/furry/yiff/gynomorph?notes=disabled"

                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here"

                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("images")
                uwu = blep[0].get("yiffMediaURL")
                ## create embed for picture
                color = random.randint(0, 0xffffff)
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=color)
                embed.set_image(url=uwu)
                embed.set_footer(text="Powered by yiff.rest")
                await ctx.send(embed=embed)

            
    @yiff.command()
    async def ylesbian(self, ctx):
        """Lesbian Yiff"""
        # actual command
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                
                url = "https://v2.yiff.rest/furry/yiff/lesbian?notes=disabled"

                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here"

                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("images")
                uwu = blep[0].get("yiffMediaURL")
                ## create embed for picture
                color = random.randint(0, 0xffffff)
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=color)
                embed.set_image(url=uwu)
                embed.set_footer(text="Powered by yiff.rest")
                await ctx.send(embed=embed)

        
    @yiff.command()
    async def ystraight(self, ctx):
        """Straight Yiff"""
        # actual command
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                
                url = "https://v2.yiff.rest/furry/yiff/straight?notes=disabled"

                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here"

                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("images")
                uwu = blep[0].get("yiffMediaURL")
                ## create embed for picture
                color = random.randint(0, 0xffffff)
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=color)
                embed.set_image(url=uwu)
                embed.set_footer(text="Powered by yiff.rest")
                await ctx.send(embed=embed)
        
    @yiff.command()
    async def yfuta(self, ctx):
        """futa yiff"""
        # actual command
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:

            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")
        
            else:
                
                url = "https://v2.yiff.rest/furry/yiff/dickgirl?notes=disabled"

                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here"

                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("images")
                uwu = blep[0].get("yiffMediaURL")
                ## create embed for picture
                color = random.randint(0, 0xffffff)
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=color)
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
        # actual command
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:

            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+male/female&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()
    async def gay(self, ctx):
        """gay yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+male/male&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()
    async def lesbian(self, ctx):
        """lesbian yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+female/female&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()
    async def mawshot(self, ctx):
        """mawshot yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+mawshot&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)


    @e6.command()
    async def paw(self, ctx):
        """pawb yiff from e621.net, aka pawshot"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+foot_play&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def good(self, ctx):
        """high favorited yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>500&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def canine(self, ctx):
        """Canine-centric or including yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+canine&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def vulpine(self, ctx):
        """Fox-centric or including yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+vulpine&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def feline(self, ctx):
        """Feline-centric or including yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+felid&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def collar(self, ctx):
        """yiff including collars from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+collar&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def goodboy(self, ctx):
        """what it says on the tin, man"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+pet_praise&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def femboy(self, ctx):
        """femboy yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+girly+male&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def latex(self, ctx):
        """getting adventurous, are we?"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+latex_transformation&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def anal(self, ctx):
        """anal yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+anal&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    
    @e6.command()   
    async def licc(self, ctx):
        """cunnilingus yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>75+cunnilingus&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)
        
        
    @e6.command()   
    async def ass(self, ctx):
        """eat ass yiff from e621.net"""
        if ctx.guild is None:
            await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+rimming&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

    @e6.command()   
    async def oral(self, ctx):
        """oral yiff from e621.net"""
        if ctx.guild is None:
                    await ctx.send("This command can only be used in a server.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+oral&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                full = blep[select].get("file")
                fulluwu = full.get("url")
                uwu = blep[select].get("sample")
                img = uwu.get("url")
                ## create embed for picture
                embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                embed.set_image(url=img)
                embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                await ctx.send(embed=embed)

 

    @e6.command()   
    async def top(self, ctx):
        """top rated yiff from e621.net"""
        ## throw error if command is run outside of a guild
        if ctx.guild is None:
            await ctx.send("This command is only available in servers.")
        else:
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")
            else:
                url = "https://e621.net/posts.json?tags=favcount%3A>50+order:top&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                ## throw error if posts is empty
                if blep == []:
                    await ctx.send("No posts found, please try again or check your tags.")
                else:
                    full = blep[select].get("file")
                    fulluwu = full.get("url")
                    uwu = blep[select].get("sample")
                    img = uwu.get("url")
                    ## create embed for picture
                    embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                    embed.set_image(url=img)
                    embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                    await ctx.send(embed=embed)

    
    @e6.command()   
    async def search(self, ctx, search: str):
        """searh your own tags from e621.net, Please use valid tags from e621.net, seperate tags by -, tags with two words should be spaced with an underscore (e.g. 'furry_cat'). please do not place spaces before or after tags. a proper query should look like this: `+e6 search garfield-furry_cat-rating:s`"""
        ## throw error if command is run outside of a guild
        if ctx.guild is None:
            await ctx.send("This command is not available in DM's.")
        else:
        ## check if channel has nsfw atribute
            if ctx.channel.is_nsfw() == False:
                await ctx.send("This command is only available in NSFW channels.")

            else:
                search = search.replace("-", "+") 
                url = "https://e621.net/posts.json?tags=favcount%3A>=10+order:random+" + search + "&limit=50"
                select = random.randint(0, 49)
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "place user agent here(racketclack on e621)"
                resp = requests.get(url, headers=headers,).json()
                yiff = json.dumps(resp)
                url = json.loads(yiff)
                blep = url.get("posts")
                ## throw error if posts is empty
                if blep == []:
                    await ctx.send("No results found, please try again or check your tags.")
                else:
                    uwu = blep[select].get("sample")
                    full = blep[select].get("file")
                    img = uwu.get("url")
                    fulluwu = full.get("url")
                    tag = blep[select].get("tags")
                    tagdone = tag.get("artist")
                    ## create embed for picture
                    embed = discord.Embed(title="*OWO*", description="*real degen hours*", color=0x1d2985)
                    embed.set_image(url=img)
                    ## provide footer containing post id and link to full image under fulluwu
                    embed.set_footer(text="https://e621.net/post/show/" + str(blep[select].get("id")) + " | " + "Full Image: " + fulluwu)
                    await ctx.send(embed=embed)





    
