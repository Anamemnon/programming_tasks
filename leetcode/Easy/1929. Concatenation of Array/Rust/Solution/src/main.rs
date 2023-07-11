fn main() {
}

struct Solution;

impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        nums.repeat(2)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_concatenation() {
        assert_eq!(Solution::get_concatenation(vec![1, 2, 3]), vec![1, 2, 3, 1, 2, 3])
    }
}