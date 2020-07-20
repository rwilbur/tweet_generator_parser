import argparse
from urllib.request import Request, urlopen
import re

parser = argparse.ArgumentParser()
parser.add_argument("--seed", type=str, help="seed to generate tweet from", default=None)
args = parser.parse_args()

req = None
if args.seed:
    req = Request(f'https://thoughts.sushant-kumar.com/{args.seed}', headers={'User-Agent': 'Mozilla/5.0'})
else:
    req = Request(f'https://thoughts.sushant-kumar.com/', headers={'User-Agent': 'Mozilla/5.0'})

page = urlopen(req).read().decode('utf-8')
quote = re.search('(?<=</span>).*?(?=<span>)', page).group(0)

print(quote)
