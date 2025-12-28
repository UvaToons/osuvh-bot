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

# =========================
# CONTROL DEL LOOP
# =========================
bleeh_activo = True

@bot.event
async def on_ready():
    print("osuvh activo bleeh")

# =========================
# MENSAJES
# =========================
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    contenido = message.content.lower()

    if "nigga" in contenido:
        await message.channel.send("niggableeh")

    elif "polla" in contenido:
        await message.channel.send("pollableeh")

    elif "gaspar" in contenido:
        await message.channel.send("grasableeh")

    elif bot.user in message.mentions:
        cantidad = random.randint(1, 5)
        await message.channel.send(" ".join(["bleeh"] * cantidad))

    elif random.randint(1, 30) == 1:
        cantidad = random.randint(1, 5)
        probabilidad = random.randint(0, 18)
        probabilidad2 = random.randint(0, 3)

        palabras = [
            "semencito", "Tralaletastico", "tus bolas explotaran", "ano",
            "trisfilacutarismo", "que pasa el 20 de agosto de 1921",
            "soy mejor que el cubo gris bleeh bleeh",
            "silkson debio haber ganado el goty bleeh",
            "tu puta madre es una bleeh", "un dos tres catolica weon",
            "faggot bleeh", "*voz de maricon* bleeh", "bliih", "blue",
            "tuputamadrebleeh", "miau",
            "||https://youtu.be/SYCP71qcYZw||",
            "bliggahh bleeh", "blue"
        ]

        if probabilidad2 == 0:
            respuesta = " ".join(["bleeh"] * cantidad + [palabras[probabilidad]])
        else:
            respuesta = " ".join(["bleeh"] * cantidad)

        await message.channel.send(respuesta)

    elif random.randint(1, 50) == 1:
        cantidad = random.randint(1, 5)
        respuestas = {
            1: "pinochet tenia razón",
            2: "bleehtastico!",
            3: "callate voh puto nigga",
            4: "Pinche cepillin te dedike unas chaquetotas y ni sabes q existo...",
            5: "bleeh bleeh FAGGOT bleeh bleeh"
        }
        await message.channel.send(respuestas[cantidad])

    # IMPORTANTE: SIEMPRE AL FINAL
    await bot.process_commands(message)

# =========================
# VOICE
# =========================
@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return

    if before.channel is None and after.channel is not None:
        canal = after.channel

        if member.guild.voice_client is None:
            await canal.connect()
            print(f"Me uni a {canal.name}")
            bot.loop.create_task(reproducir_sonido_loop(member.guild))

async def reproducir_sonido_loop(guild):
    global bleeh_activo
    await bot.wait_until_ready()

    while True:
        if not bleeh_activo:
            await asyncio.sleep(1)
            continue

        vc = guild.voice_client

        if vc and vc.is_connected() and not vc.is_playing():
            if random.randint(0, 20) == 0:
                vc.play(discord.FFmpegPCMAudio("bleeh2.mp3"))
            elif random.randint(0, 50) == 0:
                vc.play(discord.FFmpegPCMAudio("bleeh3.mp3"))
            else:
                vc.play(discord.FFmpegPCMAudio("bleeh1.mp3"))

        await asyncio.sleep(random.randint(0, 300))

# =========================
# COMANDOS
# =========================
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

@bot.command()
async def niggers(ctx):
    vc = ctx.guild.voice_client

    if vc is None or not vc.is_connected():
        await ctx.send("no estoy en llamada bleeh")
        return

    if vc.is_playing():
        await ctx.send("ya llegaron los bliggas")
        return

    vc.play(discord.FFmpegPCMAudio("bleeh3.mp3"))
    await ctx.send("biggah")

@bot.command()
async def ña(ctx):
    vc = ctx.guild.voice_client

    if vc is None or not vc.is_connected():
        await ctx.send("no estoy en llamada bleeh")
        return

    if vc.is_playing():
        await ctx.send("ya estoy mariconsillo ijiji ooooh te cague")
        return

    vc.play(discord.FFmpegPCMAudio("bleeh4.mp3"))
    await ctx.send("ña")
    
@bot.command()
async def callatemierda(ctx):
    global bleeh_activo
    bleeh_activo = False

    vc = ctx.guild.voice_client
    if vc and vc.is_playing():
        vc.stop()

    await ctx.send("si ok entiendo")

@bot.command()
async def hablaamigotechupareelpene(ctx):
    global bleeh_activo
    bleeh_activo = True
    await ctx.send("si viejo estoy en el pasillo de lacteos del jumbo")

# =========================
bot.run(DISCORD_TOKEN)

