import os

parent_dir = 'C:\\Users\\jerem\\Python\\100-days-python\\'
print(parent_dir)

for num in range(9,101):
    day = f'Day {num:03d}'
    new_dir_path = (f'{parent_dir}Day {num:03d}')
    os.mkdir(new_dir_path)
    print(f'Directory {day} was created')