import os
from argparse import ArgumentParser

from PIL import Image

from rembg import remove


def process_image(input_path, output_path):
    """Removes the background of an image and saves the output."""
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)
    print(f"Processed image saved to {output_path}")


def main():
    parser = ArgumentParser(description="Remove background from an image.")
    parser.add_argument(
        "--input",
        "-i",
        default="test_image.jpg",
        help="Give path to the input image. Default is 'test_image.jpg'.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help=(
            "Path to save the output image. Default is the input file name "
            "suffixed with '_clean'."
        ),
    )

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output or f"{os.path.splitext(input_path)[0]}_clean.png"

    process_image(input_path, output_path)


if __name__ == "__main__":
    main()
