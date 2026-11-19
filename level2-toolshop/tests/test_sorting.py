import pytest
from playwright.sync_api import expect
@pytest.mark.parametrize(
    "sort_value, sort_type",
    [
        ("name,asc", "name"),
        ("name,desc", "name"),
        ("price,asc", "price"),
        ("price,desc", "price"),
    ]
)
def test_product_sorting(page, shop_base_url, sort_value, sort_type):
    # Step 1: Open Toolshop
    shop_url = f"{shop_base_url.rstrip('/')}/#/"
    page.goto(shop_url)
    # Step 2: Locate the sorting dropdown
    sort_dropdown = page.locator('[data-test="sort"]')
    # Step 3: Locate product names
    product_names = page.locator(
        '[data-test^="product-"] [data-test="product-name"]'
    )
    # Step 4: Locate product prices
    product_prices = page.locator(
        '[data-test^="product-"] [data-test="product-price"]'
    )
    # Step 5: Wait until products are visible
    expect(product_names.first).to_be_visible(timeout=15000)
    # Step 6: Select the required sorting option
    sort_dropdown.select_option(sort_value)
    # Step 7: Wait until the product list is updated
    if sort_type == "name":
        if sort_value == "name,asc":
            expect(product_names.first).to_have_text(
                "Adjustable Wrench", timeout=15000
            )
        else:
            expect(product_names.first).to_have_text(
                "Wood Saw", timeout=15000
            )
    else:
        page.wait_for_function(
            """(sortValue) => {
                const elements = document.querySelectorAll(
                    '[data-test^="product-"] [data-test="product-price"]'
                );
                const prices = Array.from(elements).map(element =>
                    parseFloat(element.textContent.replace('$', '').trim())
                );
                if (prices.length === 0) return false;
                const sortedPrices = [...prices].sort((a, b) =>
                    sortValue === 'price,asc' ? a - b : b - a
                );
                return prices.every(
                    (price, index) => price === sortedPrices[index]
                );
            }""",
            arg=sort_value,
            timeout=15000
        )
    # Step 8: Collect all product names
    names = [
        name.strip().lower()
        for name in product_names.all_text_contents()
    ]
    # Step 9: Collect all product prices
    prices = [
        float(price.strip().replace("$", ""))
        for price in product_prices.all_text_contents()
    ]
    # Step 10: Verify the sorting order
    if sort_value == "name,asc":
        assert names == sorted(names)
    elif sort_value == "name,desc":
        assert names == sorted(names, reverse=True)
    elif sort_value == "price,asc":
        assert prices == sorted(prices)
    elif sort_value == "price,desc":
        assert prices == sorted(prices, reverse=True)
