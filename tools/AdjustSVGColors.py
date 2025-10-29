#!/usr/bin/env python3
"""
Replace color #009688 with #892410 in all SVG files.

This script walks through the resources/images directory and replaces all occurrences
of the color #009688 (Orca teal) with #892410 (Adartys brown) in .svg files,
handling both uppercase and lowercase hex notation.
"""

import os
import sys
from pathlib import Path


def replace_color_in_svg(file_path, old_color='#009688', new_color='#892410'):
    """
    Replace a color in a single SVG file.
    
    Args:
        file_path: Path to the .svg file
        old_color: Color to replace (default: #009688)
        new_color: New color (default: #892410)
        
    Returns:
        tuple: (number of replacements, success boolean)
    """
    try:
        # Read file content with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Store original content
        original_content = content
        
        # Replace both lowercase and uppercase variants
        old_lower = old_color.lower()
        old_upper = old_color.upper()
        new_lower = new_color.lower()
        
        # Count occurrences
        count_lower = content.count(old_lower)
        count_upper = content.count(old_upper)
        total_replacements = count_lower + count_upper
        
        # Replace both variants with lowercase new color
        content = content.replace(old_lower, new_lower)
        content = content.replace(old_upper, new_lower)
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return total_replacements, True
        
        return 0, True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return 0, False


def main():
    """Main entry point."""
    # Parse command line arguments for custom colors
    old_color = '#009688'
    new_color = '#892410'
    
    if len(sys.argv) > 1:
        old_color = sys.argv[1]
    if len(sys.argv) > 2:
        new_color = sys.argv[2]
    
    # Get the project root directory (parent of tools/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    images_dir = project_root / 'resources' / 'images'
    
    if not images_dir.exists():
        print(f"Error: Images directory not found: {images_dir}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning for .svg files in: {images_dir}")
    print(f"Replacing color: {old_color} → {new_color}")
    print("-" * 60)
    
    # Find all .svg files
    svg_files = list(images_dir.rglob('*.svg'))
    
    if not svg_files:
        print("No .svg files found!")
        sys.exit(0)
    
    total_replacements = 0
    processed_files = 0
    failed_files = 0
    
    # Process each file
    for svg_file in sorted(svg_files):
        relative_path = svg_file.relative_to(project_root)
        replacements, success = replace_color_in_svg(svg_file, old_color, new_color)
        
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
    print(f"  Files scanned: {len(svg_files)}")
    print(f"  Files modified: {processed_files}")
    print(f"  Files failed: {failed_files}")
    print(f"  Total replacements: {total_replacements}")
    
    if failed_files > 0:
        sys.exit(1)
    
    print("\n✓ Done!")


if __name__ == '__main__':
    main()
