import os
from PIL import Image

SILHOUETTE_COLOR = (30, 30, 30)
SILHOUETTE_OPACITY = 0.9


def create_dark_silhouette(input_path, output_path):
    """
    Creates a silhouette version of an image with a transparent background.

    Example usage: 
    ```
    input_image_path = './gen1/1.png'
    output_image_path = './output.png'
    create_dark_silhouette(input_image_path, output_image_path)
    ```
    """
    try:
        image = Image.open(input_path).convert('RGBA')
        new_image = Image.new('RGBA', image.size)

        for x in range(image.width):
            for y in range(image.height):
                _, _, _, a = image.getpixel((x, y))

                # Apply silhouette
                new_r, new_g, new_b = SILHOUETTE_COLOR
                silhouette_a = round(255 * SILHOUETTE_OPACITY)

                new_a = 0 if a == 0 else silhouette_a
                new_image.putpixel((x, y), (new_r, new_g, new_b, new_a))

        new_image.save(output_path)

    except Exception as e:
        print(f"Error creating silhouette for {input_path}: {e}")


def apply_to_image_folder(in_dir, out_dir, f):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    images = os.listdir(in_dir)

    for filename in images:
        in_path = os.path.join(in_dir, filename)
        out_path = os.path.join(out_dir, filename)

        # Check that file is a png image
        if os.path.isfile(in_path) and filename.lower().endswith(".png"):
            # Apply the function f
            f(in_path, out_path)


def main():
    apply_to_image_folder("./gen1", "./output", f=create_dark_silhouette)


if __name__ == "__main__":
    main()
