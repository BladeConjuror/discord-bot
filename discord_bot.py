

import discord
from discord.ext import commands
import json
from discord import Embed
    

# Initialize the bot

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to keep track of user message counts
user_message_count = {}

# Load message counts from a JSON file
try:
    with open("message_counts.json", "r") as f:
        user_message_count = json.load(f)
except FileNotFoundError:
    pass

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_id = str(message.author.id)

    if user_id not in user_message_count:
        user_message_count[user_id] = 0

    user_message_count[user_id] += 1

    try:
        embed = discord.Embed(color=0xFF0000)
        if user_message_count[user_id] == 5:
            role = discord.utils.get(message.guild.roles, name='Agent In-Training')
            await message.author.add_roles(role)
            embed.title = "Поздравляем!"
            embed.description = f"Поздравляю {message.author.mention}, Вы уже неделю с нами или активно общаетесь. Продолжайте в том же духе!"
            embed.add_field(name="Новая роль", value=f"**{role.name}**", inline=False)
        elif user_message_count[user_id] == 10:
            role = discord.utils.get(message.guild.roles, name='Bronze Operator')
            await message.author.add_roles(role)
            embed.title = "Отличная работа!"
            embed.description = f"Отличная работа, {message.author.mention}, Ваши заслуги не остались незамеченными. Вы активный участник нашего сервера!"
            embed.add_field(name="Новая роль", value=f"**{role.name}**", inline=False)
        elif user_message_count[user_id] == 20:
            role = discord.utils.get(message.guild.roles, name='Silver Sheriff')
            await message.author.add_roles(role)
            embed.title = "Вау!"
            embed.description = f"Вау, {message.author.mention}, Вы регулярно участвуете в обсуждениях и ваше мнение ценится. Спасибо за вашу активность!"
            embed.add_field(name="Новая роль", value=f"**{role.name}**", inline=False)
        elif user_message_count[user_id] == 50:
            role = discord.utils.get(message.guild.roles, name='Gold Guardian')
            await message.author.add_roles(role)
            embed.title = "Потрясающе!"
            embed.description = f"Потрясающе, {message.author.mention}, Ваши советы и активное участие делают сервер лучше. Вы стали нашим золотым стражем!"
            embed.add_field(name="Новая роль", value=f"**{role.name}**", inline=False)
        elif user_message_count[user_id] == 100:
            role = discord.utils.get(message.guild.roles, name='Platinum Phantom')
            await message.author.add_roles(role)
            embed.title = "Великолепно!"
            embed.description = f"Великолепно, {message.author.mention}, Вы не просто активный участник, вы создаете интересные обсуждения и помогаете серверу!"
            embed.add_field(name="Новая роль", value=f"**{role.name}**", inline=False)
        elif user_message_count[user_id] == 200:
            role = discord.utils.get(message.guild.roles, name='Diamond Duelist')
            await message.author.add_roles(role)
            embed.title = "Невероятно!"
            embed.description = f"Невероятно, {message.author.mention}, Ваша длительная активность и вклад в жизнь сервера не могут быть недооценены. Вы диамант среди нас!"
            embed.add_field(name="Новая роль", value=f"**{role.name}**", inline=False)
        elif user_message_count[user_id] == 400:
            role = discord.utils.get(message.guild.roles, name='Immortal Sage')
            await message.author.add_roles(role)
            embed.title = "Легендарно!"
            embed.description = f"Легендарно, {message.author.mention}, Вы легенда этого сервера. Ваша активность и вклад в сообщество бесценны."
            embed.add_field(name="Новая роль", value=f"**{role.name}**", inline=False)
        if embed.title:
            await message.channel.send(embed=embed)
    except Exception as e:
            await message.channel.send("Сожалею, у меня нет прав добавлять эту роль ;(")


    # Save message counts to a JSON file
    with open("message_counts.json", "w") as f:
        json.dump(user_message_count, f)

    await bot.process_commands(message)

@bot.command()
async def messages(ctx):
    user_id = str(ctx.author.id)
    if user_id in user_message_count:
        count = user_message_count[user_id]
        await ctx.send(f"{ctx.author.mention}, вы отправили {count} сообщений.")
    else:
        await ctx.send(f"{ctx.author.mention}, вы ещё не отправляли сообщений.")

@bot.command()
async def roles(ctx):
    embed = discord.Embed(title="Роли на сервере", description="Надеемся, что вы найдете своё место в нашем сообществе! 🌟", color=0x00ff00)

    embed.add_field(name="Начальные роли", value="Recruit (#D3D3D3) - Добро пожаловать на сервер!\nAgent In-Training (#ADFF2F) - Вы уже неделю с нами.", inline=False)
    embed.add_field(name="Промежуточные роли", value="Bronze Operator (#CD7F32) - Активное участие.\nSilver Sheriff (#C0C0C0) - Регулярное участие.\nGold Guardian (#FFD700) - Помощь новичкам.", inline=False)
    embed.add_field(name="Высшие роли", value="Platinum Phantom (#E5E4E2) - Организация событий.\nDiamond Duelist (#B9F2FF) - Долгосрочная активность.\nImmortal Sage (#8A2BE2) - Очень активные участники.", inline=False)
    embed.add_field(name="Элитные роли", value="Radiant (#FF4500) - Роль для модераторов.\nValorant (#FF0000) - Роль для администраторов.", inline=False)
    embed.add_field(name="Специальные роли", value="Sniper (#0000FF) - Для любителей снайперских винтовок.\nStrategist (#800080) - Для тех, кто хорошо разбирается в тактике.\nLore Master (#FFFF00) - Для тех, кто хорошо знает лор.\nEvent Winner (#4B0082) - Для победителей событий.", inline=False)
    
    await ctx.send(embed=embed)

# Run the bot (ur token)
bot.run("")

