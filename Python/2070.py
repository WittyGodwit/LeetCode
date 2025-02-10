class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        answer = []
        record = {}
        items.sort(key=lambda x:(x[0], x[1]))
        max_beauty = []
        current_max = 0
        for price, beauty in items:
            current_max = max(current_max, beauty)
            max_beauty.append((price, current_max))
        for query in queries:
            if query in record:
                answer.append(record[query])
                continue
            left, right = 0, len(items) - 1
            while left <= right:
                mid = (left + right) // 2
                if items[mid][0] > query:
                    right = mid - 1
                else:
                    left = mid + 1
            if right >= 0:
                maximum = max_beauty[right][1]
            else:
                maximum = 0
            record[query] = maximum
            answer.append(maximum)
        return max_beauty