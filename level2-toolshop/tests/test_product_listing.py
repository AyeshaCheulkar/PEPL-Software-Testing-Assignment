
from playwright.sync_api import expect


# Test Case 1: Verify product listing is visible
def test_product_listing_is_visible(page, shop_base_url):

    # Step 1: Open the actual Toolshop homepage
    shop_url = f"{shop_base_url.rstrip('/')}/#/"
    page.goto(
        shop_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Step 2: Locate all product cards
    products = page.locator(
        'a[data-test^="product-"]'
    )

    # Step 3: Wait for the first product to appear
    expect(products.first).to_be_visible(timeout=15000)

    # Step 4: Verify that products are displayed
    assert products.count() > 0, "No products were displayed"

    # Step 5: Display the total number of products
    print("\nProducts found:", products.count())

    print("\nProduct listing verified successfully!")
