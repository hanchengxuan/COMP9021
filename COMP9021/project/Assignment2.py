# COMP9021 21T3 - Rachid Hamadi
# Assignment 2 *** Due Monday Week 11 @ 10.00am

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# IMPORT ANY REQUIRED MODULE

movelist = [(-1, 0), (1, 0), (0, -1), (0, 1),(1,-1),(-1,1),(1,1)]
movelist2 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class MazeError(Exception):
    def __init__(self, message):
        self.message = message


class Maze:
    def __init__(self, filename):
        self.filename=filename
        with open(filename, 'r') as f:
            self.initmazegrid = f.readlines()

        self.mazegrid=[]                                            #put grid into a digit list
        for i in range(len(self.initmazegrid)):
            rowlist = []
            for j in range(len(self.initmazegrid[i])):
                if self.initmazegrid[i][j].isdigit():
                    rowlist.append(int(self.initmazegrid[i][j]))
            if rowlist:
                self.mazegrid.append(rowlist)

        self.wallsgrid=[]                                           #seperate grid for walls search
        for i in range(len(self.initmazegrid)):
            rowlist = []
            for j in range(len(self.initmazegrid[i])):
                if self.initmazegrid[i][j].isdigit():
                    rowlist.append(int(self.initmazegrid[i][j]))
            if rowlist:
                self.wallsgrid.append(rowlist)

        for i in range(len(self.mazegrid)):                         #test input
            for j in range(len(self.mazegrid[i])):
                if self.mazegrid[i][j] not in [0,1,2,3]:
                    raise MazeError('Incorrect input.')
        for i in range(len(self.mazegrid)-1):
            if len(self.mazegrid[i])!=len(self.mazegrid[i+1]):
                raise MazeError('Incorrect input.')
        if len(self.mazegrid)<2 or len(self.mazegrid)>41:
            raise MazeError('Incorrect input.')
        for i in range(len(self.mazegrid)):
            if len(self.mazegrid[i])<2 or len(self.mazegrid[i])>31:
                raise MazeError('Incorrect input.')
        for i in range(len(self.mazegrid)):
            if self.mazegrid[i][-1] in [1,3]:
                raise MazeError('Input does not represent a maze.')
        for i in self.mazegrid[-1]:
            if i in [2,3]:
                raise MazeError('Input does not represent a maze.')

        gate = 0
        self.gatelist = []
        for i in range(len(self.mazegrid) - 1):  # find gates in vertical sides
            if self.mazegrid[i][0] == 0:
                gate += 1
                self.gatelist.append((i, 0))
            if self.mazegrid[i][-1] == 0:
                gate += 1
                self.gatelist.append((i, len(self.mazegrid[i]) - 1))
            if (self.mazegrid[i][0], self.mazegrid[i + 1][0]) in [(1, 3), (1, 1), (1, 2), (1, 0)]:
                gate += 1
                self.gatelist.append((i, 0))

        for j in range(len(self.mazegrid[0]) - 1):  # find gates in horizontal sides
            if self.mazegrid[0][j] == 0:
                gate += 1
                self.gatelist.append((0, j))
            if self.mazegrid[0][j] == 2:
                if self.mazegrid[0][j + 1] in [0, 1, 2, 3]:
                    gate += 1
                    self.gatelist.append((0, j))
        if self.mazegrid[0][-2] == 2 and self.mazegrid[0][-1] == 0:
            gate += 1
            self.gatelist.append((0, len(self.mazegrid[0]) - 2))

        for j in range(len(self.mazegrid[-1]) - 1):
            if self.mazegrid[-1][j] == 0:
                gate += 1
                self.gatelist.append((len(self.mazegrid) - 1, j))

        # findwall:
        self.walltotal = []
        for i in range(len(self.wallsgrid)):
            for j in range(len(self.wallsgrid[i])):
                tempi = i
                tempj = j
                if self.wallsgrid[i][j] in [1, 2, 3]:
                    self.wallList = []
                    Maze.find_walls(self, i, j, self.wallList)
                    if self.wallList:
                        for (i, j) in self.wallList:
                            self.wallsgrid[i][j] = 99
                        self.walltotal.append(self.wallList)
                i = tempi
                j = tempj

        # findinnerpoints:
        self.pointtotal = []
        for i in range(len(self.mazegrid)):
            for j in range(len(self.mazegrid[i])):
                isgate = 0
                (tempi, tempj) = (i, j)
                if (i, j) not in self.pointtotal:
                    if (i, j) not in self.gatelist:
                        self.pointlist = []
                        Maze.find_inner_point(self, i, j, self.pointlist)
                        for anypoint in self.pointlist:
                            if anypoint in self.gatelist:
                                isgate = 1
                        if isgate == 0:
                            for anypoint in self.pointlist:
                                self.pointtotal.append(anypoint)
                (i, j) = (tempi, tempj)

        # findaccessiblearea:
        self.areatotal = []
        self.num_area = 0
        for i in range(len(self.mazegrid)):
            for j in range(len(self.mazegrid[i])):
                isgate = 0
                (tempi, tempj) = (i, j)
                if (i, j) not in self.areatotal:
                    if (i, j) in self.gatelist:
                        self.pointlist = []
                        Maze.find_inner_point(self, i, j, self.pointlist)
                        for anypoint in self.pointlist:
                            if anypoint in self.gatelist:
                                isgate = 1
                        if isgate == 1:
                            self.num_area += 1
                            for anypoint in self.pointlist:
                                self.areatotal.append(anypoint)
                (i, j) = (tempi, tempj)

        #find cul_de_sacs
        self.cdstotal = []
        num_cds = 0
        for (i, j) in self.gatelist:
            if (i, j) not in self.cdstotal:
                self.pointlist = []
                self.cdslist = []
                self.cdslist2 = []
                self.cdslist3 = []
                Maze.find_cul_de_sacs2(self, i, j, self.pointlist, self.cdslist, self.gatelist)
                for anypoint in self.cdslist:
                    if anypoint not in self.cdstotal:
                        self.cdslist2.append(anypoint)
                if self.cdslist2:
                    for (i, j) in self.cdslist2:
                        not_in_cdslist = 0
                        self.nextlist = []
                        Maze.find_nextpoint(self, i, j, self.nextlist)
                        for nextpoint in self.nextlist:
                            if nextpoint not in self.cdslist2:
                                not_in_cdslist += 1
                        if not_in_cdslist == 0:
                            self.cdslist3.append((i, j))
                        else:
                            self.cdslist3.append((i, j))
                            if self.cdslist3 and self.cdslist3 not in self.cdstotal:
                                self.cdstotal.append(self.cdslist3)
                            self.cdslist3 = []
                    if self.cdslist3 and self.cdslist3 not in self.cdstotal:
                        self.cdstotal.append(self.cdslist3)
        self.cdstotallist = []
        for allcds in self.cdstotal:
            for allcdspoint in allcds:
                self.cdstotallist.append(allcdspoint)

        #find path
        self.pathtotal = []
        self.num_path = 0
        for (i, j) in self.gatelist:
            if (i, j) not in self.cdstotallist:
                if (i, j) not in self.pathtotal:
                    isgate = 0
                    ispath = 1
                    self.pointlist = []
                    Maze.find_path(self, i, j, self.pointlist, self.cdstotallist)
                    for anypoint in self.pointlist:
                        if anypoint in self.gatelist:
                            isgate += 1
                    for (i, j) in self.pointlist:
                        if Maze.find_cango(self, i, j, self.cdstotallist, self.gatelist) != 2:
                            ispath = 0
                    if isgate == 2 and ispath == 1:
                        self.num_path += 1
                        for anypoint in self.pointlist:
                            self.pathtotal.append(anypoint)
                    if isgate == 1 and (i, j) == (0, 0) and len(self.pointlist) == 1:
                        self.num_path += 1
                        for anypoint in self.pointlist:
                            self.pathtotal.append(anypoint)

        #findpillar:
        self.pillar=[]
        for i in range(len(self.mazegrid)):
            for j in range(len(self.mazegrid[i])):
                if self.mazegrid[i][j]==0:
                    if Maze.find_pillar(self,i,j)==2:
                        self.pillar.append((i,j))


        # REPLACE PASS ABOVE WITH YOUR CODE




    # POSSIBLY DEFINE OTHER METHODS


    def analyse(self):
        gate=len(self.gatelist)
        if gate == 0:
            print("The maze has no gate.")
        elif gate == 1:
            print("The maze has a single gate.")
        else:
            print(f"The maze has {gate} gates.")


        num_walls=len(self.walltotal)
        if num_walls==0:
            print("The maze has no wall.")
        elif num_walls==1:
            print("The maze has walls that are all connected.")
        else:
            print(f"The maze has {num_walls} sets of walls that are all connected.")


        num_innerpoint=len(self.pointtotal)
        if num_innerpoint==0:
            print("The maze has no inaccessible inner point.")
        elif num_innerpoint==1:
            print("The maze has a unique inaccessible inner point.")
        else:
            print(f"The maze has {num_innerpoint} inaccessible inner points.")


        if self.num_area==0:
            print("The maze has no accessible area.")
        elif self.num_area==1:
            print("The maze has a unique accessible area.")
        else:
            print(f"The maze has {self.num_area} accessible areas.")


        num_cds = len(self.cdstotal)
        if num_cds==0:
            print(f"The maze has no accessible cul-de-sac.")
        elif num_cds==1:
            print(f"The maze has accessible cul-de-sacs that are all connected.")
        else:
            print(f"The maze has {num_cds} sets of accessible cul-de-sacs that are all connected.")


        if self.num_path == 0:
            print("The maze has no entry-exit path with no intersection not to cul-de-sacs.")
        elif self.num_path == 1:
            print("The maze has a unique entry-exit path with no intersection not to cul-de-sacs.")
        else:
            print(f"The maze has {self.num_path} entry-exit paths with no intersections not to cul-de-sacs.")
        # REPLACE PASS ABOVE WITH YOUR CODE

    def find_walls(self,i,j,wallList):                       #test if two blocks are connected by its value
        if 0<=i<len(self.wallsgrid) and 0<=j<len(self.wallsgrid[i]):
            wallList.append((i,j))
            for a,b in movelist:
                if 0<=i+a<len(self.wallsgrid) and 0<=j+b<len(self.wallsgrid[i]) and (i+a,j+b) not in wallList:
                    if a==1 and b==0:
                        if self.wallsgrid[i][j] in [2,3]:
                            if self.wallsgrid[i+a][j+b] in [1,2,3]:
                                Maze.find_walls(self,i+a,j+b,wallList)
                    if a==-1 and b==0:
                        if self.wallsgrid[i][j] in [1,2,3]:
                            if self.wallsgrid[i+a][j+b] in [2,3]:
                                Maze.find_walls(self,i + a, j + b, wallList)
                    if a==0 and b==1:
                        if self.wallsgrid[i][j] == 1:
                            if self.wallsgrid[i+a][j+b] in [1,2,3]:
                                Maze.find_walls(self,i + a, j + b, wallList)
                        if self.wallsgrid[i][j] == 3:
                            if self.wallsgrid[i+a][j+b] in [1,2,3]:
                                Maze.find_walls(self,i + a, j + b, wallList)
                    if a==0 and b==-1:
                        if self.wallsgrid[i][j] in [1,2,3]:
                            if self.wallsgrid[i+a][j+b] in [1,3]:
                                Maze.find_walls(self,i + a, j + b, wallList)
                    if a==1 and b==-1:
                        if self.wallsgrid[i][j] in [2,3]:
                            if self.wallsgrid[i+a][j+b] in [1,3]:
                                Maze.find_walls(self,i + a, j + b, wallList)
                    if a==-1 and b==1:
                        if self.wallsgrid[i][j] in [1,3]:
                            if self.wallsgrid[i+a][j+b] in [2,3]:
                                Maze.find_walls(self,i + a, j + b, wallList)
        else:
            return wallList

    def find_inner_point(self,i,j,pointlist):                                    #simply go from a point and no way back to see how far it can go and return all the path it goes
        if 0 <= i < len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            pointlist.append((i,j))
            for a,b in movelist2:
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in pointlist:
                    if a==1 and b==0:
                        if self.mazegrid[i][j] in [0,1,2,3]:
                            if self.mazegrid[i+a][j+b] in [0,2]:
                                Maze.find_inner_point(self,i+a,j+b,pointlist)
                    if a==-1 and b==0:
                        if self.mazegrid[i][j] in [0,2]:
                            if self.mazegrid[i+a][j+b] in [0,1,2,3]:
                                Maze.find_inner_point(self,i+a,j+b,pointlist)
                    if a==0 and b==1:
                        if self.mazegrid[i][j] in [0,1,2,3]:
                            if self.mazegrid[i + a][j + b] in [0, 1]:
                                Maze.find_inner_point(self, i + a, j + b, pointlist)
                    if a==0 and b==-1:
                        if self.mazegrid[i][j] in [0,1]:
                            if self.mazegrid[i+a][j+b] in [0,1,2,3]:
                                Maze.find_inner_point(self, i + a, j + b, pointlist)
        elif i==len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                pointlist.append((i, j))
                a = -1
                b = 0
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in pointlist:
                    if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                        Maze.find_inner_point(self, i + a, j + b, pointlist)
        elif 0 <= i < len(self.mazegrid)-1 and j== len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                pointlist.append((i, j))
                a = 0
                b = -1
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in pointlist:
                    if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                        Maze.find_inner_point(self, i + a, j + b, pointlist)
        else:
            return pointlist

    def find_cul_de_sacs2(self,i,j,pointlist,cdslist,gatelist):
        cango = 0
        if 0 <= i < len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            pointlist.append((i,j))
            for a,b in movelist2:
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in pointlist and (i + a, j + b) not in cdslist:
                    if a==1 and b==0:
                        if self.mazegrid[i][j] in [0,1,2,3]:
                            if self.mazegrid[i+a][j+b] in [0,2]:
                                cango += 1
                                Maze.find_cul_de_sacs2(self,i+a,j+b,pointlist,cdslist,gatelist)
                                Maze.find_cul_de_sacs2(self, i, j, pointlist, cdslist, gatelist)                #need to go through the function again to test if it is a cul_de_sac when its next point is cul_de_sac(returned by cdslist)
                    if a==-1 and b==0:
                        if self.mazegrid[i][j] in [0,2]:
                            if self.mazegrid[i+a][j+b] in [0,1,2,3]:
                                cango += 1
                                Maze.find_cul_de_sacs2(self,i+a,j+b,pointlist,cdslist,gatelist)
                                Maze.find_cul_de_sacs2(self, i, j, pointlist, cdslist, gatelist)
                    if a==0 and b==1:
                        if self.mazegrid[i][j] in [0,1,2,3]:
                            if self.mazegrid[i + a][j + b] in [0, 1]:
                                cango += 1
                                Maze.find_cul_de_sacs2(self,i+a,j+b,pointlist,cdslist,gatelist)
                                Maze.find_cul_de_sacs2(self, i, j, pointlist, cdslist, gatelist)
                    if a==0 and b==-1:
                        if self.mazegrid[i][j] in [0,1]:
                            if self.mazegrid[i+a][j+b] in [0,1,2,3]:
                                cango += 1
                                Maze.find_cul_de_sacs2(self,i+a,j+b,pointlist,cdslist,gatelist)
                                Maze.find_cul_de_sacs2(self, i, j, pointlist, cdslist, gatelist)
        elif i==len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                pointlist.append((i, j))
                a = -1
                b = 0
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in pointlist and (i + a, j + b) not in cdslist:
                    if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                        cango += 1
                        Maze.find_cul_de_sacs2(self,i+a,j+b,pointlist,cdslist,gatelist)
                        Maze.find_cul_de_sacs2(self, i, j, pointlist, cdslist, gatelist)
        elif 0 <= i < len(self.mazegrid)-1 and j== len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                pointlist.append((i, j))
                a = 0
                b = -1
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in pointlist and (i + a, j + b) not in cdslist:
                    if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                        cango += 1
                        Maze.find_cul_de_sacs2(self,i+a,j+b,pointlist,cdslist,gatelist)
                        Maze.find_cul_de_sacs2(self, i, j, pointlist, cdslist, gatelist)
        if cango==0:
            if Maze.find_cango(self,i,j,cdslist,gatelist)==1:
                if i!=len(self.mazegrid)-1:
                    cdslist.append((i,j))
            return cdslist

    def find_cango(self,i,j,cdslist,gatelist):            #find all possible dirctions a point can go not into a cul_de_sac or way back(used in find cul_de_sacs)
        cango = 0
        if (i,j) in gatelist:
            cango+=1
            if (i,j)==(0,0):
                cango += 1
        if 0 <= i < len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            for a,b in movelist2:
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in cdslist:
                    if a==1 and b==0:
                        if self.mazegrid[i][j] in [0,1,2,3]:
                            if self.mazegrid[i+a][j+b] in [0,2]:
                                cango += 1
                    if a==-1 and b==0:
                        if self.mazegrid[i][j] in [0,2]:
                            if self.mazegrid[i+a][j+b] in [0,1,2,3]:
                                cango += 1
                    if a==0 and b==1:
                        if self.mazegrid[i][j] in [0,1,2,3]:
                            if self.mazegrid[i + a][j + b] in [0, 1]:
                                cango += 1
                    if a==0 and b==-1:
                        if self.mazegrid[i][j] in [0,1]:
                            if self.mazegrid[i+a][j+b] in [0,1,2,3]:
                                cango += 1
        elif i==len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                a = -1
                b = 0
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in cdslist:
                    if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                        cango += 1
        elif 0 <= i < len(self.mazegrid)-1 and j== len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                a = 0
                b = -1
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in cdslist:
                    if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                        cango += 1
        return cango

    def find_nextpoint(self,i,j,nextlist):          #used to test if all nextpoint is in cdslist when test cul_de_sacs found are in the same area
        if 0 <= i < len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            for a,b in movelist2:
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]):
                    if a==1 and b==0:
                        if self.mazegrid[i][j] in [0,1,2,3]:
                            if self.mazegrid[i+a][j+b] in [0,2]:
                                nextlist.append((i+a,j+b))
                    if a==-1 and b==0:
                        if self.mazegrid[i][j] in [0,2]:
                            if self.mazegrid[i+a][j+b] in [0,1,2,3]:
                                nextlist.append((i+a,j+b))
                    if a==0 and b==1:
                        if self.mazegrid[i][j] in [0,1,2,3]:
                            if self.mazegrid[i + a][j + b] in [0, 1]:
                                nextlist.append((i+a,j+b))
                    if a==0 and b==-1:
                        if self.mazegrid[i][j] in [0,1]:
                            if self.mazegrid[i+a][j+b] in [0,1,2,3]:
                                nextlist.append((i+a,j+b))
        elif i==len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                a = -1
                b = 0
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]):
                    if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                        nextlist.append((i+a,j+b))
        elif 0 <= i < len(self.mazegrid)-1 and j== len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                a = 0
                b = -1
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]):
                    if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                        nextlist.append((i+a,j+b))
        return nextlist

    def find_path(self,i,j,pointlist,cdstotallist):
        if 0 <= i < len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            pointlist.append((i,j))
            for a,b in movelist2:
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in pointlist:
                    if (i + a, j + b) not in cdstotallist:         #make sure the path will not contain cul_de_sacs
                        if a == 1 and b == 0:
                            if self.mazegrid[i][j] in [0, 1, 2, 3]:
                                if self.mazegrid[i + a][j + b] in [0, 2]:
                                    Maze.find_path(self, i + a, j + b, pointlist,cdstotallist)
                        if a == -1 and b == 0:
                            if self.mazegrid[i][j] in [0, 2]:
                                if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                                    Maze.find_path(self, i + a, j + b, pointlist,cdstotallist)
                        if a == 0 and b == 1:
                            if self.mazegrid[i][j] in [0, 1, 2, 3]:
                                if self.mazegrid[i + a][j + b] in [0, 1]:
                                    Maze.find_path(self, i + a, j + b, pointlist,cdstotallist)
                        if a == 0 and b == -1:
                            if self.mazegrid[i][j] in [0, 1]:
                                if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                                    Maze.find_path(self, i + a, j + b, pointlist,cdstotallist)
        elif i==len(self.mazegrid)-1 and 0 <= j < len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                pointlist.append((i, j))
                a = -1
                b = 0
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in pointlist:
                    if (i + a, j + b) not in cdstotallist:
                        if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                            Maze.find_path(self, i + a, j + b, pointlist,cdstotallist)
        elif 0 <= i < len(self.mazegrid)-1 and j== len(self.mazegrid[i])-1:
            if self.mazegrid[i][j] == 0:
                pointlist.append((i, j))
                a = 0
                b = -1
                if 0 <= i + a < len(self.mazegrid) and 0 <= j + b < len(self.mazegrid[i]) and (i + a, j + b) not in pointlist:
                    if (i + a, j + b) not in cdstotallist:
                        if self.mazegrid[i + a][j + b] in [0, 1, 2, 3]:
                            Maze.find_path(self, i + a, j + b, pointlist,cdstotallist)
        else:
            return pointlist

    def find_pillar(self,i,j):
        movelist3 = [(-1, 0), (0, -1)]
        ispillar = 0
        if 0 < i < len(self.mazegrid) and 0 <= j < len(self.mazegrid[i]):
            for a,b in movelist3:
                if a==-1 and b==0:
                    if self.mazegrid[i+a][j+b] in [0,1]:
                        ispillar+=1
                if a==0 and b==-1:
                    if self.mazegrid[i+a][j+b] in [0,2]:
                        ispillar+=1
        elif i==0:
            if (i,j)==(0,0):
                ispillar=2
            else:
                if self.mazegrid[i][j-1] in [0,2]:
                    ispillar=2
        return ispillar


    def display(self):
        texname=self.filename[:-3]
        with open(f'{texname}tex', 'w') as f:
            f.write('\\documentclass[10pt]{article}\n'
                    '\\usepackage{tikz}\n'
                    '\\usetikzlibrary{shapes.misc}\n'
                    '\\usepackage[margin=0cm]{geometry}\n'
                    '\\pagestyle{empty}\n'
                    '\\tikzstyle{every node}=[cross out, draw, red]\n'
                    '\n'
                    '\\begin{document}\n'
                    '\n'
                    '\\vspace*{\\fill}\n'
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n'
                    '% Walls\n')
            wallleft=[]
            wallright=[]                                                                        #draw horizontal walls
            for i in range(len(self.mazegrid)):
                for j in range(len(self.mazegrid[i])):
                    if self.mazegrid[i][j] in [1,3]:                                            #walls only be drew horizontally when its 1,3
                        wallleft.append(j)                                                      #use pathleft[0] to keep the leftest coordinate of continuous line
                        wallright.append(j + 1)                                                 #use pathright[-1] to keep the rightest coordinate of continuous line
                        if j<len(self.mazegrid[i])-1:
                            if self.mazegrid[i][j+1] not in [1,3]:
                                f.write(f'    \\draw ({wallleft[0]},{i}) -- ({wallright[-1]},{i});\n')
                                wallleft=[]
                                wallright=[]
            wallup=[]
            wallbelow=[]                                                                        #draw vertical walls
            for j in range(len(self.mazegrid[0])):                                              #same as horizontal walls
                for i in range(len(self.mazegrid)):
                    if self.mazegrid[i][j] in [2,3]:
                        wallup.append(i)
                        wallbelow.append(i+1)
                        if i<len(self.mazegrid)-1:
                            if self.mazegrid[i+1][j] not in [2,3]:
                                f.write(f'    \\draw ({j},{wallup[0]}) -- ({j},{wallbelow[-1]});\n')
                                wallup=[]
                                wallbelow=[]

            f.write('% Pillars\n')                                                                  #go through pillar list and print
            for (i,j) in self.pillar:
                f.write(f'    \\fill[green] ({j},{i}) circle(0.2);\n')

            f.write('% Inner points in accessible cul-de-sacs\n')                                   #just go through cul_de_sacs list and print
            for i in range(len(self.mazegrid)):
                for j in range(len(self.mazegrid[i])):
                    if (i,j) in self.cdstotallist:
                        f.write(f'    \\node at ({j+0.5},{i+0.5}) {{}};\n')

            f.write('% Entry-exit paths without intersections\n')
            pathleft=[]
            pathright=[]                                                                            #draw horizontal path
            for i in range(len(self.mazegrid)-1):                                                   #same as drawing vertical line
                for j in range(len(self.mazegrid[i])):
                    if (i,j) in self.pathtotal:
                        if j==0 and self.mazegrid[i][j] in [0,1]:
                            pathleft.append(-1)
                            pathright.append(j)
                        if j<len(self.mazegrid[i])-1:
                            pathleft.append(j)
                            if (i,j+1) in self.pathtotal and self.mazegrid[i][j+1] in [0,1]:
                                pathright.append(j+1)
                                if j+1==len(self.mazegrid[i])-1:
                                    f.write(f'    \\draw[dashed, yellow] ({pathleft[0] + 0.5},{i + 0.5}) -- ({pathright[-1] + 0.5},{i + 0.5});\n')
                                    pathleft = []
                                    pathright = []
                            elif (i,j+1) not in self.pathtotal or self.mazegrid[i][j+1] not in [0,1]:
                                if pathright:
                                    f.write(f'    \\draw[dashed, yellow] ({pathleft[0]+0.5},{i+0.5}) -- ({pathright[-1]+0.5},{i+0.5});\n')
                                    pathleft=[]
                                    pathright=[]
                                else:
                                    pathleft = []
                                    pathright = []
            pathup = []
            pathbelow = []                                                                          #draw vertical path
            for j in range(len(self.mazegrid[0])):
                for i in range(len(self.mazegrid)):
                    if (i,j) in self.pathtotal:
                        if i == 0 and self.mazegrid[i][j] in [0, 2]:                                #if its first line,start with -0.5(-1+0.5),path only can go up or down when up or below block is  0,2
                            pathup.append(-1)
                            pathbelow.append(i)
                        if i < len(self.mazegrid) - 1:
                            pathup.append(i)                                                        #keep the up coordinate of path needed to be drew in pathleft everytime
                            if (i+1,j) in self.pathtotal and self.mazegrid[i+1][j] in [0,2]:        #if next block is path and its 0,2,add into pathright,keep the lowest coordinate of the line that draw in one time
                                pathbelow.append(i+1)
                                if i+1==len(self.mazegrid)-1:                                       #if reaches the boundary,must draw the line if the line continues to the boundary
                                    f.write(f'    \\draw[dashed, yellow] ({j+0.5},{pathup[0] + 0.5}) -- ({j + 0.5},{pathbelow[-1] + 0.5});\n')
                                    pathup = []
                                    pathbelow = []
                            elif (i+1,j) not in self.pathtotal or self.mazegrid[i+1][j] not in [0,2] :    #if next block not a path,draw the line start with uppest coordinate already keep in pathleft[0] and lowest coordinate keep in pathright[-1]
                                if pathbelow:
                                    f.write(f'    \\draw[dashed, yellow] ({j+0.5},{pathup[0] + 0.5}) -- ({j + 0.5},{pathbelow[-1] + 0.5});\n')
                                    pathup = []
                                    pathbelow = []
                                else:
                                    pathup = []
                                    pathbelow = []
            f.write('\\end{tikzpicture}\n'
                    '\\end{center}\n'
                    '\\vspace*{\\fill}\n'
                    '\n'
                    '\\end{document}\n')
        # REPLACE PASS ABOVE WITH YOUR CODE