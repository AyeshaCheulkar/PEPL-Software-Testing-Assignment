
from playwright.sync_api import expect
import os


# Common function to open the Contact page
def open_contact_page(page, shop_base_url):

    # Step 1: Open the Toolshop homepage
    shop_url = f"{shop_base_url.rstrip('/')}/#/"
    page.goto(
        shop_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Step 2: Locate the Contact navigation link
    contact_link = page.locator('[data-test="nav-contact"]')

    # Step 3: Verify that the Contact link is visible
    expect(contact_link).to_be_visible(timeout=15000)

    # Step 4: Click the Contact link
    contact_link.click()

    # Step 5: Verify that the Contact page opens
    expect(
        page.get_by_role("heading", name="Contact")
    ).to_be_visible(timeout=15000)


# Common function to capture screenshots on the bug website
def take_bug_screenshot(page, shop_base_url, screenshot_name):

    if "with-bugs" in shop_base_url:
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(
            path=f"screenshots/{screenshot_name}",
            full_page=True
        )


# Test Case 1: Verify Contact Form fields are visible
def test_contact_form_is_visible(page, shop_base_url):

    open_contact_page(page, shop_base_url)

    expect(page.locator('[data-test="first-name"]')).to_be_visible()
    expect(page.locator('[data-test="last-name"]')).to_be_visible()
    expect(page.locator('[data-test="email"]')).to_be_visible()
    expect(page.locator('[data-test="subject"]')).to_be_visible()
    expect(page.locator('[data-test="message"]')).to_be_visible()
    expect(page.locator('[data-test="attachment"]')).to_be_visible()
    expect(page.locator('[data-test="contact-submit"]')).to_be_visible()

    print("\nAll Contact Form fields are visible!")


# Test Case 2: Verify empty form submission
def test_empty_contact_form_submission(page, shop_base_url):

    open_contact_page(page, shop_base_url)

    page.locator('[data-test="contact-submit"]').click()

    expect(
        page.get_by_role("heading", name="Contact")
    ).to_be_visible()

    print("\nEmpty form submission checked!")


# Test Case 3: Verify invalid email validation
def test_contact_form_invalid_email(page, shop_base_url):

    open_contact_page(page, shop_base_url)

    page.locator('[data-test="first-name"]').fill("Ayesha")
    page.locator('[data-test="last-name"]').fill("Tester")
    page.locator('[data-test="email"]').fill("invalid-email")
    page.locator('[data-test="subject"]').select_option("customer-service")
    page.locator('[data-test="message"]').fill("This is a test message.")

    page.locator('[data-test="contact-submit"]').click()

    expect(
        page.locator('[data-test="email"]')
    ).to_have_js_property("validity.valid", False)

    print("\nInvalid email validation checked!")


# Test Case 4: Verify valid contact form submission
def test_valid_contact_form_submission(page, shop_base_url):

    open_contact_page(page, shop_base_url)

    page.locator('[data-test="first-name"]').fill("Ayesha")
    page.locator('[data-test="last-name"]').fill("Tester")
    page.locator('[data-test="email"]').fill("ayesha.test@example.com")
    page.locator('[data-test="subject"]').select_option("customer-service")
    page.locator('[data-test="message"]').fill(
        "This is a test message for contact form validation."
    )

    page.locator('[data-test="contact-submit"]').click()

    print("\nContact form submission result:")
    print(page.locator("body").inner_text())


# Test Case 5: Verify subject dropdown has no error messages
def test_contact_subject_options(page, shop_base_url):

    open_contact_page(page, shop_base_url)

    subject_dropdown = page.locator('[data-test="subject"]')

    expect(subject_dropdown).to_be_visible()

    if "with-bugs" in shop_base_url:
        subject_dropdown.select_option(
            label="Error 101: Subject not found"
        )
        take_bug_screenshot(
            page,
            shop_base_url,
            "contact-subject-dropdown-errors.png"
        )

    expect(
        subject_dropdown.get_by_text("Error 101: Subject not found")
    ).to_have_count(0)

    expect(
        subject_dropdown.get_by_text("Error 202: Translation error")
    ).to_have_count(0)

    print("\nSubject dropdown options verified!")


# Test Case 6: Verify attachment instructions
def test_contact_attachment_instructions(page, shop_base_url):

    open_contact_page(page, shop_base_url)

    take_bug_screenshot(
        page,
        shop_base_url,
        "contact-attachment-instructions.png"
    )

    attachment_instructions = page.get_by_text(
        "Only files with the txt extension are allowed, and files must be 0kb.",
        exact=True
    )

    expect(attachment_instructions).to_be_visible()

    print("\nAttachment instructions verified!")


# Test Case 7: Verify attachment file type restriction
def test_pdf_attachment_upload(page, shop_base_url):

    open_contact_page(page, shop_base_url)

    attachment_input = page.locator('[data-test="attachment"]')

    accepted_types = attachment_input.get_attribute("accept")

    print("\nAttachment file type validation:")
    print("Website:", shop_base_url)
    print("Accepted file types:", accepted_types)

    if "with-bugs" in shop_base_url:
        take_bug_screenshot(
            page,
            shop_base_url,
            "contact-pdf-attachment-test.png"
        )

    expect(attachment_input).to_have_attribute("accept", ".txt")

    print("\nAttachment file type restriction checked!")


# Test Case 8: Verify PDF attachment submission
def test_pdf_attachment_submission(page, shop_base_url):

    open_contact_page(page, shop_base_url)

    # Step 1: Fill all required contact form fields
    page.locator('[data-test="first-name"]').fill("Ayesha")
    page.locator('[data-test="last-name"]').fill("Tester")
    page.locator('[data-test="email"]').fill("ayesha.test@example.com")

    # Step 2: Select a valid subject
    subject_dropdown = page.locator('[data-test="subject"]')

    subject_dropdown.select_option("customer-service")

    # Step 3: Print the selected subject value
    print("\nSelected subject value:", subject_dropdown.input_value())

    # Step 4: Enter a valid message
    page.locator('[data-test="message"]').fill(
        "Testing PDF attachment validation on the contact form."
    )

    # Step 5: Attach the PDF file
    page.locator('[data-test="attachment"]').set_input_files("sample.pdf")

    print("\nPDF file selected for upload.")

    # Step 6: Submit the completed form
    page.locator('[data-test="contact-submit"]').click()

    # Step 7: Wait for the page to respond
    page.wait_for_timeout(3000)

    # Step 8: Display the page content after submission
    print("\nPage content after PDF submission:")
    print(page.locator("body").inner_text())
# Test Case 9: Verify subject selection and form submission
def test_contact_subject_selection(page, shop_base_url):
    open_contact_page(page, shop_base_url)
    # Fill the required fields
    page.locator('[data-test="first-name"]').fill("Ayesha")
    page.locator('[data-test="last-name"]').fill("Tester")
    page.locator('[data-test="email"]').fill("ayesha.test@example.com")
    # Select Customer service
    subject_dropdown = page.locator('[data-test="subject"]')
    subject_dropdown.select_option("customer-service")
    print("\nSelected subject:", subject_dropdown.input_value())
    # Enter a valid message
    page.locator('[data-test="message"]').fill(
        "This message is being used to test subject validation."
    )
    # Submit the form
    page.locator('[data-test="contact-submit"]').click()
    # Wait for the result
    page.wait_for_timeout(3000)
    # Capture screenshot on bug website
    take_bug_screenshot(
        page,
        shop_base_url,
        "contact-subject-validation.png"
    )
    # Display the result
    page_content = page.locator("body").inner_text()
    print("\nPage content after submission:")
    print(page_content)
    # Verify successful submission
    expect(
        page.get_by_text(
            "Thanks for your message! We will contact you shortly.",
            exact=True
        )
    ).to_be_visible(timeout=10000)