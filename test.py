from PIL import Image
import os

def test_images_dimensions(directory_path):
    """
    Tests if all images within a directory have a width and height
    greater than or equal to 500 pixels.

    :param directory_path: Path to the directory containing the images.
    """
    # List to keep track of images that do not meet the criteria
    failed_images = []

    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        # Construct the full path to the file
        file_path = os.path.join(directory_path, filename)
        
        # Skip if it's not a file
        if not os.path.isfile(file_path):
            continue

        try:
            # Open the image file
            with Image.open(file_path) as img:
                width, height = img.size
                
                # Check if both dimensions are greater than or equal to 500
                if width < 500 or height < 500:
                    failed_images.append(filename)
                    
        except IOError:
            # This catches files that are not images or are corrupted
            print(f"Could not process file {filename}. It may not be an image file.")
    
    # Check if there were any failed images
    if failed_images:
        print("Test Failed for the following images (width and/or height less than 500 pixels):")
        for failed_image in failed_images:
            print(failed_image)
    else:
        print("Test Passed: All images are greater than or equal to 500 pixels in both dimensions.")

# Example usage
directory_path = 'C:\\Users\\User\\Documents\\gitwork\\import-mercado-livre-product-images\\test'
test_images_dimensions(directory_path)
