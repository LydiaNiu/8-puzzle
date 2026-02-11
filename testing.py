def get_blank_position(state):
    return state.index(0) # find the index of the blank tile (0) in the current state


s1 = [1,2,3,4,5,6,0,7,8]
s2 = [1,2,3,0,4,5,7,6,8]
s3 = [0,1,2,5,3,6,4,7,8]

print(get_blank_position(s1) )# should return 6
print(get_blank_position(s2) )# should return 3
print(get_blank_position(s3) )# should return 0