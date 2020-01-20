from queue import PriorityQueue
GRAPH = {\
            'S': {'A': 1, 'G': 12},\
            'A': {'S': 1, 'C': 1,'B': 3},\
            'B': {'A': 3, 'D': 3},\
            'C': {'A': 1, 'D': 1, 'G': 2},\
            'D': {'B': 3, 'C': 1, 'G': 3},\
            'G': {'S': 12, 'C': 2, 'D': 3},\
          
        }

heuristic_G = {\
                        'S': 4,\
                        'A': 2,\
                        'B': 6,\
                        'C': 2,\
                        'D': 3,\
                        'G': 0\
             
                    }
def main():
    print('ENTER FIRST NODE :', end=' ')
    first_node = input().strip()
    goal_node = 'G'
    if first_node not in GRAPH:
        print('ERROR: NODE IS NOT FOUND.')
    else:
        print('INITIALIZATION:  [',first_node,',',heuristic_G[first_node],']')
        fn, cost, optimal_path,j = a_star(first_node, goal_node)
        print('ITERATION',j,'GIVES THE FINAL OUTPUT AS', optimal_path)

def a_star(first_node,goal_node):    
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((heuristic_G[first_node], 0, first_node, [first_node]))
    visited[first_node] = heuristic_G[first_node]
    j=0
    i=0
    while not priority_queue.empty():
        if(i==1):
            count=0
            print('ITERATION',j,':',end='')
            while True:
                if count==priority_queue.qsize():
                    print('')
                    break
                else:
                    print('   ',priority_queue.queue[count][3],priority_queue.queue[count][0],end='')
                    count=count+1
        j=j+1
        i=0
        (fn, cost, vertex, path) = priority_queue.get()
        if vertex == goal_node:
            return fn, cost, path, j 
        for next_node in GRAPH[vertex].keys():
            i=1
            gn = cost + GRAPH[vertex][next_node]
            fn = gn + heuristic_G[next_node]
            if not next_node in visited or visited[next_node] >= fn:
                visited[next_node] = fn
                priority_queue.put((fn, gn, next_node, path + [next_node]))

if __name__ == '__main__':
    main()