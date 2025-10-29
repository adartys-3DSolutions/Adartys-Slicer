#!/usr/bin/env python3
"""
Replace 'Orca' with 'Adartys' in all .po translation files.

This script walks through the localization directory and replaces all occurrences
of 'Orca' (case-sensitive) with 'Adartys' in .po files, preserving file encoding.
"""

import os
import sys
from pathlib import Path


def replace_in_po_file(file_path):
    """
    Replace 'Orca' with 'Adartys' in a single .po file.
    
    Args:
        file_path: Path to the .po file
        
    Returns:
        tuple: (number of replacements, success boolean)
    """
    try:
        # Read file content with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count and replace occurrences
        original_content = content
        content = content.replace('Orca', 'Adartys')
        content = content.replace('orca', 'adartys')
        
        replacements = original_content.count('Orca') + original_content.count('orca')
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return replacements, True
        
        return 0, True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return 0, False


def main():
    """Main entry point."""
    # Get the project root directory (parent of tools/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    localization_dir = project_root / 'localization'
    
    if not localization_dir.exists():
        print(f"Error: Localization directory not found: {localization_dir}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning for .po files in: {localization_dir}")
    print("-" * 60)
    
    # Find all .po files
    po_files = list(localization_dir.rglob('*.po'))
    
    if not po_files:
        print("No .po files found!")
        sys.exit(0)
    
    total_replacements = 0
    processed_files = 0
    failed_files = 0
    
    # Process each file
    for po_file in sorted(po_files):
        relative_path = po_file.relative_to(project_root)
        replacements, success = replace_in_po_file(po_file)
        
        if success:
            if replacements > 0:
                print(f"✓ {relative_path}: {replacements} replacement(s)")
                total_replacements += replacements
                processed_files += 1
            else:
                print(f"  {relative_path}: no changes needed")
        else:
            print(f"✗ {relative_path}: FAILED")
            failed_files += 1
    
    # Summary
    print("-" * 60)
    print(f"Summary:")
    print(f"  Files scanned: {len(po_files)}")
    print(f"  Files modified: {processed_files}")
    print(f"  Files failed: {failed_files}")
    print(f"  Total replacements: {total_replacements}")
    
    if failed_files > 0:
        sys.exit(1)
    
    print("\n✓ Done!")


if __name__ == '__main__':
    main()
