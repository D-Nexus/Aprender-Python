import discord
from urllib import parse, request
import re
from discord.ext import commands
import random
from url_memes import enlaces

bot = commands.Bot(command_prefix= "@")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
#Saludar
@bot.command()
async def hola(ctx):
    await ctx.send("Hola :3")
#Calcular IMC
@bot.command() 
async def imc(ctx, peso: float, altura: float):
    imc = peso/(altura)**2
    estado = ""
    if (imc < 18.5):
        estado = "Estado: Bajo peso"
    elif(imc >= 18.5 and imc <= 24.9):
        estado = "Estado: Normal"
    elif(imc >= 25.0 and imc <= 29.9):
        estado = "Estado: Sobrepeso"
    else:
        estado = "Estado: Obeso"
    await ctx.send("Tu imc es: {} // {}".format(round(imc,2), estado,))
#Imprime texto en Mayusculas
@bot.command() 
async def text(ctx, *, arg):
    await ctx.send(arg.upper())
#Mostrar memes
@bot.command() 
async def meme(ctx,):
    n = random.randint(0, 9)
    await ctx.channel.send(enlaces()[n]) #Lista con los enlaces en archivo url_memes.py
#Saludar Miembros nuevos
@bot.event
async def on_member_join(member):
    await member.send("¡¡Bienvenido al G.R.E.M.I.O!!")
@bot.event
async def on_ready():
    print("A.I.C.O ONLINE")

bot.run("Aqui poner el Token")
