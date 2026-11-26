from UnionFind import UnionFind

def test_init():
    test = UnionFind([1, 2, 3, 4])
    assert test.parent == [0, 1, 2, 3]
    assert test.size == [1, 1, 1, 1]

    test = UnionFind(3)
    assert test.parent == [0, 1, 2]
    assert test.size == [1, 1, 1]

def test_merge():

    union = UnionFind(8)
    union.merge(0, 1)
    assert union.size[0] == 2
    assert union.parent[1] == 0

    union.merge(0, 7)

    assert union.size[0] == 3
    assert union.parent[0] == 0
    assert union.parent[7] == 0

    union.merge(1, 7)
    assert union.parent[1] == 0
    assert union.parent[7] == 0
    assert union.size[0] == 3
    assert union.size[1] == 1
    assert union.size[7] == 1

    union.size[3] = 4
    union.merge(1, 3)
    assert union.parent[1] == 3
    assert union.parent[0] == 3
    assert union.size[3] == 7

def test_find():
    union = UnionFind(5)
    union.parent = [0, 0, 1, 2, 3]

    assert union.find(4) == 0
    assert union.parent == [0, 0, 0, 0, 0]

