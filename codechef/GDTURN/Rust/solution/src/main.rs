use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let t: u8 = input.trim().parse().unwrap();

    for _ in 0..t {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let arr = input.split_whitespace()
            .map(|c| c.parse::<u8>().unwrap()).collect::<Vec<u8>>();

        if arr[0] + arr[1] > 6 {
            println!("YES");
        } else {
            println!("NO");
        }
    }
}


