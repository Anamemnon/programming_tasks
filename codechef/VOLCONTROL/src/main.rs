use std::io;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Error reading");

    let n = n.trim().parse::<u8>().expect("Error parsing 'n'");

    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Error reading 'input'");
        let arr: Vec<i8> = input.split_whitespace().map(|x| x.parse().unwrap()).collect();
        println!("{}", (arr[0] - arr[1]).abs());
    }
}
