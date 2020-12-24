from datetime import datetime, timedelta

class Node:
    def __init__(self, key):
        schedTime, duration, nameOfJob = key.split(",")
        rawSchedTime = datetime.strptime(schedTime, '%H:%M')
        key = rawSchedTime.time()
        endTime = (rawSchedTime + timedelta(minutes=int(duration))).time()
        self.data = key
        self.scheduledEnd = endTime
        self.duration = duration
        self.nameOfJob = nameOfJob.rstrip()
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return f"Time: {self.data}, Duration: {self.duration}, End: {self.scheduledEnd}, Jobname: {self.nameOfJob}"

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
            self.helpfulPrint(key, True)
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data > curr.data and key.data >= curr.scheduledEnd:
            if curr.rchild == None:
                curr.rchild = key
                self.helpfulPrint(key, True)
            else:
                self._insert(curr.rchild, key)
        elif key.data < curr.data and key.scheduledEnd <= curr.data:
            if curr.lchild == None:
                curr.lchild = key
                self.helpfulPrint(key, True)
            else:
                self._insert(curr.lchild, key)
        else:
            self.helpfulPrint(key, False)

    def helpfulPrint(self, key, succeeded):
        if succeeded:
            print(f'Added:\t\t {key.nameOfJob}')
            print(f'Begin:\t\t {key.data}')
            print(f'End:\t\t {key.scheduledEnd}')
            print('-'*60)
        else:
            print(f'Rejected:\t\t {key.nameOfJob}')
            print(f'Begin:\t\t {key.data}')
            print(f'End:\t\t {key.scheduledEnd}')
            print('Reason:\t Time slot overlap, please verify')
            print('-'*60)

    def inOrder(self):
        print("Full job schedule for today")
        print("-"*60)
        self._inOrder(self.root)
        print("-"*60)

    def _inOrder(self, curr):
        if curr:
            self._inOrder(curr.lchild)
            print(curr)
            self._inOrder(curr.rchild)

    def length(self):
        return self._length(self.root)

    def _length(self, curr):
        if curr is None:
            return 0
        return 1 + self._length(curr.lchild) + self._length(curr.rchild)

    def findVal(self, key):
        return self._findVal(self.root, key)

    def _findVal(self, curr, key):
        if curr:
            if key == curr.data:
                return curr
            elif key < curr.data:
                return self._findVal(curr.lchild, key)
            else:
                return self._findVal(curr.rchild, key)
        return

    def minRSubtree(self, curr):
        if curr.lchild == None:
            return curr
        else:
            return self.minRSubtree(curr.lchild)

    def deleteVal(self, key):
        self._deleteVal(self.root, None, None, key)

    def _deleteVal(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.lchild and curr.rchild:
                    min_child = self.minRSubtree(curr.rchild)
                    curr.data = min_child.data
                    self._deleteVal(curr.rchild, curr, False, min_child.data)
                elif curr.lchild == None and curr.rchild == None:
                    if prev:
                        if is_left:
                            prev.lchild = None
                        else:
                            prev.rchild = None
                    else:
                        self.root = None
                elif curr.lchild == None:
                    if prev:
                        if is_left:
                            prev.lchild = curr.rchild
                        else:
                            prev.rchild = curr.rchild
                    else:
                        self.root = curr.rchild
                else:
                    if prev:
                        if is_left:
                            prev.lchild = curr.lchild
                        else:
                            prev.rchild = curr.lchild
                    else:
                        self.root = curr.lchild
            elif key < curr.data:
                self._deleteVal(curr.lchild, curr, True, key)
            elif key > curr.data:
                self._deleteVal(curr.rchild, curr, False, key)
        else:
            print(f"{key} not found in Tree")
