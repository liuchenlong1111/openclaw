#!/usr/bin/env python3
"""
Extract text content from PDF files.
Supports both text-based and scanned PDFs (with OCR).
"""

import sys
import argparse

try:
    import PyPDF2
except ImportError:
    print("Error: PyPDF2 not installed. Run: pip install PyPDF2", file=sys.stderr)
    sys.exit(1)

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

def extract_with_pdfplumber(file_path):
    """Extract text using pdfplumber (better for complex layouts)"""
    text_parts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
    return "\n\n".join(text_parts)

def extract_with_pypdf2(file_path):
    """Extract text using PyPDF2 (fallback)"""
    text_parts = []
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
    return "\n\n".join(text_parts)

def extract_pdf(file_path):
    """Extract text from PDF, trying multiple methods"""
    try:
        if HAS_PDFPLUMBER:
            return extract_with_pdfplumber(file_path)
        else:
            return extract_with_pypdf2(file_path)
    except Exception as e:
        print(f"Error extracting PDF: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Extract text from PDF files')
    parser.add_argument('file_path', help='Path to PDF file')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    args = parser.parse_args()
    
    text = extract_pdf(args.file_path)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Extracted text saved to {args.output}", file=sys.stderr)
    else:
        print(text)

if __name__ == '__main__':
    main()
