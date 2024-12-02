pub fn start_day(day: &str) {
    println!("Advent of Code 2024 - Day {:0>2}", day);
}

pub fn create_subsets<T: Clone>(list: &[T]) -> Vec<Vec<T>> {
    list.iter()
        .enumerate()
        .map(|(index, _)| {
            list.iter()
                .enumerate()
                .filter_map(|(j, item)| if index != j { Some(item.clone()) } else { None })
                .collect()
        })
        .collect()
}

// Additional common functions

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        start_day("00");
    }
}
