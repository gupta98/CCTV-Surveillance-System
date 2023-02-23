import cv2
import os
import numpy as np
from datetime import datetime as dt


def widthHeightRatioCalculator(resolution: iter, *, width: int = None, height: int = None) -> any:
    """
    widthHeightRatioCalculator(resolution: iter, width: int = None, height: int = None) -> any

    :param resolution:  An ordered iterable with two integers - the resolution.
                        Mandatory argument.

    :param width:       Given by user to calculate new height.
                        Default is None.
                        Keyword-only optional argument.

    :param height:      Given by user to calculate new width.
                        Default is None.
                        Keyword-only optional argument.

    :return:            If both width and height are None, it will return the aspect ratio.
                        If width is given, it will return the new height according to the given resolution's aspect ratio.
                        If height is given, it will return the new width according to the given resolution's aspect ratio.

    :example:           widthHeightRatioCalculator([1280, 720])               -> (16, 9)      # The aspect ratio.
                        widthHeightRatioCalculator((1280, 720), width=1600)   -> 900          # New height by maintaining the aspect ratio.
                        widthHeightRatioCalculator([1280, 720], height=900)   -> 1600         # New width by maintaining the aspect ratio.
                        widthHeightRatioCalculator()                          -> TypeError    # resolution is mandatory.
                        widthHeightRatioCalculator((1280, 720), 1600)         -> TypeError    # No position argument after resolution.
                        widthHeightRatioCalculator(resolution=[1280, 720])    -> (16, 9)      # resolution can be used as both positional and keyword argument.
    """

    if width is None and height is None:

        def gcd(num1: int, num2: int) -> int:
            if num1 > num2:
                num1, num2 = num2, num1
            while True:
                rem = num2 % num1
                if rem == 0:
                    return num1
                else:
                    num2 = num1
                    num1 = rem

        div = gcd(resolution[0], resolution[1])
        return resolution[0] // div, resolution[1] // div

    else:
        if width is not None:
            ratio = resolution[0] / resolution[1]
            return round(width / ratio)
        else:
            ratio = resolution[1] / resolution[0]
            return round(height / ratio)


def secondToDay(seconds: int) -> str:
    seconds = round(abs(seconds))
    if seconds < 60:
        return f"00:00:00:{str(seconds).zfill(2)}"
    else:
        minutes = seconds // 60
        seconds = seconds % 60
        if minutes < 60:
            return f"00:00:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        else:
            hours = minutes // 60
            minutes = minutes % 60
            if hours < 24:
                return f"00:{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
            else:
                day = hours // 24
                hours = hours % 24
                return f"{str(hours).zfill(2)}:{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


def imageStretchAndBlurNormalCamera(image, camera_name=""):
    background_image = cv2.resize(image, (350, 197), interpolation=cv2.INTER_LINEAR)
    blurred_background_image = cv2.blur(background_image, (20, 20))

    image_shape = image.shape
    image_width = image_shape[1]
    image_height = image_shape[0]
    if image_width > image_height:
        new_width = 350
        new_height = widthHeightRatioCalculator((image_width, image_height), width=new_width)
        x_offset = 0
        y_offset = (197 - new_height) // 2
    elif image_width < image_height:
        new_height = 197
        new_width = widthHeightRatioCalculator((image_width, image_height), height=new_height)
        x_offset = (350 - new_width) // 2
        y_offset = 0
    else:
        new_width = new_height = 197
        x_offset = y_offset = 0

    front_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    blurred_background_image[y_offset:y_offset + front_image.shape[0],
    x_offset:x_offset + front_image.shape[1]] = front_image

    blurred_background_image = cv2.putText(blurred_background_image, camera_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                                           fontScale=0.8, color=(0, 0, 255), thickness=2)
    now = dt.now()
    day = str(now.day).zfill(2)
    month = str(now.month).zfill(2)
    year = str(now.year).zfill(4)
    hour = str(now.strftime("%H")).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    microsecond = str(now.microsecond).zfill(6)
    time = f"{day}-{month}-{year}  {hour}:{minute}:{second}:{microsecond}"
    blurred_background_image = cv2.putText(blurred_background_image, time, (90, 190), cv2.FONT_HERSHEY_SIMPLEX,
                                           fontScale=0.5, color=(0, 0, 0), thickness=1)

    return blurred_background_image


def imageStretchAndBlurBigCamera(image, camera_name=""):
    background_image = cv2.resize(image, (709, 403), interpolation=cv2.INTER_LINEAR)
    blurred_background_image = cv2.blur(background_image, (20, 20))

    image_shape = image.shape
    image_width = image_shape[1]
    image_height = image_shape[0]
    if image_width > image_height:
        new_width = 709
        new_height = widthHeightRatioCalculator((image_width, image_height), width=new_width)
        x_offset = 0
        y_offset = (403 - new_height) // 2
    elif image_width < image_height:
        new_height = 403
        new_width = widthHeightRatioCalculator((image_width, image_height), height=new_height)
        x_offset = (709 - new_width) // 2
        y_offset = 0
    else:
        new_width = new_height = 403
        x_offset = y_offset = 0

    front_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    blurred_background_image[y_offset:y_offset + front_image.shape[0], x_offset:x_offset + front_image.shape[1]] = front_image

    blurred_background_image = cv2.putText(blurred_background_image, camera_name, (10, 55), cv2.FONT_HERSHEY_SIMPLEX,
                                           fontScale=2, color=(0, 0, 255), thickness=3)
    now = dt.now()
    day = str(now.day).zfill(2)
    month = str(now.month).zfill(2)
    year = str(now.year).zfill(4)
    hour = str(now.strftime("%H")).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    microsecond = str(now.microsecond).zfill(6)
    time = f"{day}-{month}-{year}  {hour}:{minute}:{second}:{microsecond}"
    blurred_background_image = cv2.putText(blurred_background_image, time, (135, 383), cv2.FONT_HERSHEY_SIMPLEX,
                                           fontScale=1, color=(0, 0, 0), thickness=2)

    return blurred_background_image


def nowToStr():
    now = dt.now()
    day = str(now.day).zfill(2)
    month = str(now.month).zfill(2)
    year = str(now.year).zfill(4)
    hour = str(now.strftime("%H")).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    microsecond = str(now.microsecond).zfill(6)
    time = f"{day}-{month}-{year}  {hour}_{minute}_{second}_{microsecond}"
    return time

if __name__ == "__main__":
    print(widthHeightRatioCalculator((626, 416), width=1000))
