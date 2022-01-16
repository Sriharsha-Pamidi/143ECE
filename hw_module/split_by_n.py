def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''

    assert type(fname) == str and type(n) == int and n > 0

    from pathlib import Path
    file_size = Path(fname).stat().st_size
    read_size = 0

    with open(fname) as f:
        carry = ""
        for i in range(n):
            chunk_size = (file_size-read_size) / (n-i)
            f1_size = 0
            f1name = fname + '_' + '%03d' % i + '.txt'
            f1 = open(f1name,'wt')
            if carry != "":
                f1.write(carry)
                f1_size += len(carry)
                carry = ""
            while chunk_size >= f1_size:
                line = f.readline()
                if line:
                    if chunk_size >= f1_size + len(line):
                        f1.write(line)
                        f1_size += len(line)
                    else:
                        carry = line
                        break
                else:
                    break
            f1.close()
            read_size += Path(f1name).stat().st_size

    assert file_size == read_size
