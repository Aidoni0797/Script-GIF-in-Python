from PIL import Image

# Загрузите изображения, которые будут кадрами GIF
frames = [Image.open(image) for image in ['frame1.png', 'frame2.png', 'frame3.png', 'frame4.png',
                                          'frame5.png', 'frame6.png', 'frame7.png', 'frame8.png']]

# Сохраните как анимацию GIF
frames[0].save(
    'aidoni.gif', save_all=True, append_images=frames[1:],
    duration=200, loop=0
)