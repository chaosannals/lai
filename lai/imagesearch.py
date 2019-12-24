import os
import pickle
import imagehash
import numpy
from PIL import Image
from vptree import VPTree


def dhash(path):
    '''
    图片哈希
    '''
    path = os.path.abspath(path)
    image = Image.open(path)
    h = imagehash.dhash(image)
    i = int(str(h), 16)
    return int(numpy.array(i, dtype="float64"))


def dhamming(a, b):
    '''
    汉明距离
    '''
    d = bin(int(a) ^ int(b))
    return d.count('1')


def plist(folder):
    '''
    列举文件夹内的所有文件
    '''
    result = []
    dirname = os.path.abspath(folder)
    for i in os.listdir(dirname):
        path = os.path.abspath(dirname + '/' + i)
        if os.path.isdir(path):
            result.extend(plist(path))
        else:
            result.append(path)
    return result


class IndexManager:
    '''
    索引管理器
    '''

    def __init__(self):
        self.hashes = {}
        self.vptree = {}

    def query(self, path, max_distance=64):
        '''
        查询
        '''
        imageHash = dhash(path)
        nodes = sorted(self.vptree.get_all_in_range(imageHash, max_distance))
        results = []
        for (d, h) in nodes:
            images = self.hashes.get(h, [])
            results.append((1 - (d / 64), images))
        return results

    def index(self, folder):
        '''
        载入图片库
        '''
        images = plist(folder)
        count = len(images)
        for i, path in enumerate(images):
            print('[加载] {}/{} - {}'.format(i + 1, count, path))
            h = dhash(path)
            l = self.hashes.get(h, [])
            l.append(path)
            self.hashes[h] = l
        points = list(self.hashes.keys())
        self.vptree = VPTree(points, dhamming)

    def save_vptree(self, path):
        '''
        保存 VPTREE
        '''
        with open(path, 'wb') as writer:
            data = pickle.dumps(self.vptree)
            writer.write(data)

    def save_hashes(self, path):
        '''
        保存 哈希
        '''
        with open(path, 'wb') as writer:
            data = pickle.dumps(self.hashes)
            writer.write(data)

    def load_vptree(self, path):
        '''
        加载 VPTREE
        '''
        with open(path, 'rb') as reader:
            data = reader.read()
            self.vptree = pickle.loads(data)

    def load_hashes(self, path):
        '''
        加载 哈希
        '''
        with open(path, 'rb') as reader:
            data = reader.read()
            self.hashes = pickle.loads(data)
