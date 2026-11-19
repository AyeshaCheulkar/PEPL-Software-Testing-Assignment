
from playwright.sync_api import expect


def test_product_details(page, shop_base_url):

    # Step 1: Open Toolshop homepage
    shop_url = f"{shop_base_url.rstrip('/')}/#/"
    page.goto(shop_url)

    # Step 2: Locate the first product card
    first_product = page.locator(
        '[data-test^="product-"]'
    ).first

    # Step 3: Wait until the product is visible
    first_product.wait_for(state="visible", timeout=15000)

    # Step 4: Get the product name from the listing
    product_name = first_product.locator(
        '[data-test="product-name"]'
    ).inner_text().strip()

    print("\nSelected product:", product_name)

    # Step 5: Click the product card
    first_product.click()

    # Step 6: Wait for product details to load
    page.wait_for_timeout(3000)

    # Step 7: Verify product name
    expect(page.get_by_text(
        product_name,
        exact=True
    ).first).to_be_visible()

    # Step 8: Verify product price
    product_price = page.get_by_text(
        "$14.15",
        exact=True
    )

    expect(product_price).to_be_visible()

    # Step 9: Verify product description
    description = page.get_by_text(
        "Versatile combination pliers designed for gripping, bending, and cutting wire with ease.",
        exact=False
    )

    expect(description).to_be_visible()

    # Step 10: Verify Add to Cart button
    add_to_cart_button = page.get_by_role(
        "button",
        name="Add to cart"
    )

    expect(add_to_cart_button).to_be_visible()

    # Step 11: Print confirmation
    print("\nProduct details verified successfully.")
    print("Product:", product_name)
    print("Price: $14.15")
    print("Add to Cart button is visible.")
