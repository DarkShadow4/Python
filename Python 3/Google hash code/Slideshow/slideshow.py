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

    def __init__(self, slide_id, content, tags):
        super(Slide, self).__init__()
        self.slide_id = slide_id
        self.content = content # a list with the image or images contained
        self.tags = tags

    def typesinfo(self):
        print(str(type(self.content)) + " of " + str(type(self.content[0])))
        print(type(self.tags))

    def show_img_id(self):
        img_num = len(self.content)
        if img_num == 1:
            return str(self.content[0])
        elif img_num == 2:
            return str(self.content[0]) + " and image " + str(self.content[1])

    def showSlide(self):
        img_num = len(self.content)
        if img_num == 1:
            print("This slide contains image:\n {0}".format(self.content[0]))
        elif img_num == 2:
            print("This slide contains images:\n {0} \n and \n {1}".format(self.content[0], self.content[1]))
        else:
            print("This slide is empty")
        print("The tags contained in it are:")
        for tag in self.tags:
            print(tag, end=" ")
        print()

def getHighestValue(slides, slides2, start_costs):
    rest = Diff(slides, slides2)
    next_slides = [slide for slide in start_costs]
    highest = []
    for slide in v:
        if slide in  next_slides:
            highest.append(slide, start_costs[slide][0])
    return (sorted(highest, key=lambda x:x[1])[-1])

def most_profitable(final_costs):
    shows = [[current, final_costs[current]] for current in final_costs.keys()]
    return (sorted(shows, key=lambda x:x[1])[-1])

def dijkstra_highest_value(ss_transition_values, slides):
                                    # as i am not forced to start from one
                                    # particular image or slide, i will take the
                                    # most profitable start
    """A dijkstra variation that seeks for the most profitable slide order"""
    starts_N_puntuations = {}
    slides2 = []
    for slide in slides: # trying to start from each slide to get the best start
        slides2 = [slide]
        start_costs = get_start_costs(starting_slide)
        while Diff(slides, slides2) != []:
            highest_value = getHighestValue(slides, slides2, start_costs)
            slides2.append(highest_value[0])
            for next_slide in sorted(Diff(slides, slides2)):
                if start_costs[next_slide][0] < start_costs[highest_value[0]][0] + last_step_cost():
                    start_costs[next_slide] = [start_costs[highest_value[0]][0] + last_step_cost(), highest_value[0]]
        starts_N_puntuations[slide] = most_profitable(start_costs)
    pass

def create_adjacency_table(slides):
    """This is used in order to prepare the adjacency table for the dijkstra
    variation that gets the best order for the slides of the slide show"""
    adj_table = []
    i = 0
    while i < len(slides):
        slide_i_adj_values = []
        j = 0
        while j < len(slides):
            slide_i_adj_values.append(pair_value(slides[i], slides[j]))
            j += 1
        adj_table.append(slide_i_adj_values)
        i += 1
    return(adj_table)


def createShow(images):
    """It creates the SlideShow"""
    slides = []
    verticals = []

    for img in images: # horizontal images are always going to be in separate slides
        if img.orientation == "H":
            slides.append(Slide([img.img_id], img.tags))
        else:
            verticals.append(img)

    # Meanwhile, vertical images are the ones that can increase the points a lot
    # so it is important to give coherence to the agrupation or group 2 images
    # that have nothing to do with each other in order to get the minimum loss
    # when changing the topic of the images because 2 images in the same slide
    # having no common tags are not penalized

    # Gonna try to solve the order problem sorting the tags of each slide
    # and then sorting the slides based on the first tag, then i will try not
    # basing it on the first but compare and get the best order that i can get
    # sorting the based on the i-est tag getting more than one possible order
    # so i can select the one that gives the highest puntuation

    # I could sort them based on a dijkstra variation assigning the value of
    # each s1 s2 pair to the connection assigned and look for the highest
    # cost(value) instead of the lowest

def pair_value(slide1, slide2):
    """Function that given a pair of slides returns the points that it would get"""
    common_tags = len(slide1.tags.intersection(slide2.tags))
    in_S1_not_in_S2 = len(slide1.tags - slide2.tags)
    in_S2_not_in_S1 = len(slide2.tags - slide1.tags)
    points = sorted([common_tags, in_S1_not_in_S2, in_S2_not_in_S1])[0]
    return(points)

def ShowValue(slides):
    """Function that given a SlideShow returns the points that it would get"""
    points = 0
    if len(slides) >= 2:
        i = 0
        while i < len(slides)-1:
            points += pair_value(slides[i], slides[i+1])
            i += 1
    return(points)



####################



N = int(input())
images = []

for i in range(N):
    orientation, num_of_tags, *tags = input().split(" ") # input interpreta todo como un string, así que lo divido en una lista unterpretando que cada elemento se separa con un espacio
    images.append(Image(i, orientation, num_of_tags, tags))

slides = []
verticals = []

slide = 0
for img in images:
    if img.orientation == "H":
        slides.append(Slide(slide, [img.img_id], img.tags))
        slide += 1
    else:
        verticals.append(img)

i = 0
while i < len(verticals):
    if i+1 < len(verticals):
        slides.append(Slide(slide, [verticals[i].img_id, verticals[i+1].img_id], verticals[i].tags.union(verticals[i+1].tags)))
        i += 2
    else:
        slides.append(Slide(slide, [verticals[i].img_id], verticals[i].tags))
        i += 1
    slide += 1

for slide in slides:
    # slide.typesinfo()
    slide.showSlide()

show1 = ShowValue(slides)
print("The value of the show is: {0}".format(show1))

##############

adj_table = create_adjacency_table(slides)
print("\nAdjacency table is:")
i = 0
print("Slide    ", end="")
while i < len(adj_table):
    print("S{0}".format(i), end=" ")
    i += 1
print()
i = 0
while i < len(adj_table):
    print("Slide {0}: ".format(i), end="")
    j = 0
    while j < len(adj_table[i]):
        print(adj_table[i][j], end="  ")
        j += 1
    print()
    i += 1

####

slide_ids = [slide.slide_id for slide in slides]
dijkstra_highest_value(adj_table, slide_ids)

####

# 4
# H 3 cat beach sun
# V 2 selfie smile
# V 2 garden selfie
# H 2 garden cat
