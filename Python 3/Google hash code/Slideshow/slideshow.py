class Image(object):
    """Image"""

    def __init__(self, img_id, orientation, num_of_tags, tags):
        super(Image, self).__init__()
        self.img_id = img_id
        self.orientation = orientation
        self.num_of_tags = num_of_tags
        self.tags = set(tags)

    def imprimir(self):
        print(self.orientation)
        print(self.num_of_tags)
        print(self.tags)

class Slide(object):
    """A slide containing one horizontal or vertical image or 2 vertical images"""

    def __init__(self, content, tags):
        super(Slide, self).__init__()
        self.content = content # a list with the image or images contained
        self.tags = tags

    def show_img_id(self):
        img_num = len(self.content)
        if img_num == 1:
            return str(self.content[0])
        elif img_num == 2:
            return str(self.content[0]) + " and image " + str(self.content[1])

    def showSlide(self):
        img_num = len(self.content)
        if img_num == 1:
            print("This slide contains image:\n {0}".format(self.content[0].imprimir()))
        elif img_num == 2:
            print("This slide contains images:\n {0} \n and \n {1}".format(self.content[0].imprimir(), self.content[1].imprimir()))
        else:
            print("This slide is empty")
        print("The tags contained in it are:")
        for tag in self.tags:
            print(tag, end=" ")
        print()




def createShow(images):
    """It creates the SlideShow"""
    pass


N = int(input())
images = []

for i in range(N):
    orientation, num_of_tags, *tags = input().split(" ") # input interpreta todo como un string, así que lo divido en una lista unterpretando que cada elemento se separa con un espacio
    images.append(Image(id, orientation, num_of_tags, tags))

slides = []
verticals = []

for img in images:
    if img.orientation == "H":
        slides.append(Slide([img.img_id], img.tags))
    else:
        verticals.append(img)

for i in range(len(verticals)):
    if i+1 < len(verticals):
        slides.append(Slide([verticals[i].img_id, verticals[i+1].img_id], verticals[i].tags.union(verticals[i+1].tags)))
    else:
        slides.append(Slide([verticals[i].img_id], verticals[i].tags))

for slide in slides:
    slide.showSlide()

# for image in images:
#     image.imprimir()
