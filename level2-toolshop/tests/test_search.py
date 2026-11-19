
from playwright.sync_api import expect
def test_search_product(page, shop_base_url):
    # Step 1: Open Toolshop homepage
    shop_url = f"{shop_base_url.rstrip('/')}/#/"
    page.goto(shop_url)
    # Step 2: Locate the search box
    search_box = page.locator('[data-test="search-query"]')
    # Step 3: Verify that the search box is visible
    expect(search_box).to_be_visible(timeout=15000)
    # Step 4: Enter the product name
    search_box.fill("Combination Pliers")
    # Step 5: Locate and click the search button
    search_button = page.locator('[data-test="search-submit"]')
    search_button.click()
    # Step 6: Verify that the matching product appears
    product_names = page.locator(
        '[data-test^="product-"] [data-test="product-name"]'
    )
    expect(product_names.first).to_have_text(
        "Combination Pliers",
        timeout=15000
    )
    # Step 7: Print the search result
    print("Search result:", product_names.all_text_contents())
