fn main() {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).unwrap();
    let n = buffer.trim().parse().unwrap();

    for _ in 0..n {
        buffer.clear();
        std::io::stdin().read_line(&mut buffer).unwrap();
        let arr: Vec<u8> = buffer.split_whitespace().map(|x| x.parse().unwrap()).collect();
        let s = Solution::new(arr[0], arr[1]);
        println!("{}", s.biryani());
    }
}

struct Solution {
    weeks: u8,
    cost: u8,
}

impl Solution {
    fn new(weeks:  u8, cost: u8) -> Solution {
        Solution { weeks, cost }
    }

    fn biryani(&self) -> u16 {
        (self.weeks * self.cost) as u16
    }
}