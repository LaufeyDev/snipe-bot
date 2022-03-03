import hikari
import lightbulb


bot = lightbulb.BotApp(
    token='OTQ1MjQyMzgyMjIyMzg1MTky.YhNTkQ.xBgZTYn7L1Ehs7MmuI09z6Z2_k8', 
    prefix="!" 
)


@bot.command
@lightbulb.command('ping', 'says pong')
@lightbulb.implements(lightbulb.PrefixCommand)

async def ping(ctx):
    await ctx.respond('https://tenor.com/view/kokushibou-gif-22120843')
    await ctx.respond('pong!')



bot.run()