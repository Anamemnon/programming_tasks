fn main() {
    println!("Hello, world!");
}

struct Solution;

impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        let mut max_char = '0';
        for ch in n.chars() {
            if ch > max_char {
                max_char = ch;
            }
            if max_char == '9' {
                return 9;
            }
        }
        return (max_char.to_digit(10).unwrap() - '0'.to_digit(10).unwrap()) as i32;
    }
}