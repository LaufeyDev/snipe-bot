import hikari
import lightbulb


bot = lightbulb.BotApp(
    token='include ur token here', 
    prefix="!" 
)


@bot.command
@lightbulb.command('ping', 'says pong')
@lightbulb.implements(lightbulb.PrefixCommand)

async def ping(ctx):
    await ctx.respond('https://tenor.com/view/kokushibou-gif-22120843')
    await ctx.respond('pong!')



bot.run()
