if __name__ == '__main__':
    version1,version2 = map(lambda x:x.split("."),input().split())
    version1 = list(map(int,version1))
    version2 = list(map(int,version2))
    length = len(version1) if len(version1) < len(version2) else len(version2)
    for i in range(length):
        if version1[i] == version2[i]:
            continue
        elif version1[i] < version2[i]:
            print(-1)
            break
        elif version1[i] > version2[i]:
            print(1)
            break
    else:
        if len(version1) < len(version2):
            print(-1)
        elif len(version1) > len(version1):
            print(1)
        else:
            print(0)