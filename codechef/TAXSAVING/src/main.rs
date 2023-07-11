use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let t: u8 = input.trim().parse().unwrap();

    for _ in 0..t {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();

        let v = input
            .trim()
            .split_ascii_whitespace()
            .map(|x|x.parse().unwrap())
            .collect::<Vec<u8>>();

        println!("{}", v[0] - v[1]);
    }
}
