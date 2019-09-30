from pathlib import Path
import pandas as pd


def add_header(fp):
    df = pd.read_csv(fp, header=-1)
    df2 = df.rename(columns={0: '氏名', 1: 'メールアドレス', 2: '得点'})
    df2.to_csv(fp, index=False, encoding='utf_8_sig')


def main():
    p = Path('score_data')
    file_path_list = list(p.glob('**/*csv'))
    for f in file_path_list:
        add_header(f)


if __name__ == '__main__':
    main()
