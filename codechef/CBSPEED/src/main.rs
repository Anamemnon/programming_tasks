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

    let (a, b) = read_tuple!(buffer, (u8, u8));
    println!("{}", if a < b { "YES" } else { "NO"})
}
