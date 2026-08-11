import argparse
import requests
import concurrent.futures


parser = argparse.ArgumentParser()

args = parser.add_argument("-l", "--list", help="Specify file with urls, example: -l urls.txt", type=str)
args = parser.add_argument("-o", "--output", help="Specify output file, example: -o outputs.txt", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 2", type=int)
args = parser.add_argument("-ti", "--timeout", help="Specify timeout number, example: --timeout 5", default=5, type=int)

args = parser.parse_args()

FILE = args.list
OUTPUT = args.output
THREAD = args.thread
TIMEOUT = args.timeout

def main():

    # Read file
    urls = []
    with open(FILE, 'r') as f:
        for file in f:
            urls.append(file.strip())

    # Requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREAD) as executor:
        futures = [executor.submit(requests_urls, url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                if result[1] >= 200 and result[1] < 300:
                    print(f"{result[0]} -> \033[92m{result[1]}\033[00m")
                elif result[1] >= 300 and result[1] < 400:
                    print(f"{result[0]} -> \033[36m{result[1]}\033[00m")
                elif result[1] >= 400 and result[1] < 500:
                    print(f"{result[0]} -> \033[33m{result[1]}\033[00m")
                elif result[1] >= 500 and result[1] < 600:
                    print(f"{result[0]} -> \033[31m{result[1]}\033[00m")

def requests_urls(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
    try:
        req = requests.get(url, headers=headers, allow_redirects=False, timeout=TIMEOUT)
        req_url = req.url
        status_code = req.status_code
        return req_url, status_code
    except:
        pass

if __name__ == "__main__":
    main()