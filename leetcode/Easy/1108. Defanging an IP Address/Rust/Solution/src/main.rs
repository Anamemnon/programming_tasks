fn main() {
    println!("Hello, world!");
}

struct Solution;

impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        address.replace(".", "[.]")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_defang_i_paddr() {
        assert_eq!(Solution::defang_i_paddr("1.1.1.1".to_string()), "1[.]1[.]1[.]1")
    }
}