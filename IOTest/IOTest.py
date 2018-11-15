class IOTest(object):
    def read_file_readline(self):
        with open('./test.txt', 'r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                print(line)
                line = f.readline()

    def read_file_readlines(self):
        with open('./test.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                print(line)

    def write_file(self):
        with open('./test.txt', 'a', encoding='utf-8') as f:
            f.write('Hi\n')
            f.write('中国\n')


IO = IOTest()
print('-------readline')
IO.read_file_readline()
print('-------readlines')
IO.read_file_readlines()
IO.write_file()
print('-------write file done')
