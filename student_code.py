import math

def shortest_path(M, start, goal):
    """
    :param M: map object, contains two properties, "roads" and "intersections". "Intersections" is a dictionary that
    contains coordinates of each node in graph. "Roads" is a list  where, if i is an intersection, roads[i] contains
    a list of the intersections that intersection i connects to.
    :param start: integer, identifies the start node
    :param goal: integer, identifies the end node
    :return: a list of integers identifying the shortest sequence of nodes to reach the goal form the start.
    """
    print("shortest path called")

    # 1. To calculate heuristic I can calculate the straight line distance between start and goal intersection,
    # based on their coordinates: math.sqrt( (goal.x - start.x)**2 + (start.y - goal.y)**2 )
    # 2. Frontier - a priority queue of nodes to explore. Initially it contains start node. In later steps, it is filled with
    # previously explored node children, that weren't yet explored
    # 3. Keep a list of nodes already explored. At the end of the algorithm, this will be the reusult path
    # 4. At each step, check the cost of travel to node in frontier. This is total cost from the start + heuristic

    frontier = HeapSort()
    frontier.insert(start, 0)




def heuristic(intersections, start, goal):
    """ Calculate Euclidean distance between two intersections """
    startx = intersections[start][0]
    starty = intersections[start][1]
    goalx = intersections[goal][0]
    goaly = intersections[goal][1]
    return math.sqrt((goalx - startx)**2 + (starty - goaly)**2)


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class HeapSort:
    """ Class helping with sorting the frontier """
    # TODO check if heap works ok
    def __init__(self):
        self.heap_list = []

    def insert(self, value, priority):
        self.heap_list.append(Node(value, priority))
        self.heapify(self.heap_list[-1])

    # def create_heap(self):
    #     for index in range(len(self.heap_list), -1, -1):
    #         self.heapify(index)

    def heapify(self, index):
        left_child_index = 2 * index
        right_child_index = 2 * index + 1
        smallest = index

        if left_child_index < len(self.heap_list) and \
                self.heap_list[left_child_index].priority < self.heap_list[smallest].priority:
            smallest = left_child_index

        if right_child_index < len(self.heap_list) and \
                self.heap_list[right_child_index].priority < self.heap_list[smallest].priority:
            smallest = right_child_index

        if smallest != index:
            temp = self.heap_list[index]
            self.heap_list[index] = self.heap_list[smallest]
            self.heap_list[smallest] = temp
            self.heapify(smallest)

    def remove_smallest(self):
        if self.size() > 1:
            removed = self.heap_list.pop(0)
            self.heap_list.insert(0, self.heap_list.pop(-1))
            self.heapify(0)
            return removed
        elif self.size() == 1:
            return self.heap_list.pop()
        return -1

    def size(self):
        return len(self.heap_list)


if __name__ == "__main__":
    test_list1 = [1, 2, 3, 4, 5]
    heapSort = HeapSort(test_list1)
    print(heapSort.heap_list)
    print(heapSort.remove_smallest())
    print(heapSort.heap_list)
    print(heapSort.remove_smallest())
    print(heapSort.heap_list)
    print()

    test_list2 = [3, 1, 6, 2, 7]
    heapSort2 = HeapSort(test_list2)
    print(heapSort2.heap_list)
    print(heapSort2.remove_smallest())
    print(heapSort2.heap_list)
    print(heapSort2.remove_smallest())
    print(heapSort2.heap_list)
    print(heapSort2.remove_smallest())
    print(heapSort2.heap_list)
    print(heapSort2.remove_smallest())
    print(heapSort2.heap_list)
    print()

    test_list3 = [1]
    heapSort3 = HeapSort(test_list3)
    print(heapSort3.remove_smallest())
    print(heapSort3.heap_list)
    print(heapSort3.remove_smallest())
    print(heapSort3.heap_list)

    print(heuristic({0: [2, 2], 1: [3, 3]}, 0, 1))
    print(heuristic({0: [3, 3], 1: [2, 2]}, 0, 1))
