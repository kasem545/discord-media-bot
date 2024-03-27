import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import asyncio
import os 

# Bot token
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Initialize bot with intents
intents = nextcord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.slash_command(name="send_media", description="Send media to the specified channel.")
    
    # set choices for channel_name of your server channel for media only, disable send messages permissions of those channels
async def send_media(ctx, media_type: str = nextcord.SlashOption(choices={"image", "video"}), channel_name: str = nextcord.SlashOption(choices={"random-1", "random-2", "random-3"}), attachment: nextcord.Attachment = None):
    # Acknowledge the interaction
    await ctx.send("Processing your request...")

    # Process the command asynchronously
    await asyncio.create_task(process_send_media(ctx, media_type, channel_name, attachment))

# Asynchronous function to process the send_media command
async def process_send_media(ctx, media_type, channel_name, attachment):
    # Check if a media file is attached
    if attachment is None:
        await ctx.send("Please attach a media file.")
        return

    # Check if the attachment is of the specified media type
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

    # Get the media URL
    media_url = attachment.url

    # Get the channel
    if channel_name:
        channel = nextcord.utils.get(ctx.guild.channels, name=channel_name)

        # If the channel is not found, inform the user
        if channel is None:
            await ctx.send(f"Could not find the specified channel '{channel_name}'. Please ensure the channel exists.")
            return
    else:
        pass
        
    # Send the media to the specified channel
    await channel.send(media_url)
    # Wait for 5 seconds
    await asyncio.sleep(5)
    # Send confirmation message
    await ctx.send("Media sent successfully :)")

@bot.slash_command(name="usage", description="Show usage .")
async def options(ctx):
    # Provide some options to the user
    options_text = "Usage:\n1. /send_media [media_type] [channel_name] - Send media to the specified channel [attachment] - the media you want to upload\n2. /Usage - Show Usage."
    await ctx.send(options_text)

@bot.event
async def on_message(message):
    # Check if the message is from a bot or if it starts with '/'
    if message.author.bot or message.content.startswith('/send_media') or message.content.startswith('/usage') :
        await bot.process_commands(message)  # Process commands normally
    else:
        # Delete the message if it doesn't start with '/'
        await message.delete()

# Handling errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, nextcord.ext.commands.errors.CommandNotFound):
        await ctx.send("Invalid command. Type /options for available commands.")
    else:
        print(error)  # Print the error to console for debugging purposes

bot.run(TOKEN)
