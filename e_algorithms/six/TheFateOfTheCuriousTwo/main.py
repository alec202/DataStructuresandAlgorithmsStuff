import time
import heapq
start_time = time.time()

def union_sets(com):
    final = set()
    for group in com:
        final.update(group)
    return final

def how_many_agents():
    n, k = map(int, input().split())

    heaped_agents = []
    agents = []
    for _ in range(n):
        num_skills_possessed = int(input())
        skills = list(map(int, input().split()))
        data_on_skills = [-num_skills_possessed, _]
        data_on_skills.append(skills)
        # listForHeap = [num_skills_possessed]
        # listForHeap += skills
        # listForHeap.append(_)
        heapq.heappush(heaped_agents, data_on_skills)

        # # Check for and remove subsets
        # flag = False
        # for agent in heaped_agents:
        #     if skills.issubset(agent):
        #         flag = True
        #     if agent.issubset(skills):
        #         agents.remove(agent)
        #         flag = False
        # if not flag:
        #     agents.append(skills)

    # Now all agents are in the list
    covered_skills = []
    indices_picked = []
    num_agents = 0
    while len(covered_skills) < k:
        if time.time() - start_time >= 9:
            return num_agents, indices_picked
        item_picked = (heapq.heappop(heaped_agents))
        skills_picked = item_picked.pop()
        indices_picked.append(item_picked.pop())
        covered_skills += skills_picked
        num_agents += 1
    return num_agents, indices_picked


    # max_len = max(len(agent) for agent in agents)
    # for i in range(k // max_len, len(agents)):
    #     if time.time() - start_time >= 8:
    #     combinations = itertools.combinations(agents, i)
    #     for com in combinations:
    #         if time.time() - start_time >= 8:
    #             found_skills = union_sets(com)
    #             if len(found_skills) == k:
    #                 selected_agents = [index + 1 for index, agent in enumerate(agents) if agent in com]
    #                 return i, selected_agents
    #
    # return n, [i + 1 for i in range(n)]  # Return all agents if no suitable combination found

# Call the function and print the results
num_agents, selected_agents = how_many_agents()
print(num_agents)
print(*selected_agents)

# 3 5
# 2
# 1 3
# 3
# 0 1 2
# 3
# 0 2 4