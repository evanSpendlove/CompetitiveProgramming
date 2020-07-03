/*
  LeetCode - Problem 1480, Running Sum of 1D Array
*/

class L1480_RunningSum {
    public int[] runningSum(int[] nums) {
        int[] runningSum = new int[nums.length];
        int sum = 0;
        
        for(int i = 0; i < nums.length; i++) {
            sum += nums[i];
            runningSum[i] = sum;
        }
        
        return runningSum;
    }
}

/*
  C++ Solution
  class Solution {
    public:
        vector<int> runningSum(vector<int>& nums) {
            for(int i = 1; i < nums.size(); i++) {
                nums[i] += nums[i-1];
            }

            return nums;
        }
  };
*/

/*
  Python Solution

  class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1
        while i < len(nums):
            nums[i] += nums[i - 1]
            i += 1
        return nums
*/