#!/usr/bin/env python3
"""
Plugin packaging tool - equivalent to `zip -r <name>.zip .`
Usage: python pack_plugin.py <plugin_dir> [output_name]
"""

import argparse
import os
import zipfile
from pathlib import Path


def pack_plugin(plugin_dir: str, output_name: str = None) -> str:
    """
    Pack a plugin directory into a zip file.

    Args:
        plugin_dir: Path to the plugin directory
        output_name: Optional output zip filename (without .zip extension)

    Returns:
        Path to the created zip file
    """
    plugin_path = Path(plugin_dir).resolve()

    if not plugin_path.is_dir():
        raise ValueError(f"Directory not found: {plugin_path}")

    # Default output name is the directory name
    if output_name is None:
        output_name = plugin_path.name

    # Output zip file inside the plugin directory
    zip_path = plugin_path / f"{output_name}.zip"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(plugin_path):
            # Skip __pycache__ directories
            dirs[:] = [d for d in dirs if d != '__pycache__']

            for file in files:
                file_path = Path(root) / file
                # Skip the output zip file itself and .pyc files
                if file_path == zip_path or file.endswith('.pyc'):
                    continue
                # Calculate relative path from plugin directory
                arcname = file_path.relative_to(plugin_path)
                zf.write(file_path, arcname)

    return str(zip_path)


def main():
    parser = argparse.ArgumentParser(
        description='Pack a plugin directory into a zip file'
    )
    parser.add_argument('plugin_dir', help='Path to the plugin directory')
    parser.add_argument('-o', '--output', help='Output zip filename (without .zip)')

    args = parser.parse_args()

    try:
        zip_path = pack_plugin(args.plugin_dir, args.output)
        print(f"Created: {zip_path}")
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
