def randomGraphGenerator():
    import networkx as nx
    import random

    # Create the complete graph

    # Generate a random graph with 100 nodes and edge probability p=0.5

    random_graph = nx.gnp_random_graph(random.randint(10, 50), 0.3)

    # Print the number of nodes and edges in the random graph
    # print("Number of nodes:", random_graph.number_of_nodes())
    # print("Number of edges:", random_graph.number_of_edges())

    # Convert the graph to a dictionary format
    graph_dict = nx.to_dict_of_dicts(random_graph)

    # Print the dictionary
    # print(graph_dict)

    output_graph = {}
    # x = set()
    # print(type(x))

    for vertex in graph_dict:
        output_graph[vertex] = (set(graph_dict[vertex].keys())) if len(graph_dict[vertex]) != 0 else {}
        # for key in graph:
        #     output_graph[graph] = key
    return output_graph

print(randomGraphGenerator())