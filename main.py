from instabot import Bot
import time
import random


# Lista de mensajes predefinidos para comentarios
mensajes_comentarios = [
    "¡Excelente contenido!",
    "¡Me encanta tu perfil!",
    "¡Qué foto tan genial!",
    "¡Siguiendo tus pasos!",
    "¡Maravilloso!",
    "¡Impresionante!",
    "¡Hermoso!",
    "¡Sigue así!",
    "¡Muy inspirador!",
    "¡Gran contenido!"
]

# Lista de mensajes predefinidos para enviar por mensajes directos
mensajes_dm = [
    "¡Hola! Buen nombre de usuario",
    "¡Hola! Me encanta tu perfil. ",
    "¡Hola! ¿Qué tal tu día? me gustan tus publicaciones",
    "¡Hola! Sigue así con tus publicaciones.",
    "¡Hola! Estoy siguiendo tus pasos.",
    "¡Hola! Muy buen contenido.",
    "¡Hola! Continúa inspirando.",
    "¡Hola! ¡Impresionante!",
    "¡Hola! Me gusta tu estilo.",
    "¡Hola! ¡Gran trabajo!"
]

from instabot import Bot
import time
import random

# Lista de mensajes predefinidos para comentarios
# ... (código anterior) ...

# Lista de mensajes predefinidos para enviar por mensajes directos
# ... (código anterior) ...

mi_bot = Bot()
mi_bot.login(username='tu-usuario', password='tu-contrase;a')

def get_last_posts(username, num_posts):
    media = mi_bot.get_user_medias(username)
    return media[:num_posts]

def comment_on_last_posts(username, amount):
    last_posts = get_last_posts(username, 3)
    for post_id in last_posts:
        message = random.choice(mensajes_comentarios)
        mi_bot.comment(post_id, message)
        print(f"Comentario enviado a la publicación {post_id}: {message}")
        time.sleep(random.randint(10, 30))  # Pausa aleatoria entre 10 y 30 segundos

def send_message_to_user(username):
    message = random.choice(mensajes_dm)
    mi_bot.send_message(message, [username])
    print(f"Mensaje enviado a {username}: {message}")

# Hacer comentarios en los últimos 3 posts de nobat_ve
comment_on_last_posts('usuarioaseguir', 3)

# Enviar un mensaje a nobat_ve
send_message_to_user('usuarioaseguir')

# Cerrar sesión
mi_bot.logout()
