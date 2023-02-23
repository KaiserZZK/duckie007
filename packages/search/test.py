adjacency_matrix = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: [7],
        7: []
    }

next = [((5, 4), 'South', 1), ((4, 5), 'West', 1)]

# next[1][2] +=2
# print(next[1])

# for ma in adjacency_matrix[2]:
#     print(ma)

myDict = {(1,1): (2,3)}

# print(myDict[(1,1)])
#
# for successor in next:
#     print(successor[0])
#     print(successor[3] + 'heh')

umbers = [999,1,4,5,66]
print(sorted(umbers)[0])