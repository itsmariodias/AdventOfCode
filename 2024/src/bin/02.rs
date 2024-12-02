use anyhow::*;
use aoc_2024::*;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::result::Result::Ok;

const DAY: &str = "02";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const TEST: &str = "\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<i32> {
        let mut total_safe: i32 = 0;

        for line in reader.lines() {
            if let Ok(line) = line {
                let levels: Vec<i32> = line
                    .split_whitespace() // Split the line by whitespace
                    .filter_map(|s: &str| s.parse::<i32>().ok()) // Parse each part into i32
                    .collect();

                let length = levels.len() - 1;

                if levels.len() > 1 {
                    let first = levels[0];
                    let second = levels[1];
                    let diff = second - first;
                    let order;

                    if 1 <= diff && diff <= 3 {
                        order = 1;
                    } else if -3 <= diff && diff <= -1 {
                        order = -1;
                    } else {
                        continue;
                    }

                    let mut flag = true;
                    for i in 1..length {
                        let diff = levels[i + 1] - levels[i];
                        if !(order == 1 && 1 <= diff && diff <= 3)
                            && !(order == -1 && -3 <= diff && diff <= -1)
                        {
                            flag = false;
                            break;
                        }
                    }
                    if flag {
                        total_safe += 1;
                    }
                }
            }
        }

        Ok(total_safe)
    }

    assert_eq!(2, part1(BufReader::new(TEST.as_bytes()))?);

    let input_file: BufReader<File> = BufReader::new(File::open(INPUT_FILE)?);
    let result: i32 = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<i32> {
        let mut total_safe: i32 = 0;

        for line in reader.lines() {
            if let Ok(line) = line {
                let levels: Vec<i32> = line
                    .split_whitespace() // Split the line by whitespace
                    .filter_map(|s: &str| s.parse::<i32>().ok()) // Parse each part into i32
                    .collect();

                let mut sets: Vec<Vec<i32>> = vec![levels.clone()];
                sets.append(&mut create_subsets(&levels));

                for levels in sets {
                    let length = levels.len() - 1;

                    if levels.len() > 1 {
                        let first = levels[0];
                        let second = levels[1];
                        let diff = second - first;
                        let order;

                        if 1 <= diff && diff <= 3 {
                            order = 1;
                        } else if -3 <= diff && diff <= -1 {
                            order = -1;
                        } else {
                            continue;
                        }

                        let mut flag = true;
                        for i in 1..length {
                            let diff = levels[i + 1] - levels[i];
                            if !(order == 1 && 1 <= diff && diff <= 3)
                                && !(order == -1 && -3 <= diff && diff <= -1)
                            {
                                flag = false;
                                break;
                            }
                        }
                        if flag {
                            total_safe += 1;
                            break;
                        }
                    }
                }
            }
        }

        Ok(total_safe)
    }

    assert_eq!(4, part2(BufReader::new(TEST.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result: i32 = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}
