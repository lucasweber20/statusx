import argparse


parser = argparse.ArgumentParser()

args = parser.add_argument("-u", "--url", help='Specify url, example: -u https://example.com/?param=value', nargs="+", type=str)
args = parser.add_argument("-l", "--list", help="Specify file with urls, example: -l urls.txt", type=str)
args = parser.add_argument("-o", "--output", help="Specify output file, example: -o outputs.txt", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 2", type=int)

args = parser.parse_args()

def main():
    url = args.url
    file = args.list
    output = args.output
    thread = args.thread

if __name__ == "__main__":
    main()