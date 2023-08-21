def rotateString(s, goal):
    return True if (len(s) == len(goal)) and goal in s+s else False

if __name__=="__main__":
    s = "abcde"
    goal = "abced"

    print(rotateString(s,goal))