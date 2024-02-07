def main():
    nandm = input().split()
    missions = int(nandm[0])
    agents = int(nandm[1])
    vals = input().split()
    vals = [-1*int(i) for i in vals]
    vals.sort()
    total = 0
    multiplyer = 1
    agent_count = 0
    for mission in range(missions):
        total+=vals[mission]*multiplyer
        agent_count += 1
        if agent_count == agents:
            multiplyer += 1
            agent_count = 0
    print(-1*total)
main()
    



