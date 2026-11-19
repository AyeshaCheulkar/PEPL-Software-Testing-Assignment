# BUG-006: Missing File Type Restriction on Contact Form Attachment

**Severity:** Medium (provisional)  
**Module:** Contact Form – Attachment  
**Environment:** Bug Build – https://with-bugs.practicesoftwaretesting.com  
**Browser:** Chromium  
**Status:** Open

## Description

The attachment input on the Contact page is missing the HTML `accept` attribute that restricts file selection to `.txt` files.

The reference website uses `accept=".txt"`, whereas the bug website has no `accept` attribute.

## Steps to Reproduce

1. Open the reference website and navigate to Contact.
2. Inspect the attachment input using its `data-test="attachment"` attribute.
3. Observe that its `accept` attribute is `.txt`.
4. Open the bug website and navigate to Contact.
5. Inspect the same attachment input.
6. Observe that the `accept` attribute is missing.

## Expected Result

The attachment input should have the attribute `accept=".txt"`, consistent with the reference website.

## Actual Result

The bug website's attachment input has no `accept` attribute.

The displayed instructions also mention `.txt`, `.pdf` and `.jpg` files smaller than 500 KB, unlike the reference website.

## Evidence

- Screenshot: `contact-attachment-instructions.png`
- Screenshot: `contact-pdf-attachment-test.png`
- Automated test: `test_pdf_attachment_upload`
- Reference result: PASSED
- Bug-build result: FAILED

Reference actual attribute: `.txt`

Bug-build actual attribute: `None`

## Impact

The browser's file picker does not receive the reference website's file-type restriction. Users may be able to select unsupported file types. Server-side file validation has not yet been verified.