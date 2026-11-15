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
    args = parser.parse_args()
    paths = sorted((ROOT / 'notebooks').glob('*.ipynb'))
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
                code = ''.join(cell['source'])
                exec(compile(code, f'{path.name}:cell-{index}', 'exec'), namespace)
        plt.close('all')
        completed += 1
        print(f'PASS {path.name}', flush=True)
    print(f'Executed {completed} notebooks successfully.', flush=True)

if __name__ == '__main__':
    main()
