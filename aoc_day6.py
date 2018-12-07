import datetime
import sys
from string import ascii_lowercase

input = """249, 60
150, 332
174, 83
287, 329
102, 338
111, 201
259, 96
277, 161
143, 288
202, 311
335, 55
239, 148
137, 224
48, 214
186, 87
282, 334
147, 157
246, 191
241, 181
286, 129
270, 287
79, 119
189, 263
324, 280
316, 279
221, 236
327, 174
141, 82
238, 317
64, 264
226, 151
110, 110
336, 194
235, 333
237, 55
230, 137
267, 44
258, 134
223, 42
202, 76
159, 135
229, 238
197, 83
173, 286
123, 90
314, 165
140, 338
347, 60
108, 76
268, 329"""

input3 = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

input2 = input.split('\n')


print(len(input2))
matrix = [[0] * 350 for _ in range(350)]

coord_set = set(input2)

counter = 1
for line in input2:
    coordinates = line.split(',')
    matrix[int(coordinates[1])][int(coordinates[0])] = counter
    counter += 1

#print(matrix)
the_amount = 0
for row_index in range(len(matrix)):
    for col_index in range(len(matrix)):
        total_dist = 0
        for line in input2:
            coordinates = line.split(',')
            dist = abs((int(coordinates[1])) - row_index) + abs((int(coordinates[0])) - col_index)
            total_dist += dist

        if total_dist < 10000:
            the_amount += 1

#print(matrix)
print(input2)
print(the_amount)

visited_set = set()
for line in input2:
    coordinates = line.split(',')

    dist = abs(int(coordinates[1]) - row_index) + abs(int(coordinates[0]) - col_index)

amount = {}
invalid = set()
for index in range(counter):
    is_invalid = False
    if index != 0:
        amount[index] = 0
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix)):
                if is_invalid == False:
                    if matrix[row_index][col_index] == index:
                        amount[index] += 1
                        if row_index == 0 or row_index == (len(matrix)-1) or col_index == 0 or col_index == (len(matrix)-1):
                            amount[index] = -1
                            is_invalid = True
#print(amount)

#print(matrix)
