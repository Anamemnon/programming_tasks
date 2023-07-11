const SQUATS_IN_SET: u8 = 15;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("read error");
    let n: u32 = input.trim().parse().expect("parse error");

    for _ in 0..n {
        input.clear();
        std::io::stdin().read_line(&mut input).expect("read error");
        let number: u32 = input.trim().parse().expect("parse error");
        println!("{}", number * SQUATS_IN_SET as u32);
    };
}