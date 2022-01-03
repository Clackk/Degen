from .degen import degen


def setup(bot):
    bot.add_cog(degen(bot))