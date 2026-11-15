#!/usr/bin/env python3
"""Read-only, dependency-free PHP project inventory. Created by Tariq Al-Taie."""
import argparse
import json
import re
from pathlib import Path

SKIP = {'.git', 'node_modules', 'vendor', '.next', 'dist', 'build', 'storage', 'cache'}
EXTENSIONS = {'.php', '.phtml', '.sql', '.js', '.ts', '.css', '.html', '.twig'}
PATTERNS = {
    'database': r'\b(PDO|mysqli_|DB::|->query\s*\(|->prepare\s*\()',
    'session': r'\b(session_start|\$_SESSION|Session::)',
    'authentication': r'\b(password_verify|password_hash|Auth::|auth\s*\()',
    'routes': r'\b(Route::|\$router->|addRoute\s*\()',
    'uploads': r'\b(move_uploaded_file|\$_FILES)',
    'mail': r'\b(mail\s*\(|Mail::)',
    'external_http': r'\b(curl_init|GuzzleHttp|Http::)',
}

def scan(root):
    if not root.is_dir():
        raise ValueError('Source directory does not exist')
    files = []
    totals = {k: 0 for k in PATTERNS}
    for path in sorted(root.rglob('*')):
        if not path.is_file() or any(part in SKIP for part in path.relative_to(root).parts):
            continue
        if path.suffix.lower() not in EXTENSIONS:
            continue
        try:
            content = path.read_text(encoding='utf-8', errors='replace')
        except OSError:
            continue
        counts = {k: len(re.findall(pattern, content)) for k, pattern in PATTERNS.items()} if path.suffix.lower() in {'.php', '.phtml'} else {}
        for key, value in counts.items():
            totals[key] += value
        files.append({'path': path.relative_to(root).as_posix(), 'lines': len(content.splitlines()), 'signals': {k: v for k, v in counts.items() if v}})
    return {'source': str(root.resolve()), 'file_count': len(files), 'signals': totals, 'files': files, 'warning': 'Heuristic inventory only. Not a security audit or complete dependency analysis.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('--output', default='migration-inventory.json')
    args = parser.parse_args()
    result = scan(Path(args.source))
    Path(args.output).write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(f"Scanned {result['file_count']} files; wrote {args.output}")
