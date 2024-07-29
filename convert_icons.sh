#!/bin/bash

# Check if ImageMagick is installed
if ! command -v convert &> /dev/null; then
    echo "ImageMagick is not installed. Please install it first."
    exit 1
fi

# Check for the correct number of arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_image.png>"
    exit 1
fi

# Input image file
input_image="$1"

# List of icon sizes
sizes=("16x16" "32x32" "48x48" "180x180" "192x192" "512x512")

# Loop through sizes and create icons
for size in "${sizes[@]}"; do
    output_file="${input_image%.*}_${size}.png"
    convert "$input_image" -resize "$size" "$output_file"
    echo "Created: $output_file"
done

echo "Icons generated successfully."
