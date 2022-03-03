import hikari


bot = hikari.GatewayBot(token='OTQ1MjQyMzgyMjIyMzg1MTky.YhNTkQ.xBgZTYn7L1Ehs7MmuI09z6Z2_k8')

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Hey kokushibo is online.")




bot.run()