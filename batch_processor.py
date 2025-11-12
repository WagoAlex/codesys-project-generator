# -*- coding: utf-8 -*-
"""
WAGO PLC Configuration Batch Processor
Processes Excel files and generates organized output

Usage:
    python batch_processor.py --input=/path/to/input.xls --output=/path/to/output
    
Examples:
    python batch_processor.py --input=measuring_points.xls --output=./configs
    python batch_processor.py --input=/usr/src/app/data/points.xls --output=/usr/src/app/output
"""

import os
import sys
import argparse
from excel_to_json_converter import PLCConfigExtractor


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='WAGO PLC Configuration Batch Processor',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python batch_processor.py --input=measuring_points.xls --output=./configs
    python batch_processor.py --input=/full/path/to/file.xls --output=/full/path/to/output
        """
    )
    
    parser.add_argument(
        '--input',
        required=True,
        help='Path to Excel input file (.xls or .xlsx)'
    )
    
    parser.add_argument(
        '--output',
        required=True,
        help='Path to output directory'
    )
    
    return parser.parse_args()


def main():
    """Main processing function"""
    
    # Parse arguments
    args = parse_arguments()
    
    input_file = args.input
    output_dir = args.output
    
    # Validate input file
    if not os.path.exists(input_file):
        print(f"ERROR: Input file not found: {input_file}")
        sys.exit(1)
    
    if not input_file.lower().endswith(('.xls', '.xlsx')):
        print(f"ERROR: Input file must be .xls or .xlsx format")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print("\n" + "="*80)
    print("WAGO PLC Configuration Processor")
    print("="*80)
    print(f"Input:  {input_file}")
    print(f"Output: {output_dir}")
    print("="*80 + "\n")
    
    try:
        # Process the file
        extractor = PLCConfigExtractor(input_file)
        json_files = extractor.process(output_dir)
        
        # Print results
        print("\n" + "="*80)
        print("PROCESSING COMPLETE")
        print("="*80)
        print(f"Generated {len(json_files)} PLC configuration files")
        print(f"Total PLCs: {extractor.stats['total_plcs']}")
        print(f"Total Signals: {extractor.stats['total_signals']}")
        print(f"Total Modules: {extractor.stats['total_modules']}")
        print(f"Warnings: {extractor.stats['warnings']}")
        print(f"Errors: {extractor.stats['errors']}")
        print(f"\nOutput directory: {output_dir}")
        print("="*80 + "\n")
        
        sys.exit(0)
        
    except Exception as e:
        print(f"\nERROR: Processing failed: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
