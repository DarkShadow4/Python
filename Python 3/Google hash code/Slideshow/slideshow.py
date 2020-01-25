N = int(input())
images = []
class Image(object):
    """Image"""

    def __init__(self, orientation, num_of_tags, tags):
        super(Image, self).__init__()
        self.orientation = orientation
        self.num_of_tags = num_of_tags
        self.tags = set(tags)

    def imprimir(self):
        print(self.orientation)
        print(self.num_of_tags)
        print(self.tags)

def createShow(images):
    """It creates the SlideShow"""

for i in range(N):
    orientation, num_of_tags, *tags = input().split(" ") # input interpreta todo como un string, así que lo divido en una lista unterpretando que cada elemento se separa con un espacio
    images.append(Image(orientation, num_of_tags, tags))

for image in images:
    image.imprimir()
