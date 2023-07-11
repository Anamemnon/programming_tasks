fn main() {
    println!("Hello, world!");
}

impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        let c = Celsius {value: celsius};

        vec![
            Kelvin::from(c).value,
            Fahrenheit::from(c).value,
        ]
    }
}


struct Kelvin {
    value: f64,
}

struct Fahrenheit {
    value: f64,
}

#[derive(Clone, Copy)]
struct Celsius {
    value: f64,
}

impl From<Celsius> for Kelvin {
    fn from(c: Celsius) -> Self {
        Kelvin { value: Celsius {value: c.value + 273.15}.value }
    }
}

impl From<Celsius> for Fahrenheit {
    fn from(c: Celsius) -> Self {
        Fahrenheit { value: Celsius {value:c.value * 1.80 + 32.00}.value }
    }
}
