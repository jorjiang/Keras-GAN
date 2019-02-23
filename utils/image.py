import base64
import io

import matplotlib.animation as animation
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
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
