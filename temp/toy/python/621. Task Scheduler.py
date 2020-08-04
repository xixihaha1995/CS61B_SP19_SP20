class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length < 1: return length
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        task_sort = sorted(task_map.items(), key = lambda x: -x[1])
        maxCount = task_sort[0][1]
        res = (maxCount - 1) * (n+1)
        for other in task_sort:
            if other[1] == maxCount:
                res += 1
        return res if res > length else length