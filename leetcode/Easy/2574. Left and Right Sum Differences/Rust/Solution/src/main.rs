fn main() {
    println!("Hello, world!");
}

struct Solution;

impl Solution {
    pub fn left_rigth_difference(mut nums: Vec<i32>) -> Vec<i32> {
        let mut left = 0;
        let mut right: i32 = nums.iter().sum();
        let mut buf = 0;

        nums
            .iter_mut()
            .for_each(|i| {
                right -= *i;
                left += buf;
                buf = *i;
                *i = (left - right).abs();
            });

        nums
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_left_rigth_difference() {
        assert_eq!(Solution::left_rigth_difference(vec![10,4,8,3]), vec![15, 1, 11, 22]);
    }
}