"""Run selected notebook code in order, with a headless plotting backend."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--include-downloads', action='store_true')
    parser.add_argument('--notebook', help='Run only a notebook whose filename starts with this value, e.g. 02')
    args = parser.parse_args()
    paths = sorted((ROOT / 'notebooks').glob('*.ipynb'))
    if args.notebook:
        paths = [path for path in paths if path.name.startswith(args.notebook)]
        if not paths:
            parser.error('No matching notebook')
    completed = 0
    for path in paths:
        if path.name.startswith('02-') and not args.include_downloads:
            print(f'SKIP {path.name}: use --include-downloads to include California housing', flush=True)
            continue
        print(f'RUN {path.name}', flush=True)
        notebook = json.loads(path.read_text(encoding='utf-8'))
        namespace = {'__name__': '__main__', 'display': lambda *items: print(*items, sep='\n')}
        plt.show = lambda *a, **kw: plt.close('all')
        for index, cell in enumerate(notebook['cells']):
            if cell['cell_type'] == 'code':
                print(f'  cell {index}', flush=True)
                code = ''.join(cell['source'])
                exec(compile(code, f'{path.name}:cell-{index}', 'exec'), namespace)
        plt.close('all')
        completed += 1
        print(f'PASS {path.name}', flush=True)
    print(f'Executed {completed} notebooks successfully.', flush=True)

if __name__ == '__main__':
    main()

