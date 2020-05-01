from collections import deque

for _ in range(int(input())):
    queue_len = int(input())
    queue_list = deque(map(int, input().split()))
    
    status = "Yes"
    for cube in sorted(queue_list, reverse=True):
        if queue_list[-1] == cube:
            queue_list.pop()
        elif queue_list[0] == cube:
            queue_list.popleft()
        else:
            status = "No"
            break
    
    print(status)