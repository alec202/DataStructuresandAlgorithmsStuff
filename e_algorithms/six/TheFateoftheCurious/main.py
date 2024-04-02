import itertools
def how_many_agents():
    n, k = input().split()
    n = int(n)
    k = int(k)

    all_skills = set(input().split())
    
    agents = []
    for i in range(n):
        n = int(input())
        skills = set(input().split())
        ##check for and remove subsets:
        flag = False
        for agent in agents:
            if skills.issubset(agent):
                flag = True
            if agent.issubset(skills):
                agents.remove(agent)
                flag = False
        if not flag:
            agents.append(skills)
    ##now all agents are in the list
    for i in range(1, len(agents)+1):
        combins = itertools.combinations(agents, i)
        for com in combins:
            found_skills = set()
            for group in com:
                for skill in group:     
                    found_skills.add(skill)
            if found_skills == all_skills:
                return(i)
    ##print(agents)
print(how_many_agents())




##  here are some websites i used. all for syntax/library tool documentation
##
##https://www.educative.io/answers/how-to-join-two-or-more-sets-in-python
##
##https://docs.python.org/3/library/itertools.html
##
##https://www.geeksforgeeks.org/set-add-python/
##
##
