def determine_length_files(file_name):
    with open(file_name,'r', encoding='utf-8') as f:
        res = f.readlines()
    return (file_name, len(res), res)

len_files = []
files_list = ['1.txt', '2.txt','3.txt', '4.txt', '5.txt']
for file_name in files_list:
    len_files.append(determine_length_files(file_name))

sorted_tuples = sorted(len_files, key=lambda x: x[1])

with open('res.txt','w', encoding='utf-8') as file:
    for data in sorted_tuples:
        file.write(f'{data[0]}\n{data[1]}\n{"".join(data[2])}\n')