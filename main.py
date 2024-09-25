from flask import Flask
import random as r

app = Flask(__name__)

datos_interesantes = ["Las tortugas pueden definir su sexo gracias a la temperatura del ambiente",
                      "Estudios con resonancias magnéticas han mostrado que el uso intensivo de dispositivos digitales puede alterar la estructura del cerebro, afectando áreas responsables del control de impulsos, empatía y toma de decisiones.",
                      "La dependencia con el entretenimiento electrónico, los juegos virtuales, entre otros, además de afectar la salud a la larga conllevaal individuo al aislamiento y a perder el contacto con la realidad social, emocional y familiar, logrando reducir la habilidad de interacción social y la productividad.",
                      "El término Phubbing combina las palabras /phone/ y /snubbing/ (despreciar) y se refiere al acto de ignorar a las personas con quienes estás físicamente al prestar más atención a tu teléfono.",
                      "Las redes sociales están diseñadas para ser adictivas. El modelo de negocio de plataformas como Instagram, Facebook o TikTok se basa en la creación de experiencias que retienen la atención de los usuarios el mayor tiempo posible mediante notificaciones, <3me gusta<3 y comentarios.",
                      "Al recopilar enormes cantidades de datos personales, las plataformas no solo personalizan la experiencia, sino que pueden predecir y manipular comportamientos futuros",
                      "Los dientes humanos son la única parte del cuerpo que no puede curarse por sí misma. Los dientes están recubiertos de esmalte, que no es un tejido vivo.",
                      "Estados Unidos intentó usar gatos para espiar en la década de 1960 como parte de un proyecto secreto de la CIA llamado /Acoustic Kitty/."]

@app.route("/")
def hello_world():
    a = "<p>Welcome to the web :3</p>"
    url = "<a href = '/random_fact'>¿Quieres conocer un dato nuevo?</a>"
    url1 = "<a href = '/img'>Tortuga 🐢</a>"
    return f"<h1>Hello, World!</h1>{a}{url}<br><br>{url1}"

@app.route("/random_fact")
def fact_giver():
    ranfact = r.choice(datos_interesantes)
    return f"<h2>{ranfact}<h2>"


@app.route("/img")
def image():
    imagen_url = 'https://th.bing.com/th/id/R.c2bfd00d4f815dc6c8b7f878ce3f5438?rik=IiyCsJ0sbM1ktw&pid=ImgRaw&r=0'
    return f'<img src="{imagen_url}" alt="Imagen de tortuga">'

app.run(debug=True)
