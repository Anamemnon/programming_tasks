macro_rules! read_tuple {
    ( $line: ident, ($($t: ty),*)) => {{
        let mut ws = $line.trim().split_whitespace();
        (
            $(ws.next().unwrap().parse::<$t>().unwrap(),)*
        )
    }}
}

fn main() {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).unwrap();
    let n: u16 = buffer.trim().parse().unwrap();

    for _ in 0..n {
        buffer.clear();
        std::io::stdin().read_line(&mut buffer).unwrap();
        let (a, b) = read_tuple!(buffer, (u16, u16));
        println!("{}", a*7 - b);
    }
}