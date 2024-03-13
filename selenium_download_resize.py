import os
import logging
from selenium import webdriver
from PIL import Image
import requests
from io import BytesIO
from selenium.webdriver.common.by import By

# Setup logging
logging.basicConfig(filename='image_download_resize_selenium.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_and_resize_images_selenium(folder, url):
    try:
        logging.info("Starting download process for URL with Selenium: %s", url)
        print(f"Starting download process for URL with Selenium: {url}")

        # Setup Selenium Chrome WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in background
        driver = webdriver.Chrome(options=options)

        # Open the URL
        driver.get(url)

        # Find images by CSS selector
        images = driver.find_elements(By.CSS_SELECTOR ,'.ui-pdp-gallery__figure img')
        if not images:
            logging.warning("No images found at the specified URL.")
            print("No images found at the specified URL.")
            return

        # Ensure the destination folder exists
        if not os.path.exists(folder):
            os.makedirs(folder)
            logging.info("Created destination folder: %s", folder)
            print(f"Created destination folder: {folder}")

        for i, img in enumerate(images):
            img_url = img.get_attribute('src')
            if img_url.startswith('data:image'):
                logging.info("Skipping base64 embedded image.")
                continue  # Skip base64 embedded images

            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                # Resize the image
                img_obj = Image.open(BytesIO(img_response.content))
                original_size = img_obj.size
                resized_img = img_obj.resize((original_size[0]*2, original_size[1]*2))
                
                # Save the image
                image_path = os.path.join(folder, f"image_{i}.jpg")
                resized_img.save(image_path)
                logging.info("Downloaded and resized image saved to: %s", image_path)
                print(f"Downloaded and resized image saved to: {image_path}")
            else:
                logging.warning("Failed to download image from: %s", img_url)
                print(f"Failed to download image from: {img_url}")

        driver.quit()
    except Exception as e:
        logging.exception("An error occurred during the download and resize process with Selenium.")
        print(f"An error occurred: {e}")

# Example usage
destination_folder = 'path_to_destination_folder'
mercado_livre_link = 'mercado_livre_link_here'
download_and_resize_images_selenium(destination_folder, mercado_livre_link)
