import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load the secret token from the hidden .env file
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your specific Generator channel ID
GENERATOR_CHANNEL_ID = 14664612344566632829694

bot_created_channels = set()

@bot.event
async def on_ready():
    print(f'Logged in securely as {bot.user.name}!')

@bot.event
async def on_voice_state_update(member, before, after):
    # 1. User joins the Generator channel -> Create a new VC
    if after.channel and after.channel.id == GENERATOR_CHANNEL_ID:
        guild = member.guild
        category = after.channel.category
        
        # Create the new channel
        new_channel = await guild.create_voice_channel(
            name=f"☁️ {member.display_name}'s Room",
            category=category
        )
        
        # Give the creator permissions to manage their own room
        await new_channel.set_permissions(member, manage_channels=True, move_members=True)
        
        # Move the user into their new room
        await member.move_to(new_channel)
        
        # Add the new channel's ID to our tracking set
        bot_created_channels.add(new_channel.id)
        return

    # 2. Cleanup: If someone leaves a channel, check if it's empty and bot-created
    if before.channel and before.channel.id in bot_created_channels:
        if len(before.channel.members) == 0:
            await before.channel.delete()
            bot_created_channels.remove(before.channel.id)

# Run the bot using the token from the .env file
bot.run(os.getenv('DISCORD_TOKEN'))
