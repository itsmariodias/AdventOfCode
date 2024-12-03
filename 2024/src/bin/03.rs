use anyhow::*;
use aoc_2024::*;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use regex::Regex;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::result::Result::Ok;

const DAY: &str = "03";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const TEST: &str = "\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
";

const TEST_2: &str = "\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
";

fn parse_keywords(input: &str) -> HashMap<String, bool> {
    let mut result = HashMap::new();

    // Split the input string by "do()" and "don't()"
    for part in input.split("do()") {
        if let Some((key, rest)) = part.split_once("don't()") {
            // This part will either return 2 values if there is a don't() delimiter to split by, if not it returns None and goes to else statement
            if !key.trim().is_empty() {
                result.insert(key.trim().to_string(), true); // Add the `do()` part as true
            }
            if !rest.trim().is_empty() {
                result.insert(rest.trim().to_string(), false); // Add the `don't()` part as false
            }
        } else if !part.trim().is_empty() {
            // logic goes to this part of code when there is no don't() keyword, so the part is do() by default.
            result.insert(part.trim().to_string(), true); // Handle trailing `do()` parts
        }
    }

    result
}

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<i32> {
        let re: Regex = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
        let mut total = 0;

        for line in reader.lines() {
            if let Ok(line) = line {
                for captures in re.captures_iter(&line) {
                    let first_number = captures.get(1).unwrap().as_str().parse::<i32>().unwrap();
                    let second_number = captures.get(2).unwrap().as_str().parse::<i32>().unwrap();

                    total += first_number * second_number;
                }
            }
        }
        Ok(total)
    }

    assert_eq!(161, part1(BufReader::new(TEST.as_bytes()))?);

    let input_file: BufReader<File> = BufReader::new(File::open(INPUT_FILE)?);
    let result: i32 = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<i32> {
        let re: Regex = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
        let mut total = 0;

        let mut input: String = "".to_string();
        for line in reader.lines() {
            // Read all lines and combine into a single string
            if let Ok(line) = line {
                input.push_str(&line);
            }
        }
        let parsed = parse_keywords(&input); // split out each chunk of string and assign bool based on if it appears after do() or don't()

        for (part, do_flag) in &parsed {
            if *do_flag {
                // Only perform for chunks after do() and before don't()
                for captures in re.captures_iter(&part) {
                    let first_number = captures.get(1).unwrap().as_str().parse::<i32>().unwrap();
                    let second_number = captures.get(2).unwrap().as_str().parse::<i32>().unwrap();

                    total += first_number * second_number;
                }
            }
        }
        Ok(total)
    }

    assert_eq!(48, part2(BufReader::new(TEST_2.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result: i32 = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}
