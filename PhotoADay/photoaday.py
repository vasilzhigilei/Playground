import os
import cv2
import calendar
import datetime
from PIL import Image

path = os.path.join(os.path.dirname(__file__), "input")
os.chdir(path)

months = list(calendar.month_name)
days = list(calendar.day_name)

num_of_images = len(os.listdir('.'))

def generate_video():
    """
    Function to generate video using input files in relative folder input
    outputs to relative file video.avi
    :return: None
    """
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

    # loop through all images
    for image in images:
        # get image location
        image_location = os.path.join(image_folder, image)
        # get date and time information
        img_data = Image.open(image_location)._getexif()[36867]

        date = datetime.datetime(int(img_data[:4]), int(img_data[5:7]), int(img_data[8:10]), int(img_data[11:13]), int(img_data[14:16]))

        weekday = date.weekday()
        date_string = str(calendar.month_name[date.month]) + " " + str(date.day) + ", " + str(date.year)

        # read frame from image location
        frame = cv2.imread(image_location)
        # add two texts, day of the week above and larger
        cv2.putText(frame, calendar.day_name[weekday], (30, height - 190), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 13, cv2.LINE_AA)
        cv2.putText(frame, date_string, (30, height-70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 10, cv2.LINE_AA)
        # write video frame
        video.write(frame)

    # cleanup
    cv2.destroyAllWindows()
    video.release()

# Call video generator
generate_video()