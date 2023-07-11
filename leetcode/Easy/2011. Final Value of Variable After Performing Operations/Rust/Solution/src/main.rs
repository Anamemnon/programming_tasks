fn main() {
    println!("Hello, world!");
}

struct Solution;

impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut answ = 0;

        for v in operations {
            match v.as_str() {
                "++X" | "X++" => answ += 1,
                "--X" | "X--" => answ -= 1,
                _ => ()
            };
        };

        answ
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_final_value_after_operations() {
        assert_eq!(
            Solution::final_value_after_operations(
                vec!["--X".to_string(), "X++".to_string(),"X++".to_string()]), 1)
    }
}