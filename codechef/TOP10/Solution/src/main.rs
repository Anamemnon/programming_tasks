fn main() {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).unwrap();

    let n = buffer.trim().parse::<u8>().unwrap();

    for _ in 0..n {
        buffer.clear();
        std::io::stdin().read_line(&mut buffer).unwrap();

        let x = buffer.trim().parse::<u8>().unwrap();
        println!("{}", if x >= 1 && x <= 10 {"YES"} else {"NO"});
    }
}
