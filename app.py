from flask import Flask, render_template, request, jsonify
from PIL import Image
import base64
import webcolors
import io
import random

app = Flask(__name__)


@app.route("/")
def index():
    width = int(64)
    height = int(64)
    colors = get_random_colors(3)
    image_data = create_image(width, height, colors)

    return render_template("index.html", image_data=image_data, width=width, height=height, colors=colors)


@app.route("/generate", methods=["POST"])
def generate():
    width = int(request.form["width"])
    height = int(request.form["height"])
    colors = request.form.getlist("colors[]")
    colors = get_random_colors(len(colors))
    image_data = create_image(width, height, colors)

    return render_template("index.html", image_data=image_data, width=width, height=height, colors=colors)


@app.route("/refresh", methods=["POST"])
def refresh():
    width = int(request.form["width"])
    height = int(request.form["height"])
    colors = request.form.getlist("colors[]")
    image_data = create_image(width, height, colors)

    return jsonify(image_data=image_data)


def create_image(width, height, colors):
    img = Image.new("RGB", (width, height), "white")
    pixels = img.load()
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            color = random.choice(colors)
            pixels[i, j] = webcolors.hex_to_rgb(color)

    scale = get_scale(width, height)
    img = img.resize(tuple(scale * x for x in img.size), resample=Image.NEAREST, box=None)

    # save the image to a buffer
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    # encode the image data
    image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return image_data


def get_random_colors(length):
    return ["#{:02x}{:02x}{:02x}".format(random.randint(0, 255),
                                         random.randint(0, 255),
                                         random.randint(0, 255)) for _ in range(length)]


def get_scale(width, height):
    max_value = max(width, height)
    if (max_value // 10) < 10:
        scale = 100
    elif 10 < (max_value // 10) < 100:
        scale = 1
    else:
        scale = 10

    return scale


if __name__ == "__main__":
    app.run(debug=True)
