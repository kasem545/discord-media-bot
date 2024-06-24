from bot_config import bot, CHANNEL_CHOICES
import nextcord
import asyncio
from nextcord.ext import commands
from nextcord import SlashOption

@bot.slash_command(name="send_media", description="Send media to the specified channel.")
async def send_media(
    ctx, 
    media_type: str = SlashOption(choices={"image", "video"}), 
    channel_name: str = SlashOption(choices=CHANNEL_CHOICES), 
    attachment: nextcord.Attachment = None,  
    comment: str = SlashOption(description="Add your comment", required=False)
):
    await ctx.send("Processing your request...")
    await asyncio.create_task(process_send_media(ctx, media_type, comment ,channel_name, attachment))

async def process_send_media(ctx, media_type, comment, channel_name, attachment):
    if attachment is None:
        await ctx.send("Please attach a media file.")
        return

    if media_type.lower() == "image":
        if not attachment.content_type.startswith('image'):
            await ctx.send("Please attach a valid image file.")
            return
    elif media_type.lower() == "video":
        if not attachment.content_type.startswith('video'):
            await ctx.send("Please attach a valid video file.")
            return
    else:
        await ctx.send("Invalid media type. Use 'image' or 'video'.")
        return

    media_url = attachment.url
    channel = nextcord.utils.get(ctx.guild.channels, name=channel_name)

    if channel is None:
        await ctx.send(f"Could not find the specified channel '{channel_name}'. Please ensure the channel exists.")
        return
        
    await channel.send(f"{ctx.user.mention} {media_url}\n comment: {comment}")
    await asyncio.sleep(5)
    await ctx.send(f"{ctx.user.mention} Media sent successfully :)")

@bot.slash_command(name="usage", description="Show usage.")
async def options(ctx):
    options_text = "Usage:\n1. /send_media [media_type] [channel_name] - Send media to the specified channel [attachment] - the media you want to upload\n2. /Usage - Show Usage."
    await ctx.send(options_text)
