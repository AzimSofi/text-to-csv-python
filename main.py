input_file = input('Input file name: ')
input_file = f"{input_file}.txt"

output_file = input('Output file name: ')
output_file = f"{output_file}.csv"

with open(input_file , 'r', encoding='utf-8') as file:
    words = [line.split()[0] for line in file]

# 単語をセミコロンで結合する
csv_content = '\n'.join(words) + '\n'

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(csv_content)
