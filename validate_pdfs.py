#!/usr/bin/env python3
"""
PDF Validation Script
Validates all PDF files in the current directory.
Checks file accessibility, PDF header validity, and extracts basic info.
"""

import os
import sys
from pathlib import Path

# Try to import PDF library
PDF_LIBRARY = None
try:
    from pypdf import PdfReader
    PDF_LIBRARY = "pypdf"
except ImportError:
    try:
        from PyPDF2 import PdfReader
        PDF_LIBRARY = "PyPDF2"
    except ImportError:
        pass


def check_pdf_header(filepath):
    """Check if file has valid PDF header (starts with %PDF-)"""
    try:
        with open(filepath, 'rb') as f:
            header = f.read(8)
            if header.startswith(b'%PDF-'):
                return True, header[:8].decode('latin-1')
            return False, f"Invalid header: {header[:8]}"
    except Exception as e:
        return False, f"Read error: {str(e)}"


def validate_pdf_with_library(filepath):
    """Validate PDF using pypdf/PyPDF2 library"""
    try:
        reader = PdfReader(filepath)
        page_count = len(reader.pages)
        return True, {"pages": page_count}
    except Exception as e:
        return False, str(e)


def validate_pdf_fallback(filepath):
    """Fallback validation - just check header and basic structure"""
    # Check header
    valid, msg = check_pdf_header(filepath)
    if not valid:
        return False, msg

    # Try to find %%EOF marker (basic PDF structure check)
    try:
        with open(filepath, 'rb') as f:
            # Check last 1024 bytes for EOF marker
            f.seek(0, 2)  # Go to end
            size = f.tell()
            f.seek(max(0, size - 1024))
            tail = f.read()
            if b'%%EOF' in tail:
                return True, {"pages": "unknown (library not available)"}
            return False, "Missing %%EOF marker"
    except Exception as e:
        return False, f"Structure check error: {str(e)}"


def validate_pdf(filepath):
    """Main validation function"""
    # First check accessibility
    if not os.path.exists(filepath):
        return False, "File does not exist", None

    if not os.access(filepath, os.R_OK):
        return False, "File not readable (permission denied)", None

    # Check file size
    try:
        size = os.path.getsize(filepath)
        if size == 0:
            return False, "File is empty", None
    except Exception as e:
        return False, f"Cannot get file size: {str(e)}", None

    # Check PDF header
    valid_header, header_msg = check_pdf_header(filepath)
    if not valid_header:
        return False, header_msg, None

    # Full validation
    if PDF_LIBRARY:
        valid, result = validate_pdf_with_library(filepath)
    else:
        valid, result = validate_pdf_fallback(filepath)

    if valid:
        return True, None, result
    else:
        return False, result, None


def print_progress(current, total, width=50):
    """Print progress bar"""
    percent = current / total
    filled = int(width * percent)
    bar = '=' * filled + '-' * (width - filled)
    sys.stdout.write(f'\r[{bar}] {current}/{total} ({percent*100:.1f}%)')
    sys.stdout.flush()


def main():
    # Get current directory
    current_dir = Path('.')

    # Find all PDF files
    pdf_files = sorted(current_dir.glob('*.pdf'))
    total_pdfs = len(pdf_files)

    if total_pdfs == 0:
        print("No PDF files found in current directory.")
        return

    print(f"PDF Validation Report")
    print(f"=" * 60)
    print(f"Directory: {os.getcwd()}")
    print(f"PDF Library: {PDF_LIBRARY if PDF_LIBRARY else 'None (using fallback)'}")
    print(f"Total PDFs found: {total_pdfs}")
    print(f"=" * 60)
    print(f"\nValidating PDFs...")

    valid_pdfs = []
    invalid_pdfs = []
    access_errors = []

    for i, pdf_path in enumerate(pdf_files, 1):
        print_progress(i, total_pdfs)

        is_valid, error_msg, info = validate_pdf(pdf_path)

        if is_valid:
            valid_pdfs.append((pdf_path.name, info))
        elif "permission" in str(error_msg).lower() or "access" in str(error_msg).lower():
            access_errors.append((pdf_path.name, error_msg))
        else:
            invalid_pdfs.append((pdf_path.name, error_msg))

    # Clear progress line and print results
    print('\r' + ' ' * 70 + '\r')
    print(f"\n{'=' * 60}")
    print("VALIDATION RESULTS")
    print(f"{'=' * 60}")

    print(f"\nSummary:")
    print(f"  Total PDFs found:    {total_pdfs}")
    print(f"  Valid PDFs:          {len(valid_pdfs)}")
    print(f"  Invalid/Corrupt:     {len(invalid_pdfs)}")
    print(f"  Access Errors:       {len(access_errors)}")

    if invalid_pdfs:
        print(f"\n{'=' * 60}")
        print("INVALID/CORRUPT PDFs:")
        print(f"{'=' * 60}")
        for name, reason in invalid_pdfs:
            print(f"  - {name}")
            print(f"    Reason: {reason}")

    if access_errors:
        print(f"\n{'=' * 60}")
        print("ACCESS ERRORS:")
        print(f"{'=' * 60}")
        for name, reason in access_errors:
            print(f"  - {name}")
            print(f"    Reason: {reason}")

    if not invalid_pdfs and not access_errors:
        print(f"\nAll {total_pdfs} PDFs are valid!")

    print(f"\n{'=' * 60}")
    print("Validation complete.")

    # Return exit code based on results
    if invalid_pdfs or access_errors:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
