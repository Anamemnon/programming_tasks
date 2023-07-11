fn main() {
    println!("Hello, world!");
}

struct Solution;

impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut  v = Vec::with_capacity(nums.len());
        for i in 0..nums.len() {
            v.push(nums[nums[i] as usize]);
        }
        v
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_build_array() {
        assert_eq!(Solution::build_array(vec![0,2,1,5,3,4]), vec![0,1,2,4,5,3])
    }
}