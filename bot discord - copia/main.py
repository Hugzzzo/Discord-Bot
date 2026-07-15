import discord
from discord.ext import commands
import requests
import secret

intents = discord.Intents.all()

bot= commands.Bot(command_prefix="&", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")



@bot.command()
async def canal_texto(ctx, *, nombre):
    nuevo_text_canal = await ctx.guild.create_text_channel(
    nombre,
    position=len(ctx.guild.text_channels)
)
    await nuevo_text_canal.send("🎉 ¡Bienvenido al canal!")
   
    await ctx.send(f"✅ Se ha creado {nuevo_text_canal.mention}")

@bot.command()
async def canal_voz(ctx, *, nombre):
    nuevo_voice_canal = await ctx.guild.create_voice_channel(
        nombre,
        position=len(ctx.guild.voice_channels)
    )
    await ctx.send(f"✅ Se ha creado {nuevo_voice_canal.mention}")

@bot.command()
async def eliminar_canal(ctx, *, nombre):
    canal = discord.utils.get(ctx.guild.channels, name=nombre)
    if canal:
        await canal.delete()
        await ctx.send(f"✅ Se ha eliminado {canal.mention}")
    else:
        await ctx.send("❌ Canal no encontrado")

@bot.command()
async def vaciar_canal(ctx, *, nombre):

    canal = discord.utils.get(ctx.guild.channels, name=nombre)

    if canal:
        await canal.purge()
        await ctx.send("✅ Canal vaciado correctamente.")
    else:
        await ctx.send("❌ Canal no encontrado.")



bot.run(secret.TOKEN)
