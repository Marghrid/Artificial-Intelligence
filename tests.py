from time import *
from board import *
tests = [
		[[1,2,1,2,1],[2,1,2,1,2],[1,2,1,2,1],[2,1,2,1,2]],
		[[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]],
		[[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[5,1,1,3],[4,5,1,2]],
		[[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]],
		[[1,1,5,3],[5,3,5,3],[1,2,5,4],[5,2,1,4],[5,3,5,1],[5,3,4,4],[5,5,2,5],[1,1,3,1],[1,2,1,3],[3,3,5,5]]
];

i = 0
for test in tests:
	i+=1
	print("test ", end="")
	print(i, end="")
	print(":", end="")
	print()
	print_board(test)
	print()

	print("DFS1:")
	problem = InstrumentedProblem(same_game(test))
	initial_time = perf_counter()
	depth_first_tree_search(problem)
	final_time = perf_counter() - initial_time
	print("time: ", end="")
	print(final_time)
	print("Estados expandidos: ", end="")
	print(problem.succs)
	print("Nós gerados: ", end = "")
	print(problem.states)
	print()

	print("DFS2:")
	problem = InstrumentedProblem(same_game(test))
	initial_time = perf_counter()
	depth_first_graph_search(problem)
	final_time = perf_counter() - initial_time
	print("time: ", end="")
	print(final_time)
	print("Nós expandidos: ", end="")
	print(problem.succs)
	print("Nós gerados: ", end = "")
	print(problem.states)
	print()

	print("Greedy search:")
	problem = InstrumentedProblem(same_game(test))
	initial_time = perf_counter()
	greedy_best_first_graph_search(problem, problem.h)
	final_time = perf_counter() - initial_time
	print("time: ", end="")
	print(final_time)
	print("Estados expandidos: ", end="")
	print(problem.succs)
	print("Nós gerados: ", end = "")
	print(problem.states)
	print()

	print("A*:")
	problem = InstrumentedProblem(same_game(test))
	initial_time = perf_counter()
	astar_search(problem)
	final_time = perf_counter() - initial_time
	print("time: ", end="")
	print(final_time)
	print("Estados expandidos: ", end="")
	print(problem.succs)
	print("Nós gerados: ", end = "")
	print(problem.states)
	print()
