from PIL import Image


def resize_image(size1, size2):
    image = Image.open('test.jpg')

    print(f"Current size: {image.size}")

    resized_image = image.resize((size1, size2))
    resized_image.save('test' + str(size1) + 'x' + str(size2) + '.jpg')


size1 = int(input('Enter width: '))
size2 = int(input('Enter height: '))
resize_image(size1, size2)
