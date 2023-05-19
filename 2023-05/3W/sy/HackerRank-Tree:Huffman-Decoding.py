import queue as Queue

cntr = 0


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
stack = []
data = {}


def decoding(root):
    current_node = root

    if current_node.data == '\0':
        stack.append(0)
        decoding(current_node.left)
        stack.pop()
        stack.append(1)
        decoding(current_node.right)
        stack.pop()
    else:
        data[''.join(str(e) for e in stack)] = current_node.data


def decodeHuff(root, s):
    answer = ''
    decoding(root)
    cache = []

    for i in range(0, len(s)):
        cache.append(s[i])
        if ''.join(str(e) for e in cache) in data.keys():
            answer += data[''.join(str(e) for e in cache)]
            cache = []
    print(answer)


ip = input()