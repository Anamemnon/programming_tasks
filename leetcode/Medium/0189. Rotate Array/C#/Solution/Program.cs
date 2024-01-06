public class Solution
{
    public static void Rotate(int[] nums, int k)
    {
        var r = k % nums.Length;
        var start = nums[..(nums.Length - r)];
        var end = nums[(nums.Length - r)..];

        int i = 0;

        foreach ( var v in end) nums[i++] = v;
        foreach ( var v in start) nums[i++] = v;
    }
}