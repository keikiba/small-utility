import re


def clean_string(str):
    # remove newline code, truncate multiple spaces into one
    return re.sub('\s+', ' ', str.replace('\r\n', '').replace('\n', '')) if str else ''


def safe_lookup(k, dic):
    return dic[k] if k in dic else ''


def main():
    pass


if __name__ == "__main__":
    main()
