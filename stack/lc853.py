def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pos_dict = {}
    for i in range(len(position)):
        pos_dict[position[i]] = i
    position.sort()
    solu = []
    for i in range(len(position)-1, -1, -1):
        print(solu)
        time = (target - position[i])/speed[pos_dict[position[i]]]
        print("position:", position[i], ",speed:", speed[pos_dict[position[i]]], ",time:", time)
        if len(solu) == 0 or solu[len(solu)-1]<time:
            solu.append(time)
    return len(solu)

print(carFleet(target = 100, position = [0,2,4], speed = [4,2,1]))