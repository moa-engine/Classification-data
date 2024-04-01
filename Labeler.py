def add_label_to_each_line(input_file, output_file, label="__label__sport"):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            f_out.write(f"{label} {line}")
add_label_to_each_line('ورزش.txt', 'خروجی ورزش.txt')
