"""
matrix operations for :
x,y to array index
characters

"""

# ----------------------------------------------------
# characters
"""
file for converting characters to matrixs
"""
char_offset = [
    [0, 11],
    [3, 11],
    [8, 11],
    [12, 11],
    [0, 0],
    [4, 0],
    [8, 5],
    [12, 5],
]

char_dict = {
    0: [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
    ],
    1: [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ],
    2: [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
    ],
    3: [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
    ],
    4: [
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
    ],
    5: [
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
    ],
    6: [
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ],
    7: [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
    ],
    8: [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ],
    9: [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
    ],
}


class Char_Setting:
    def __init__(self, offset):
        self.offset = offset
        self.character = 0

    def char_matrix(self, character):
        char_matrix = char_dict[character]
        cx = []

        for i, row in enumerate(char_matrix):
            for j, b in enumerate(row):
                if b == 1:
                    x = self.offset[0] + j
                    y = self.offset[1] + (4 - i)
                    cx.append([x, y])

        return cx
    
def char_matrix(character, offset):
    char_matrix = char_dict[character]
    cx = []

    for i, row in enumerate(char_matrix):
        for j, b in enumerate(row):
            if b == 1:
                x = offset[0] + j
                y = offset[1] + (4 - i)
                cx.append([x, y])

    return cx


characters = [Char_Setting(cs) for cs in char_offset]
# ------------------------------------------------------

# ------------------------------------------------------
led_matrix = [
    [255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240],
    [224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239],
    [223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 210, 209, 208],
    [192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207],
    [191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176],
    [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175],
    [159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144],
    [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143],
    [127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112],
    [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],
    [95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],
    [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
    [63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48],
    [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
    [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
]


def xy_mat(x, y):
    row = led_matrix[-y - 1]
    val = row[x]
    return val


def mat_xy(val):
    for i, row in enumerate(led_matrix):
        if val in row:
            x = row.index(val)
            y = len(row) - i
            return x, y


# ------------------------------------------------------
