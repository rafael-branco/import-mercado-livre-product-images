import tkinter as tk
from tkinter import filedialog
from selenium_download_resize import download_and_resize_images_selenium  # Ensure this matches your script's structure
import chromedriver_autoinstaller

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)  # Remove current text
    folder_path_entry.insert(0, folder_selected)  # Insert the selected folder path

def start_download():
    destination_folder = folder_path_entry.get()
    mercado_livre_link = url_entry.get()
    if destination_folder and mercado_livre_link:
        download_and_resize_images_selenium(destination_folder, mercado_livre_link)
    else:
        print("Please enter both the destination folder and the URL.")



chromedriver_autoinstaller.install()

# Create the main window
root = tk.Tk()
root.title("Download and Resize Images")

# Create and pack the destination folder entry widget
folder_path_frame = tk.Frame(root)
folder_path_frame.pack(padx=10, pady=5)
folder_path_label = tk.Label(folder_path_frame, text="Destination Folder:")
folder_path_label.pack(side=tk.LEFT)
folder_path_entry = tk.Entry(folder_path_frame, width=50)
#folder_path_entry.insert(0, 'C:\\Users\\User\\Documents\\gitwork\\import-mercado-livre-product-images\\test')
folder_path_entry.pack(side=tk.LEFT, padx=5)
browse_button = tk.Button(folder_path_frame, text="Browse", command=browse_folder)
browse_button.pack(side=tk.LEFT)

# Create and pack the URL entry widget
url_frame = tk.Frame(root)
url_frame.pack(padx=10, pady=5)
url_label = tk.Label(url_frame, text="Mercado Livre URL:")
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(url_frame, width=50)
#url_entry.insert(0, "https://www.mercadolivre.com.br/creatina-monohidratada-250g-100-pura-soldiers-nutrition/p/MLB18725309#reco_item_pos=0&reco_backend=item_decorator&reco_backend_type=function&reco_client=home_items-decorator-legacy&reco_id=375fd9e7-5c08-496c-84da-8b1c86c5aea4&c_id=/home/navigation-recommendations-seed/element&c_uid=aec5e3f7-a55b-4e56-92ba-7f34243b15cd&da_id=navigation&da_position=0&id_origin=/home/dynamic_access&da_sort_algorithm=ranker")
url_entry.pack(side=tk.LEFT, padx=5)

# Create and pack the start download button
start_button = tk.Button(root, text="Start Download", command=start_download)
start_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
