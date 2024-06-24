import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os
import json

# Load bot token from config.json file
with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['bot_token']
TARGET_CHANNEL_ID = config['target_channel_id']
CHANNEL_CHOICES = config['channel_choices']

# Initialize bot with intents
intents = nextcord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='!', intents=intents)
