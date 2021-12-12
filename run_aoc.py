from genericpath import exists
import os
import subprocess
import sys
import urllib.request

session_id = os.getenv('AOC_SESSION')

# Usage shall be run_aoc.py <day> [part] [test]
def main():
    year = None
    part = None
    day = None
    testing = False
    n_args = len(sys.argv)
    if n_args >= 2:
        year = int(sys.argv[1])
    if n_args >= 3:
        day = int(sys.argv[2])
    if n_args >= 4:
        part = int(sys.argv[3])
    if n_args >= 5:
        testing = bool(sys.argv[4])
    if n_args < 2:
        print(f"Usage: {sys.argv[0]} <year(YY)> <day> [part]")
        exit()
    
    if year >= 15 and year <= 99:
        year = year+2000
    if year < 2015 or year > 2099:
        print("Year argument must lie in [2015, current_year]")
    if day < 1 or day > 25:
        print(f"Day argument must lie in [1, 25]")
        exit()
    if part is not None and (part < 1 or part > 2):
        print(f"Part argument must lie in [1,2]")
        exit()

    current_dir = os.path.dirname(os.path.relpath(__file__))

    if part is not None:
        part = [part]
    else:
        part = [1, 2]

    day = f"{day:02}"
    folder = f".{current_dir}/{year}/day{day}"
    part1_name = f"{folder}/day{day}_1.py"
    part2_name = f"{folder}/day{day}_2.py"
    input_name = f"{folder}/input_{day}"
    test_input_name = f"{folder}/test_input_{day}"

    script_template = ""

    if not exists(folder):
        print(f"Missing folder for year {year} day {day}")
        os.makedirs(folder)
        for script in [part1_name, part2_name]:
            os.mknod(script)
            with open(script, "w") as file:
                file.write('import sys, os\nsys.path.append(os.path.abspath("."))\nimport aoc')
        
        if session_id is not None:
            print(f"Downloading input for day {day}")
            opener = urllib.request.build_opener()
            opener.addheaders = [("Cookie", f"session={session_id}")]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(f"https://adventofcode.com/{int(year)}/day/{int(day)}/input", input_name)
        else:
            print("AOC_SESSION was not set. Prepairing empty input file...")
            os.mknod(input_name)
        os.mknod(test_input_name)

    if not exists(input_name):
        print(f"Missing inputfile for day {day}")

    script_names = {1: part1_name, 2:part2_name}
    for part in part:
        if not exists(script_names[part]):
            print(f"Script for aoc {year} day {day} part {part} is missing...")
            continue
        input_file = None
        if testing:
            print(f"Testing aoc {year} day {day} part {part}")
            input_file = test_input_name
        else:
            print(f"Running aoc {year} day {day} part {part}")
            input_file = input_name
        
        subprocess.run(["python3", script_names[part], input_file])
        
        

    

if __name__ == "__main__":
    main()