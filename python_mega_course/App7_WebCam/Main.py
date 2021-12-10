import cv2
import glob
import pathlib


imfiles = glob.glob('sample_images/*.jpg')

print(imfiles)

for file in imfiles:

    img = cv2.imread(file, 0)

    print(type(img))
    print(img)
    print((img.shape)[0])

    resized_img = cv2.resize(img, dsize=(100, 100))
    resize_name = str(pathlib.Path(file).parent) + "/resized_" + pathlib.Path(file).stem + pathlib.Path(file).suffix
    print(resize_name)

    cv2.imshow(resize_name, resized_img)
    cv2.imwrite(resize_name, resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



