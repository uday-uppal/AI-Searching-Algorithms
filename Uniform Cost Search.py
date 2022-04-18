uday_graph=[]
def uday_uniform_cost_search(uday_goal, uday_start):
	global uday_graph,uday_cost
	uday_answer = []
	uday_queue = []
	for i in range(len(uday_goal)):
		uday_answer.append(10**8)
	uday_queue.append([0, uday_start])
	uday_visited = {}
	count = 0
	while (len(uday_queue) > 0):
		uday_queue = sorted(uday_queue)
		p = uday_queue[-1]
		del uday_queue[-1]
		p[0] *= -1
		if (p[1] in uday_goal):
			index = uday_goal.index(p[1])
			if (uday_answer[index] == 10**8):
				count += 1
			if (uday_answer[index] > p[0]):
				uday_answer[index] = p[0]
			del uday_queue[-1]
			uday_queue = sorted(uday_queue)
			if (count == len(uday_goal)):
				return uday_answer
		if (p[1] not in uday_visited):
			for i in range(len(uday_graph[p[1]])):
				uday_queue.append( [(p[0] + uday_cost[(p[1], uday_graph[p[1]][i])])* -1, uday_graph[p[1]][i]])
		uday_visited[p[1]] = 1
	return uday_answer
if __name__ == '__main__':    
    uday_cost={}
    uday_graph=[[] for i in range(5)]
    # uday_graph=uday_graph+[]
    uday_graph[0].append(1)
    uday_graph[0].append(3)
    uday_graph[1].append(0)
    uday_graph[1].append(4)
    uday_graph[1].append(2)
    uday_graph[2].append(1)
    uday_graph[2].append(3)
    uday_graph[3].append(0)
    uday_graph[3].append(2)
    uday_graph[3].append(4)
    uday_graph[4].append(1)
    uday_graph[4].append(3)
    uday_cost[(0, 1)]=uday_cost[( 1,0)] = 1
    uday_cost[(0, 3)]=uday_cost[( 3,0)] = 10
    uday_cost[(1, 4)] =uday_cost[(4,1)]= 5
    uday_cost[(3, 4)] =uday_cost[(4,3)]= 5
    uday_cost[(1, 2)] =uday_cost[(2,1)]= 15
    uday_cost[(2, 3)] =uday_cost[(3,2)]= 5
    uday_goal = []
    uday_goal.append(2)
    uday_answer = uday_uniform_cost_search(uday_goal, 0)
    print("Minimum uday_cost from 0 to 2 is = ",uday_answer[0])
