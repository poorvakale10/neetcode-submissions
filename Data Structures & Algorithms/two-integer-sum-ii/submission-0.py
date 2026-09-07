class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            needed = target - numbers[i]

            if needed in seen:
                return [seen[needed], i + 1]
            else:
                seen[numbers[i]] = i + 1