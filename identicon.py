from PIL import Image, ImageDraw
from random import random, choice

# SETTINGS
N_CHUNK = 5
MIDDLE = N_CHUNK // 2+1
BORDER = 20
SIZE = 420
PLACE_PROBABILITY = 0.5
COLOR = choice([(210, 107, 74), (127, 225, 138), (168, 126, 223), (204, 160, 79)])  # COLOR PALETTE


def main():

    img = Image.new("RGB", (SIZE, SIZE), (240, 240, 240))

    for i in range(MIDDLE):
        for n in range(N_CHUNK):
            img = place_chunk(img, i, n)

    img.save("identicon.jpg")
    img.show()


def place_chunk(img, i, n):  # CALL CHUNK FUNCTION SYMMETRICALLY

    if random() > PLACE_PROBABILITY:
        chunk(img, i + 1, n + 1)
        if i != MIDDLE:
            print(MIDDLE + (abs(MIDDLE - i) - 1))
            chunk(img, MIDDLE + (abs((MIDDLE - i)) - 1), n + 1)
        else:
            pass
    return img


def chunk(img, x, y):  # PLACE CHUNK OF COLOR IN THE IMAGE

    if x > N_CHUNK or y > N_CHUNK:
        raise Exception("Out of range! X:{}\tY:{}".format(x, y))

    w, h = ((e - 2 * BORDER) / N_CHUNK for e in img.size)

    draw = ImageDraw.Draw(img)

    x0 = w * (x - 1) + BORDER
    x1 = w * x + BORDER
    y0 = h * (y - 1) + BORDER
    y1 = h * y + BORDER

    draw.rectangle(((x0, y0), (x1, y1)), COLOR)

    return img


if __name__ == '__main__':
    if N_CHUNK % 2 != 0:
            main()
    else:
        raise Exception("N_CHUNK need to be odd")
