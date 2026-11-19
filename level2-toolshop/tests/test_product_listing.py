
from playwright.sync_api import expect


def test_product_listing_is_visible(page, shop_base_url):

    # Step 1: Open the actual shop route
    shop_url = f"{shop_base_url.rstrip('/')}/#/"
    page.goto(shop_url)

    # Step 2: Locate all product cards
    products = page.locator('[data-test^="product-"]')

    # Step 3: Verify that the first product is visible
    expect(products.first).to_be_visible(timeout=15000)

    # Step 4: Verify that products exist
    assert products.count() > 0

    # Step 5: Display the number of products
    print("Products found:", products.count())
