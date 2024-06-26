import itertools

##right now it works but with strings and not binary. that is my next task
def how_many_agents():
    n, k = input().split()
    n = int(n)
    k = int(k)

    all_skills = set(input().split())
    
    agents = []
    for i in range(n):
        q = input()
        skills = set(input().split())
        if len(skills) == k:
            return(1)
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
    for i in range(2, len(agents)):
        combins = itertools.combinations(agents, i)
        for com in combins:
            found_skills = set()
            for group in com:
                for skill in group:     
                    found_skills.add(skill)
            if len(found_skills) == k:
                return(i)
    return(n)
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
