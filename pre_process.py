from PIL import Image
import os

INPUT_FOLDER = r"ur image path"  # folder with original images
OUTPUT_FOLDER = r"resize image path"   # folder to save resized images
NEW_WIDTH = 160
NEW_HEIGHT = 169
KEEP_ASPECT = True   # set False to force exact size

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Process each image
for filename in os.listdir(INPUT_FOLDER):
    input_path = os.path.join(INPUT_FOLDER, filename)
    output_path = os.path.join(OUTPUT_FOLDER, filename)

    try:
        img = Image.open(input_path)

        # Convert RGBA → RGB if needed
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img = img.resize((NEW_WIDTH, NEW_HEIGHT))

        # Save based on extension
        ext = filename.lower().split(".")[-1]

        if ext in ["jpg", "jpeg"]:
            img.save(output_path, "JPEG")
        else:
            img.save(output_path)

    except Exception as e:
        print("Error processing:", filename, "|", e)


