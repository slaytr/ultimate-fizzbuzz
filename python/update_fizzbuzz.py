def update_fizzbuzz(current_num_lines: int, num_lines_to_add: int, file):
    for i in range(current_num_lines + 1, current_num_lines + num_lines_to_add +1):
        out_str = ""
        if i % 3 == 0:
            out_str += "Fizz"
        if i % 5 == 0:
            out_str += "Buzz"
        file.write(f"        if i == {i}:\n")
        if out_str:
            file.write(f"            print('{out_str}')\n")
        else:
            file.write(f"            print({i})\n")


with open("fizzbuzz.py", "r+") as fizzbuzz_script:
    increment_by = 10
    update_fizzbuzz(int(fizzbuzz_script.readlines()[-2].split(" ")[-1][:-2]), increment_by, fizzbuzz_script)


