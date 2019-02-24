import base64
import io
import os

import matplotlib.animation as animation
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from keras.engine.training import Model


def video_from_imgs(img_folder, video_file, fps):
    img_file_list = [f for f in os.listdir(img_folder) if '.png' in f]
    img_files = [os.path.join(img_folder, img_file) for img_file in sorted(img_file_list)]
    fig = plt.figure()
    myimages = []

    for file in img_files:
        img = mpimg.imread(file)
        imgplot = plt.imshow(img, animated=True);
        myimages.append([imgplot])

    ani = animation.ArtistAnimation(fig, myimages)
    ani.save(video_file, fps=fps)


def play_video_html(video_file_name):
    video = io.open(video_file_name, 'r+b').read()
    encoded = base64.b64encode(video)
    data = '''<video alt="test" controls>
                    <source src="data:video/mp4;base64,{0}" type="video/mp4" />
                 </video>'''.format(encoded.decode('ascii'))
    return data


def create_imgs_from_model(model: Model, noises: np.ndarray, img_folder: str):
    os.makedirs(img_folder, exist_ok=True)
    imgs = model.predict(noises)
    imgs = imgs * 0.5 + 0.5
    for i, img in enumerate(imgs):
        file_name = "{}.png".format(str(i).zfill(6))
        file_path = os.path.join(img_folder, file_name)
        plt.imsave(file_path, img)

def create_video_from_model(model: Model, noises: np.ndarray,
                            video_file: str, fps: int):

    imgs = model.predict(noises)
    imgs = imgs * 0.5 + 0.5
    fig = plt.figure()
    myimages = []
    for img in imgs:
        imgplot = plt.imshow(img, animated=True);
        myimages.append([imgplot])

    ani = animation.ArtistAnimation(fig, myimages)
    ani.save(video_file, fps=fps)