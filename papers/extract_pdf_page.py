#!/usr/bin/env python3
"""Extract text content from a specific page of a PDF file."""

import sys
import fitz  # PyMuPDF


def extract_page_text(pdf_path: str, page_number: int) -> str:
    """
    Extract text from a specific page of a PDF.

    Args:
        pdf_path: Path to the PDF file
        page_number: 1-indexed page number

    Returns:
        Text content of the specified page
    """
    try:
        doc = fitz.open(pdf_path)
    except FileNotFoundError:
        print(f"Error: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error opening PDF: {e}", file=sys.stderr)
        sys.exit(1)

    total_pages = len(doc)

    if page_number < 1 or page_number > total_pages:
        print(f"Error: Invalid page number {page_number}. PDF has {total_pages} page(s).", file=sys.stderr)
        doc.close()
        sys.exit(1)

    # Convert to 0-indexed
    page = doc[page_number - 1]
    text = page.get_text()
    doc.close()

    return text


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <pdf_file> <page_number>", file=sys.stderr)
        print("  pdf_file: Path to the PDF file", file=sys.stderr)
        print("  page_number: Page number (1-indexed)", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]

    try:
        page_number = int(sys.argv[2])
    except ValueError:
        print(f"Error: Page number must be an integer, got: {sys.argv[2]}", file=sys.stderr)
        sys.exit(1)

    text = extract_page_text(pdf_path, page_number)
    print(text)


if __name__ == "__main__":
    main()
