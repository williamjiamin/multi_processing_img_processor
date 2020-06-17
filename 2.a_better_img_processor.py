# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
from PIL import Image, ImageFilter
import time
import concurrent.futures

img_box = ['photo-1583425423320-2386622cd2e4.jpg',
           'photo-1590933937035-8a095cd97175.jpg',
           'photo-1591643529995-aef2e1e6f281.jpg',
           'photo-1591708645323-82edcccab226.jpg',
           'photo-1591759092107-d55d53e2e250.jpg',
           'photo-1591777877953-786783dd25e7.jpg',
           'photo-1591791077933-3b5446a113b7.jpg',
           'photo-1591793217615-4581d5d05f0b.jpg',
           'photo-1591882351016-6f26999cea0a.jpg',
           'photo-1591868283584-abe4232655b7.jpg']

start_time = time.perf_counter()

resize = (500, 500)


def process_our_img(every_img):
    img = Image.open(every_img)
    img = img.filter(ImageFilter.GaussianBlur(20))
    img = img.filter(ImageFilter.GaussianBlur(20))
    img = img.filter(ImageFilter.GaussianBlur(20))
    img = img.filter(ImageFilter.GaussianBlur(20))
    img = img.filter(ImageFilter.GaussianBlur(20))

    img.thumbnail(resize)
    img.save(f'changed/{every_img}')
    print(f'{every_img}已经处理完毕～～～')


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_our_img, img_box)

end_time = time.perf_counter()

print(f'所有图片处理完毕，一共花费{end_time - start_time}秒完成')
