class testblock:
    def __init__(self,x,y,dataset):
        self.x=x
        self.y=y
        self.dataset=dataset

    def get_testcases(self):
        testcase_filtered=self.field_selector()
        removal=[]
        for i in range(len(testcase_filtered)):
            y1 = testcase_filtered[i][0]
            x1 = testcase_filtered[i][1]
            if (self.dataset[x1][y1] == "X"):
                removal.append(testcase_filtered[i])
        for g in removal:
            testcase_filtered.remove(g)
        return testcase_filtered

    def bomb_number(self):
        x=self.x
        y=self.y
        testcase=self.field_selector()
        bomb_count = 0
        for i in range(len(testcase)):
            y1 = testcase[i][0]
            x1 = testcase[i][1]
            if (self.dataset[x1][y1] == "X"):
                bomb_count += 1
        return bomb_count

    def field_selector(self):
        x = self.x
        y = self.y
        result = self.check_box_type()
        if (result == "top left corner"):  # top left corner
            testcase = [[x + 1, y], [x + 1, y + 1], [x, y + 1]]
        elif (result == "top right corner"):  # top right corner
            testcase = [[x - 1, y], [x - 1, y + 1], [x, y + 1]]
        elif (result == "bottom left corner"):  # bottom left corner
            testcase = [[x, y - 1], [x + 1, y - 1], [x + 1, y]]
        elif (result == "bottom right corner"):  # bottom right corner
            testcase = [[x - 1, y - 1], [x, y - 1], [x - 1, y]]
        elif (result == "top middle"):  # top middle
            testcase = [[x - 1, y], [x + 1, y], [x + 1, y + 1], [x, y + 1], [x - 1, y + 1]]
        elif (result == "left middle"):  # left middle
            testcase = [[x, y - 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1], [x, y + 1]]
        elif (result == "right middle"):  # right middle
            testcase = [[x - 1, y - 1], [x, y - 1], [x - 1, y], [x - 1, y + 1], [x, y + 1]]
        elif (result == "bottom middle"):  # bottom middle
            testcase = [[x - 1, y], [x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x + 1, y]]
        elif (result == "middle"):
            testcase = [[x - 1, y + 1], [x, y + 1], [x + 1, y + 1], [x + 1, y], [x + 1, y - 1], [x, y - 1],
                        [x - 1, y - 1], [x - 1, y]]
        else:
            testcase="Out of bounds"
        return testcase

    def check_box_type(self):
        x = self.x
        y = self.y
        row=len(self.dataset)
        col=len(self.dataset[0])
        if (x > row-1 or x<0 or y>col-1 or y<0):
            print("Out of bounds")
            return("error")
        else:
            if (x==0 and y==0): #top left corner
                return("top left corner")
            elif (x==row-1 and y==0): #top right corner
                return("top right corner")
            elif (x==0 and y==col-1): #bottom left corner
                return("bottom left corner")
            elif (x==row-1 and y==col-1): #bottom right corner
                return("bottom right corner")
            elif (y==0): #top middle
                return("top middle")
            elif (x==0): #left middle
                return("left middle")
            elif (x==row-1): #right middle
                return("right middle")
            elif (y==col-1): #bottom middle
                return("bottom middle")
            else:
                return("middle")

    def neighbour_blocks(self):
        surrounding_blocks = []
        new_set = self.get_testcases()
        for i in new_set:
            x = testblock(i[0], i[1],self.dataset)
            if x.bomb_number() == 0:
                surrounding_blocks.append([i[0], i[1]])
            del x
        return surrounding_blocks

