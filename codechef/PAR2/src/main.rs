fn main() {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).unwrap();
    let n: u8 = buffer.trim().parse().unwrap();

    for _ in 0..n {
        buffer.clear();
        std::io::stdin().read_line(&mut buffer).unwrap();
        let a: u8 = buffer.trim().parse().unwrap();
        println!("{}", if a % 2 == 0 {"Yes"} else {"No"});
    }
}
