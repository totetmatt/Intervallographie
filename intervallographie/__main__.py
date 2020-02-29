import argparse
import glob
import os

import numpy as np
from PIL import Image


#### Direction ####


def leftToRight(nb_files, current_index, w_size):
    """
        Going left to right
    """
    return current_index * w_size


def rightToLeft(nb_files, current_index, w_size):
    """
        Going right to left
    """
    return (nb_files - 1 - current_index) * w_size


### Proccess ###


def process(input_dir="./imgs/", output_file="out_phototimelapse.jpg", direction="ltr"):
    files = glob.glob(os.path.join(input_dir, "*.JPG"))
    nb_files = len(files)

    image = np.array(Image.open(files[0]))

    h, w, _ = image.shape
    w_size = (w // nb_files) + 1

    directionMethod = leftToRight
    if direction == "rtl":
        directionMethod = rightToLeft

    for idx, data in enumerate(files[1:], 1):
        offset = directionMethod(nb_files, idx, w_size)
        image[:, offset : w_size + offset] = np.array(Image.open(data))[
            :, offset : w_size + offset
        ]

    Image.fromarray(image).save(output_file)


def run():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("input_dir", action="store")
    parser.add_argument("output_file", action="store")
    parser.add_argument(
        "--direction", action="store", choices=["ltr", "rtl"], default="ltr"
    )
    args = parser.parse_args()
    process(args.input_dir, args.output_file, args.direction)


### Cli entrypoint ###
if __name__ == "__main__":
    run()

