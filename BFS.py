#create a graph using dictionaries and lists
graph = {'A':['B','C','E'],
'B':['A','D','E'],
'C':['A','F','G'],
'D':['B','E'],
'E':['A','B','D'],
'F':['C'],
'G':['C']}

#visits all the nodes of graph (connected component using graphs)
def bfs_connected_component(graph, start):
    #keep track of all explored nodes
    explored = []
    #keep track of nodes to be checked
    queue = [start]
    #keep looping until all the nodes checked

    while queue:
        #pop the shallowest node (first node) from the queue
        node = queue.pop(0)
        if node not in explored:
            #add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            #add neighbours of node to the queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

def bfs_shortest_path(graph,start,goal):
    #keep track of explored nodes
    explored = []
    #keep track of all the paths to be checked
    queue = [[start]]

    #return path if the start is goal
    if start == goal:
        return "That was easy! Start=Goal"
    
    #keeps looping until all the possible path have been checked
    while queue:
        #pop the first path from the queue
        path = queue.pop(0)
        #get the last node from the past
        node = path[-1]
        if node not in explored:
            neightbours = graph[node]
            #go through all neighbour nodes, contruct path and push it to the queue
            for neightbour in neightbours:
                new_path = list(path)
                new_path.append(neightbour)
                queue.append(new_path)
                #return if neighbour is the goal
                if neightbour == goal:
                    return new_path
            #mark node as explored
            explored.append(node)
    #if there is no path between nodes
    return "So sorry, But the path doesn't exist :("


print("BFS: ",bfs_connected_component(graph,'A'))
print("Shortest Path: ",bfs_shortest_path(graph,'A','G'))