class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.data)
        if self.right is not None:
            self.right.print()

    def FindMax(self):
        if self is not None:
            data = self.data
            if self.left is not None:
                left = self.left.FindMax()
            if self.right is not None:
                right = self.right.FindMax()
            if left > right:
                max = left
            else:
                max = right
            if data > max:
                max = data
            return max
        

            
data = Node(100)
data.insert(200)
data.insert(50)
data.insert(10)
data.insert(40)
data.insert(30)
data.insert(20)
data.insert(60)
data.insert(70)
data.insert(300)
data.insert(400)
data.insert(950)
data.insert(43)
data.print()
max = data.FindMax()
print(max)