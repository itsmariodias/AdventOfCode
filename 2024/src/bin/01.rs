use anyhow::*;
use aoc_2024::*;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use counter::Counter;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::result::Result::Ok;

const DAY: &str = "01";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const TEST: &str = "\
3   4
4   3
2   5
1   3
3   9
3   3
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<i32> {
        let mut left_list: Vec<i32> = Vec::new();
        let mut right_list: Vec<i32> = Vec::new();

        for line in reader.lines() {
            if let Ok(line) = line {
                let nums: Vec<i32> = line
                    .split_whitespace() // Split the line by whitespace
                    .filter_map(|s: &str| s.parse::<i32>().ok()) // Parse each part into i32
                    .collect();
                if nums.len() == 2 {
                    left_list.push(nums[0]);
                    right_list.push(nums[1]);
                }
            }
        }

        left_list.sort();
        right_list.sort();

        let mut total: i32 = 0;

        for (idx, _item) in left_list.iter().enumerate() {
            total += (left_list[idx] - right_list[idx]).abs()
        }
        Ok(total)
    }

    assert_eq!(11, part1(BufReader::new(TEST.as_bytes()))?);

    let input_file: BufReader<File> = BufReader::new(File::open(INPUT_FILE)?);
    let result: i32 = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let mut left_list: Vec<usize> = Vec::new();
        let mut right_list: Vec<usize> = Vec::new();

        for line in reader.lines() {
            if let Ok(line) = line {
                let nums: Vec<usize> = line
                    .split_whitespace() // Split the line by whitespace
                    .filter_map(|s: &str| s.parse::<usize>().ok()) // Parse each part into usize
                    .collect();
                if nums.len() == 2 {
                    left_list.push(nums[0]);
                    right_list.push(nums[1]);
                }
            }
        }

        let right_counter: Counter<usize> = right_list.into_iter().collect::<Counter<_>>();

        let mut total: usize = 0;

        for item in left_list {
            total += item * right_counter[&item];
        }
        Ok(total)
    }

    assert_eq!(31, part2(BufReader::new(TEST.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}
