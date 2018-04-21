from collections import deque
import distance

def distance_function(str1,str2):
    return distance.levenshtein(str1,str2)

class BKTree(object):
    def __init__(self, items_list=[], items_dict={}):
        self.tree = None

        _add = self.add
        for item in items_list:
            _add(item)

        for item in items_dict:
            _add(item)

    def add(self, item):
        node = self.tree
        if node is None:
            self.tree = (item, {})
            return

        while True:
            parent, children = node
            distance = distance_function(item, parent)
            node = children.get(distance)
            if node is None:
                children[distance] = (item, {})
                break

    def find(self, item, n):
        if self.tree is None:
            return []

        candidates = deque([self.tree])
        found = []

        while candidates:
            candidate, children = candidates.popleft()
            distance = distance_function(candidate, item)
            if distance <= n:
                found.append((distance, candidate))

            if children:
                lower = distance - n
                upper = distance + n
                candidates.extend(c for d, c in children.items() if lower <= d <= upper)

        found.sort()
        return found

    def __iter__(self):
        if self.tree is None:
            return

        candidates = deque([self.tree])

        while candidates:
            candidate, children = candidates.popleft()
            yield candidate
            candidates.extend(children.values())
