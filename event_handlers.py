from bot_config import *

@bot.event
async def on_ready():
    print("""
                      ▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌
                   ▄▄██▌█░░░░░░░░░░░░▐
                ▄▄▄▌▐██▌█░░░░░░░░░░░░▐
                ███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▌
                ▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀
                  
                  Credit to Kasem545
""")
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if (message.channel.id == TARGET_CHANNEL_ID and 
        not message.content.startswith(('/send_media', '/usage')) and
        message.author != bot.user):
        await message.delete()
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, nextcord.ext.commands.errors.CommandNotFound):
        await ctx.send("Invalid command. Type /options for available commands.", ephemeral=True)
    else:
        print(error)  # Print the error to console for debugging purposes
