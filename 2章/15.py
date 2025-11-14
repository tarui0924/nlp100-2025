# 15.py ファイルを行単位で N 分割

filename = "popular-names.txt"
N = 10  # 1ファイルあたりの行数

with open(filename, encoding="utf-8") as f:
    buf = []
    file_index = 1

    for line in f:
        buf.append(line)
        if len(buf) == N:
            outname = f"popular-names_{file_index}.txt"
            with open(outname, "w", encoding="utf-8") as out:
                out.writelines(buf)
            print(f"{outname} に {len(buf)} 行書き込みました")
            buf = []
            file_index += 1

    # 余りがあれば最後のファイルとして出力
    if buf:
        outname = f"popular-names_{file_index}.txt"
        with open(outname, "w", encoding="utf-8") as out:
            out.writelines(buf)
        print(f"{outname} に {len(buf)} 行書き込みました")
