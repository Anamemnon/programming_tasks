fn main() {
    println!("Hello, world!");
}

struct Solution;

impl Solution {
    pub fn create_target_array(nums: Vec<i32>, index: Vec<i32>) -> Vec<i32> {
        let mut array = Vec::new();

        nums.iter()
            .zip(index.iter())
            .for_each(|(n, i)| array.insert(*i as usize, *n));

        array
    }
}