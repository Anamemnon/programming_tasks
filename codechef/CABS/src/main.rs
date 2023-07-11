use std::io;
use std::cmp::Ordering;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Error reading");

    let n = n.trim().parse::<u8>().unwrap();

    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let arr: Vec<u8> = input.split_whitespace().map(|x| x.parse::<u8>().unwrap()).collect();

        let answer = match arr[0].cmp(&arr[1]) {
            Ordering::Less => {"FIRST".to_string()}
            Ordering::Equal => {"ANY".to_string()}
            Ordering::Greater => {"SECOND".to_string()}
        };
        println!("{}", answer);
    }
}
