# Image Background Removal with Rembg

This project uses the **Rembg** library to remove the background from images. 
<!-- It also supports running inside a Docker container to easily deploy the functionality. -->

## Features

-   Background removal using **Rembg** (based on **u2net** model).
-   Process images from the command line with flexible input and output paths.
<!-- -   Built-in Docker support for easy deployment. -->

## Prerequisites

### Python Environment

-   Python 3.11 or later.
-   Required Python libraries are listed in the `pyproject.toml` file.
-   To add packages, add package name in `pyproject.toml`.

<!-- ### Docker (Optional)

If you prefer running the project inside Docker instead of setting up a local Python environment, Docker is also supported. -->

## Installation

### install uv first

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

check this [link](https://docs.astral.sh/uv/#highlights) for details on `uv`

### 1. Clone the repository

```bash
git clone https://github.com/tamim87/image-background-removal.git
cd image-background-removal
```

### 2. Create and activate the virtual environment (Linux/macOS)

```bash
uv venv venv
source venv/bin/activate
```

or

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install necessary dependencies

```bash
uv pip compile -o requirements.txt pyproject.toml
```

```bash
uv pip sync requirements.txt
```

## Usage

Command-Line Usage

Run the script to remove the background from an image.

```bash
python main.py --input <input_image> --output <output_image>
```

    --input or -i (Required): Path to the input image.
    --output or -o (Optional): Path to the output image. If not provided, the default output will be the input image filename with suffix "_clean" appended.

Example:

```bash
python main.py --input img_1.JPG --output img_1_clean.png
```

If no --output is provided, the output will be:

python main.py --input img_1.JPG

This will generate a new file named img_1_clean.png.
Default Test Image

If no input image is provided, the script will process a default image located in the project directory, test_image.JPG.
