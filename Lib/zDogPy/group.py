'''Group'''

from functools import cmp_to_key
from zDogPy.anchor import Anchor, shapeSorter

class Group(Anchor):

    updateSort = False
    visible = True

    # ------
    # update
    # ------

    def updateSortValue(self):
        sortValueTotal = 0
        self.checkFlatGraph()
        for item in self.flatGraph:
            item.updateSortValue()
        sortValueTotal += item.sortValue

        # average sort value of all points
        # def not geometrically correct, but works for me
        self.sortValue = sortValueTotal / len(self.flatGraph)

        if self.updateSort:
            self.flatGraph.sort(key=cmp_to_key(shapeSorter))

    # ------
    # render
    # ------

    def render(self, ctx, renderer):
        if not self.visible:
            return
        self.checkFlatGraph()
        for item in self.flatGraph:
            item.render(ctx, renderer)

    def getFlatGraph(self):
        # do not include children, group handles rendering & sorting internally
        return [self]

    def updateFlatGraph(self):
        # get flat graph only used for group
        # do not include in parent flatGraphs

        # print(self.children)

        # do not include self
        flatGraph = []
        for child in self.children:
            childFlatGraph = child.getFlatGraph()
            flatGraph += childFlatGraph

        self.flatGraph = flatGraph
