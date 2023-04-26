# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def func(state):
    result =state[6]-state[13]+0.3*sum(state[0:6])-0.3*sum(state[7:13])
    if(state[0]<6):
        result+=state[0]*0.2
    if (state[1] < 5):
        result += state[1] * 0.2
    if (state[2] < 4):
        result += state[2] * 0.2
    if (state[3] < 3):
        result += state[3] * 0.2
    if (state[4] < 2):
        result += state[4] * 0.2

    if (state[7] < 6):
        result -= state[7] * 0.2
    if (state[8] < 5):
        result -= state[8] * 0.2
    if (state[9] < 4):
        result -= state[9] * 0.2
    if (state[10] < 3):
        result -= state[10] * 0.2
    if (state[11] < 2):
        result -= state[11] * 0.2

    if (state[0] == 6):
        result += 0.5
    if (state[1] == 5):
        result += 0.5
    if (state[2] == 4):
        result += 0.6
    if (state[3] == 3):
        result += 0.5
    if (state[4] == 2):
        result += 0.5
    if (state[5] == 1):
        result += 0.5

    if (state[7] == 6):
        result -= 0.5
    if (state[8] == 5):
        result -= 0.5
    if (state[9] == 4):
        result -= 0.5
    if (state[10] == 3):
        result -= 0.5
    if (state[11] == 2):
        result -= 0.5
    if (state[12] == 1):
        result -= 0.5







    return result


