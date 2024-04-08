import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'Bienvenido a este server {bot.user} ,yo soy un bot que te ayudara a cuidar el medio ambiente :)')

@bot.command()
async def sugerencia1(ctx):
    await ctx.send(f'reutiliza los plasticos')

@bot.command()
async def sugerencia2(ctx):
    await ctx.send(f'el vidrio tarda en desintegrarse mas de mil años! no lo tires')

@bot.command()
async def sugerencia3(ctx):
    await ctx.send(f'aqui te dejo un video que te ayudara: https://youtu.be/nvUqnpicSd0?feature=shared ')

@bot.command()
async def sugerencia4(ctx):
    await ctx.send(f'¿porque hay que cuidar el ambiente?: https://youtu.be/aWgHk8Mso0s?feature=shared')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            try:
                clase = (get_class (model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
                if clase == "pacman":
                    await ctx.send("Pac-Man fue creado por el diseñador Toru Iwatani, de la empresa japonesa Namco. El juego consiste en conducir a Pac-Man, una bola amarilla que abre y cierra la boca, por un laberinto. Suma puntos cuando come aquello que encuentra a su paso, bolitas y diferentes frutas, pero debe esquivar a cuatro fantasmas.")
                elif clase == "angrybirds":
                    await ctx.send("Angry Birds es un juego de precisión que consiste en lanzar pájaros contra estructuras cambiantes para destruir a los cerdos que se esconden en ellas y que, previamente, robaron los huevos a las aves. Los pájaros se mueven de diferente forma según su color, y los cerdos se ocultan a veces tras bigotes y sombreros.")
                elif clase == "candycrush":
                    await ctx.send("En el videojuego, los jugadores completan niveles intercambiando dulces de colores en un tablero de juego para hacer una combinación de tres o más del mismo color, eliminando esos dulces del tablero y reemplazándolos por otros nuevos, lo que podría crear más coincidencias.")
                elif clase == "tetris":
                    await ctx.send("El concepto de Tetris, en contraste, es asombrosamente simple: tienes que rotar y encajar unos bloques de diferentes formas que van cayendo, de manera que no queden espacios entre ellos. Apenas completas una línea horizontal, esta desaparece. Y ya.")
                elif clase == "lol":
                    await ctx.send("League of Legends es un juego de estrategia por equipos en el que dos equipos conformados por cinco poderosos campeones se enfrentan para destruir la base del otro.")
                elif clase == "fortnite":
                    await ctx.send("Este juego permite hasta a 100 personas participar juntas en una partida. Los jugadores se dejan caer en el mapa del juego y deben competir para ser el último en quedar de pie matando a todos los demás jugadores en el juego.")
                elif clase == "amongus":
                    await ctx.send("Among Us es un juego muy parecido al clásico El asesino que hemos jugado alguna vez en cartas, pero llevado al mundo de los videojuegos. Estás en una nave espacial, y dos impostores que están entre nosotros, de ahí el título, tienen que matar a los otro ocho tripulantes antes de que estos los descubran.")
                elif clase == "geometrydash":
                    await ctx.send("Se trata de un juego de plataformas retro, en el que deberemos ir saltando y volando para evitar morir a lo largo de los obstáculos que nos van apareciendo. Es el típico juego para jugar en un rato de aburrimiento una partida rápida.")
                elif clase == "minecraft":
                    await ctx.send("No hay un objetivo definido en Minecraft, ¡puedes jugar cómo quieras! Por eso se le suele llamar juego sandbox: puedes hacer montones de cosas y hay montones de formas de jugar. Si tu pasión es la creatividad, puedes usar los bloques para construir todo lo que puedas imaginar.")
                elif clase == "snake":
                    await ctx.send("En el juego, el jugador o usuario controla a una serpiente, que se desplaza a velocidad constante dentro de un plano delimitado, recogiendo alimentos (o algún otro elemento), tratando de evitar golpearse contra paredes que rodean el área de juego o su propia cola.")
                elif clase == "roblox":
                    await ctx.send("Roblox es una plataforma de entretenimiento online para jugar que permite a las personas crear juegos para el público a través de herramienta digital de Roblox conocida como Roblox Estudio. Hay literalmente millones de juegos en Roblox.")
            except:
                await ctx.send("ocurrio un error")  
    else:
        await ctx.send("Olvidaste subir la imagen :(")

bot.run("MTE3MTE5NTcwNzIyNzYzOTgwOA.GM9I66.Sei-VEh_x4RWZT3dLKoJ2sL7i8ahWbj2vc88yU")