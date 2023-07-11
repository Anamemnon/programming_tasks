fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();

    let n = input.trim().parse::<u16>().unwrap();

    for _ in 0..n {
        input.clear();
        std::io::stdin().read_line(&mut input).unwrap();
        let arr: Vec<u16> = input.trim().split_whitespace().map(|s| s.parse::<u16>().unwrap()).collect();
        println!("{}", arr[0]*5 + arr[1]*7);
    }
}

