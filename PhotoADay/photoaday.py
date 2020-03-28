import os
import cv2
from PIL import Image

path = os.path.join(os.path.dirname(__file__), "input")
os.chdir(path)

num_of_images = len(os.listdir('.'))

def generate_video():
    image_folder = '.'  # make sure to use your folder
    video_name = 'video.avi'
    os.chdir(path)

    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

generate_video()