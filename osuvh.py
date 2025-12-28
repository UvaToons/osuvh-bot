import discord
from discord.ext import commands
import random
import os
import asyncio

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("osuvh activo bleeh")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    contenido = message.content.lower()

    if "nigga" in contenido:
        await message.channel.send("niggableeh")
        return
    
    if "polla" in contenido:
        await message.channel.send("pollableeh")
        return
    
    if "gaspar" in contenido:
        await message.channel.send("grasableeh")
        return
    
    if bot.user in message.mentions:
        cantidad = random.randint(1, 5)
        respuesta = " ".join(["bleeh"] * cantidad)
        await message.channel.send(respuesta)
        return

    if random.randint(1, 30) == 1:
        cantidad = random.randint(1, 5)
        probabilidad = random.randint(0, 18)
        probabilidad2 = random.randint(0, 3)
        palabras = ["semencito", "Tralaletastico", "tus bolas explotaran", "ano", "trisfilacutarismo", "que pasa el 20 de agosto de 1921", "soy mejor que el cubo gris bleeh bleeh", "silkson debio haber ganado el goty bleeh", "tu puta madre es una bleeh", "un dos tres catolica weon", "faggot bleeh", "*voz de maricon* bleeh", "bliih", "blue", "tuputamadrebleeh", "miau", "||https://youtu.be/SYCP71qcYZw||", "bliggahh bleeh", "blue" ] 
        if probabilidad2 == 0:
            respuesta = " ".join(["bleeh"] * cantidad + [palabras[probabilidad]])
        else:
            respuesta = " ".join(["bleeh"] * cantidad)
        await message.channel.send(respuesta)
        return
    
    if random.randint(1, 50) == 1:
        cantidad = random.randint(1, 5)
        if cantidad == 1:
            respuesta = "pinochet tenia razón"
            await message.channel.send(respuesta)
        elif cantidad == 2:
            respuesta = "bleehtastico!"
            await message.channel.send(respuesta)
        elif cantidad == 3:
            respuesta = "callate voh puto nigga"
            await message.channel.send(respuesta)
        elif cantidad == 4:
            respuesta = "Pinche cepillin te dedike unas chaquetotas y ni sabes q existo esmas vete a la verga puto sepillon mierda culero pendejo pelmazo ,. Ya me puse bien awitado por.tuculpa pendejo yamejor Mela.jalo.con morras no. Con un payaso guapo y cachondo ay q rico me exitas pinche cepillin putamadre"
            await message.channel.send(respuesta)
        elif cantidad == 5:
            respuesta = "bleeh bleeh FAGGOT bleeh bleeh "
            await message.channel.send(respuesta)
        return

    await bot.process_commands(message)


@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return

    if before.channel is None and after.channel is not None:
        canal = after.channel

        if member.guild.voice_client is None:
            vc = await canal.connect()
            print(f"Me uni a {canal.name}")

            bot.loop.create_task(reproducir_sonido_loop(member.guild))

async def reproducir_sonido_loop(guild):
    await bot.wait_until_ready()

    while True:
        vc = guild.voice_client

        if vc and vc.is_connected() and not vc.is_playing():
            bleeh = random.randint(0, 20)
            if bleeh==0:
                 vc.play(discord.FFmpegPCMAudio("bleeh2.mp3"))
            else:
                 vc.play(discord.FFmpegPCMAudio("bleeh1.mp3"))

        await asyncio.sleep(random.randint(0, 300)) 

@bot.command()
async def bleeh(ctx):
    vc = ctx.guild.voice_client

    if vc is None or not vc.is_connected():
        await ctx.send("no estoy en llamada bleeh")
        return

    if vc.is_playing():
        await ctx.send("ya estoy bleeheando")
        return

    vc.play(discord.FFmpegPCMAudio("bleeh1.mp3"))
    await ctx.send("bleeh")

bot.run(DISCORD_TOKEN)