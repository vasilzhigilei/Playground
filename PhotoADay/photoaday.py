import os
import cv2
import calendar
from PIL import Image

path = os.path.join(os.path.dirname(__file__), "input")
os.chdir(path)

months = list(calendar.month_name)

num_of_images = len(os.listdir('.'))

def generate_video():
    image_folder = '.'  # make sure to use your folder
    video_name = '../video.avi'
    os.chdir(path)

    if os.path.exists(video_name):
        os.remove(video_name)

    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    for image in images:
        image_location = os.path.join(image_folder, image)
        img_data = Image.open(image_location)._getexif()[36867]
        year = img_data[:4]
        month = months[int(img_data[5:7])]
        date = str(int(img_data[8:10]))
        text = month + " " + date + ", " + year
        frame = cv2.imread(image_location)
        cv2.putText(frame, text, (20, height-120), cv2.FONT_HERSHEY_SIMPLEX, 4.5, (255, 255, 255), 10)
        video.write(frame)

    cv2.destroyAllWindows()
    video.release()

generate_video()