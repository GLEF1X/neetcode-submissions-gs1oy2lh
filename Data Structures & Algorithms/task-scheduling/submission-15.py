class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldownTable = [0] * 26
        priorityQueue = []

        for task in tasks:
            cooldownTable[ord(task) - ord('A')] += 1
        
        for idx, occurences in enumerate(cooldownTable):
            if occurences <= 0:
                continue
            heapq.heappush(priorityQueue, (-occurences, chr(idx + ord('A'))))
        
        clock = 0
        cooldownTable = [0] * 26
        pendingTasks = []
        cooldownQueue = deque()
        
        while priorityQueue:
            priority, task = heapq.heappop(priorityQueue)
            priority = abs(priority)
            # TODO: priority is negative, so apply abs
            taskIdxInCoolDownTable = ord(task) - ord('A')
            coolDownStopClockTime = cooldownTable[taskIdxInCoolDownTable]
            # print(task, priority)
            if coolDownStopClockTime <= clock:
                # increasing the priority because it's negative in python min heap
                if priority - 1 > 0:
                    # we're not supposed to push here because it's on a cooldown
                    cooldownQueue.append((-(priority - 1), task))
                clock += 1
                cooldownTable[taskIdxInCoolDownTable] = clock + n
                while cooldownQueue:
                    # attempt to execute a cooldown task
                    task = cooldownQueue.popleft()
                    # print("attempt cooldown: ", task, cooldownTable[ord(task[1]) - ord('A')], clock)
                    cooldownStopAt = cooldownTable[ord(task[1]) - ord('A')]
                    if cooldownStopAt <= clock:
                        heapq.heappush(priorityQueue, task)
                        break
                    else:
                        if not priorityQueue:
                            cooldownQueue.appendleft(task)
                            clock = cooldownStopAt 
                            continue
                        cooldownQueue.appendleft(task)
                        break
        
        return clock

# 3 A 0 0
# 2 A 4 1 - eliminate, it's on cooldown
# 1 B 0 1
# 2 A 4 2 - eliminate, it's on cooldown
# 1 C 0 2
# 2 A 4 3 - eliminate, it's on cooldown
# 2 A 4 4
# 1 A 8 5
# 1 A 8 6
# 1 A 8 7
# 1 A 8 8
