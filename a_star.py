import heapq
import math
import show_gui

cost_of_origin = 0
diagonal_move = True

def heuristic(start, dest): #估計 a 到 dest 的代價
    return abs(start[0] - dest[0]) + abs(start[1] - dest[1]) 


def find_path(frame_class, graph, origin_coor, dest_coor):
    if graph == {} or graph == None: #如果 graph 是空時, 終止function
        return None
    
    open_list = [] #按照成本排列的優先序列
    closed_set = set() #到訪過的地點
    heapq.heappush(open_list, (cost_of_origin, origin_coor))

    count = 0
    while open_list: #當 open list 不是空時, 做...
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == dest_coor: #如果 current node 是終點
            path = []
            while current_node: #當 current node 不是空時, 做...
                path.append(current_node)
                current_node = graph[current_node][1]
            return path[::-1] #反轉 array, 因為 while loop 中是由終點到起點的路線

        if current_node in closed_set: #如果 current node 是到訪過的地點
            continue #跳過這一次的 loop

        closed_set.add(current_node) #記錄為到訪過的地點

        for neighbor, cost in graph[current_node][0].items(): #neighbor 是旁邊的地點
            if neighbor in closed_set: #如果 neighbor 是到訪過的地點
                continue #跳過這一次的 loop

            #總成本 = 現在已用的成本 + 到這個 neighbor 的成本 + 估計到 dest 的成本
            total_cost = current_cost+cost + heuristic(neighbor, dest_coor)

            input("press enter:")
            show_gui.show_run(frame_class, {"x":neighbor[0],"y":neighbor[1]}, count)
            print("current_node", current_node)
            print("neighbor", neighbor)
            print("current_cost", current_cost)
            print("total_cost", total_cost,"\n")
            
            heapq.heappush(open_list, (total_cost, neighbor)) 
            graph[neighbor][1] = current_node
        count+=1
    return None


def spawn_graph(frame_class):
    if frame_class.start != None and frame_class.dest != None:
        graph = {}

        for row_index, row_data in enumerate(frame_class.board):
            for column_index, column_data in enumerate(frame_class.board[row_index]):
                node_dict = {}
                direction = None
                if diagonal_move:
                    direction = ["U", "UR", "R", "DR", "D", "DL", "L", "UL"]
                else:
                    direction = ["U", "R", "D", "L"]

                if column_data != 1: #if current node is not a block
                    for current_dir in direction:
                        if current_dir == "U":
                            if row_index > 0: #check current row is it at the boundary
                                if frame_class.board[row_index -1][column_index] == 0: #if target node is a normal node
                                    node_dict[(column_index, row_index - 1)] = 1

                        elif current_dir == "UR":
                            if (row_index > 0) and (column_index < len(row_data) - 1): #check current row is it at the boundary
                                if frame_class.board[row_index -1][column_index +1] == 0: #if target node is a normal node
                                    node_dict[(column_index +1, row_index -1)] = 1

                        elif current_dir == "R":
                            if (column_index < len(row_data) - 1): #check current row is it at the boundary
                                if frame_class.board[row_index][column_index +1] == 0: #if target node is a normal node
                                    node_dict[(column_index +1, row_index)] = 1

                        elif current_dir == "DR":
                            if (row_index < len(frame_class.board) -1) and (column_index < len(row_data) - 1): #check current row is it at the boundary
                                if frame_class.board[row_index +1][column_index +1] == 0: #if target node is a normal node
                                    node_dict[(column_index +1, row_index +1)] = 1

                        elif current_dir == "D":
                            if (row_index < len(frame_class.board) -1): #check current row is it at the boundary
                                if frame_class.board[row_index +1][column_index] == 0: #if target node is a normal node
                                    node_dict[(column_index, row_index +1)] = 1

                        elif current_dir == "DL":
                            if (row_index < len(frame_class.board) -1) and (column_index > 0): #check current row is it at the boundary
                                if frame_class.board[row_index +1][column_index -1] == 0: #if target node is a normal node
                                    node_dict[(column_index -1, row_index +1)] = 1

                        elif current_dir == "L":
                            if (column_index > 0): #check current row is it at the boundary
                                if frame_class.board[row_index][column_index -1] == 0: #if target node is a normal node
                                    node_dict[(column_index -1, row_index)] = 1

                        elif current_dir == "UL":
                            if (row_index > 0) and (column_index > 0): #check current row is it at the boundary
                                if frame_class.board[row_index -1][column_index -1] == 0: #if target node is a normal node
                                    node_dict[(column_index -1, row_index -1)] = 1

                graph[(column_index, row_index)] = [node_dict, None]

        return graph
