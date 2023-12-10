class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        return max(d.keys(), key=lambda x: d[x])


if __name__ == "__main__":
    sol = Solution()
    l1 = [2,2,1,1,1,2,2]
    l2 = [0,0,1]
    print(sol.majorityElement(l1))    # 2
    print(sol.majorityElement(l2))    # 0