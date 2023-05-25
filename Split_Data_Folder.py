import os
import shutil

# Set the path to the Data folder
data_folder = "./Data"

# Create the val folder if it doesn't exist
val_folder = os.path.join(data_folder, "val")
os.makedirs(val_folder, exist_ok=True)

# Set the paths to the train and val folders
train_folder = os.path.join(data_folder, "train")
x_folder = os.path.join(train_folder, "x")
y_folder = os.path.join(train_folder, "y")

val_x_folder = os.path.join(val_folder, "x")
val_y_folder = os.path.join(val_folder, "y")

# Create the val/x and val/y folders if they don't exist
os.makedirs(val_x_folder, exist_ok=True)
os.makedirs(val_y_folder, exist_ok=True)

# Set the percentage of images to move to the val folder
split_percentage = 0.2

# Get the list of image files in the train/x and train/y folders
x_files = os.listdir(x_folder)
y_files = os.listdir(y_folder)

# Calculate the number of images to move to the val folder
num_images_to_move = int(len(x_files) * split_percentage)

# Randomly select the images to move
selected_x_files = x_files[:num_images_to_move]
selected_y_files = y_files[:num_images_to_move]

# Move the selected images from train/x to val/x
for file_name in selected_x_files:
    src = os.path.join(x_folder, file_name)
    dst = os.path.join(val_x_folder, file_name)
    shutil.move(src, dst)

# Move the selected images from train/y to val/y
for file_name in selected_y_files:
    src = os.path.join(y_folder, file_name)
    dst = os.path.join(val_y_folder, file_name)
    shutil.move(src, dst)
