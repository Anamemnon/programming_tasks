fn main() {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Error reading");
    let n: u16 = buffer.trim().parse::<u16>().expect("Error parsing");

    for _ in 0..n {
        buffer.clear();
        std::io::stdin().read_line(&mut buffer).expect("Error reading");
        let vec: Vec<u8> = buffer.split_whitespace().map(|c| c.parse::<u8>().expect("Error parsing")).collect();

        println!("{}", if vec[2] >= vec[0] && vec[2] < vec[1] {"YES"} else {"NO"});
    }
}
