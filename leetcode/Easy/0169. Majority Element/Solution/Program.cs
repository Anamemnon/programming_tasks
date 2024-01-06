_ = Solution.MajorityElement(new int[] { 3, 2, 3 });

public class Solution
{
    public static int MajorityElement(int[] nums)
    {
        if (nums.Length == 1) return nums[0];

        Dictionary<int, int> counter = new();

        for (int i = 0; i < nums.Length; i++)
        {
            var temp = nums[i];

            if (counter.ContainsKey(temp))
            {
                counter[temp]++;

                if (i + 1 > nums.Length / 2 && counter[temp] > nums.Length / 2) return temp;
            }
            else counter[temp] = 1;
        }
        return 0;
    }
}