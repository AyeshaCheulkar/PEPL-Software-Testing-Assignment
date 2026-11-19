# BUG-007: Contact Form Does Not Recognise Selected Subject

**Severity:** Medium

**Module:** Contact Form

**Environment:** Bug Build – https://with-bugs.practicesoftwaretesting.com

**Status:** Open

### Description

The Contact Form displays a "Subject is required" validation error even after the user selects a valid subject, such as "Customer service".

### Preconditions

- Contact page is accessible.
- User is on the Bug Build.

### Steps to Reproduce

1. Open the Contact page.
2. Enter a valid first name.
3. Enter a valid last name.
4. Enter a valid email address.
5. Select "Customer service" from the Subject dropdown.
6. Enter a message containing at least 50 characters.
7. Click Send.

### Expected Result

The selected subject should be recognised as valid, and the contact form should submit successfully with a confirmation message.

### Actual Result

The dropdown shows "Customer service" as selected, but the application displays "Subject is required" and does not submit the form.

### Evidence

- Screenshot: `screenshots/contact-subject-validation.png`
- Automated test: `test_contact_subject_selection`
- Reference Build: Passed.
- Bug Build: Failed.

### Impact

Users may be unable to submit contact enquiries even after completing all required fields correctly.

### Status

Reproducible on the Bug Build.