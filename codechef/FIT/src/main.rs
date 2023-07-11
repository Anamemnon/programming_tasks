use std::fmt::{Display, Formatter};

fn main() {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).unwrap();
    let n: u8 = buffer.trim().parse().unwrap();

    for _ in 0..n {
        buffer.clear();
        std::io::stdin().read_line(&mut buffer).unwrap();
        let km = Kilometer(buffer.trim().parse().unwrap());
        println!("{}", Solution::solve(km));
    }

}

struct Solution;

impl Solution {
    pub fn solve(km: Kilometer) -> Kilometer{
        Kilometer(km.0 * 5 * 2)
    }
}

struct Kilometer(u8);

impl Display for Kilometer {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.0)
    }
}


