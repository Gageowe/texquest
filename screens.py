class Screen:
    def __init__(self, content = None, icon = "*",width = 40, height = 10, top = 1, bottom = 1, left = 1, right = 1):
        self.content = content
        self.width = width
        self.height = height
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.length = len(content)
        self.messageContent = []
        self.message = []
        self.rowSpace = self.width - self.left - self.right
        self.colSpace = self.height - self.top - self.bottom
        self.icon = icon
        self.lSpace = int((self.rowSpace - self.length)/2)
        self.rSpace = int((self.rowSpace - self.length +1 )/2)
        if self.length <= (self.rowSpace):
            self.messageContent.append(self.content)
            self.rows = 1
        else:
            self.rows = int(self.length/self.rowSpace) + 1
        for row in range(0,self.rows):
            if (row + 1)*self.rowSpace > self.length:
                self.messageContent.append(self.content[row*self.rowSpace])
            else:
                self.messageContent.append(self.content[row*self.rowSpace:(row+1)*self.rowSpace])
        print(self.messageContent)
        self.tSpace = int((self.colSpace - self.rows)/2)
        self.bSpace = int((self.colSpace - self.rows + 1)/2)
        for row in range(0,self.height):
            self.message.append("")
            self.rowNum = 0
            if row < top or row > (height - 1 - bottom):
                 for i in range(self.width):
                     self.message[row] += self.icon
            elif (row >= self.top and row < self.top + self.tSpace) or (row <= self.height - self.bottom and row >= self.top + self.tSpace + self.rows):
                for i in range(self.width):
                    if i < self.left or i >= self.width - self.right:
                        self.message[row] += self.icon
                    else:
                        self.message[row] += " "
            else:
                for i in range(self.width):
                    if i < self.left or i >= self.width - self.right:
                        self.message[row] += self.icon
                    elif i < self.left + self.lSpace or i >= self.width - self.right - self.rSpace:
                        self.message[row] += " "
                    elif i == self.left + self.lSpace + 1:
                        self.message[row] += self.messageContent[self.rowNum]
                        self.rowNum += 1
        self.content = ""
        for row in self.message:
            self.content += row + "\n"
    def show(self):
        print(self.content)
