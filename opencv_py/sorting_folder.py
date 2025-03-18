import os
import shutil

def convert_folder_format(base_dir):
    # Iterate over each date folder
    for date_folder in os.listdir(base_dir):
        date_folder_path = os.path.join(base_dir, date_folder)

        if os.path.isdir(date_folder_path):
            # Paths for the 'inner' and 'outer' image directories
            inner_folder_path = os.path.join(date_folder_path, '2025_02_17_inner')
            outer_folder_path = os.path.join(date_folder_path, '2025_02_17_outer')

            # Iterate over image ID folders (1 to 99)
            for image_id in range(1, 100):
                # Create the folder for each image_id (if it doesn't already exist)
                id_folder_path = os.path.join(date_folder_path, str(image_id))
                if not os.path.exists(id_folder_path):
                    os.makedirs(id_folder_path)
                    print(id_folder_path)

                # Process images from the inner folder
                inner_id_folder = os.path.join(inner_folder_path, str(image_id))
                if os.path.isdir(inner_id_folder):
                    for img_file in os.listdir(inner_id_folder):
                        if img_file.endswith('.jpg'):
                            timestamp = img_file.split('.')[0]  # Extract timestamp part
                            # Rename and copy the image with 'inner_' prefix
                            new_img_name = f"inner_{timestamp}.jpg"
                            shutil.copy(os.path.join(inner_id_folder, img_file), os.path.join(id_folder_path, new_img_name))

                # Process images from the outer folder
                outer_id_folder = os.path.join(outer_folder_path, str(image_id))
                if os.path.isdir(outer_id_folder):
                    for img_file in os.listdir(outer_id_folder):
                        if img_file.endswith('.jpg'):
                            timestamp = img_file.split('.')[0]  # Extract timestamp part
                            # Rename and copy the image with 'outer_' prefix
                            new_img_name = f"outer_{timestamp}.jpg"
                            shutil.copy(os.path.join(outer_id_folder, img_file), os.path.join(id_folder_path, new_img_name))

# Example usage
base_directory = 'C:\\office works\RWF\\'  # Replace with the actual path to your base directory
convert_folder_format(base_directory)

