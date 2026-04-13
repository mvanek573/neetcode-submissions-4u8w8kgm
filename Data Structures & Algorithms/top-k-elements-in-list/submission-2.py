class Solution:
    def topKFrequent(self, nums, k):
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num]+=1
        output = []
        for i in range(k):
            x = max(counts.values())
            remove = []
            for key in counts:
                if counts[key] == x:
                    output.append(key)
                    remove.append(key)
                    break
            for key in remove:
                counts.pop(key)
        return output
