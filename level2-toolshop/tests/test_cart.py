
from playwright.sync_api import expect
import os


def take_bug_screenshot(page, shop_base_url, screenshot_name):
    """
    Capture screenshots only when testing the bug website.
    """
    if "with-bugs" in shop_base_url:
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(
            path=f"screenshots/{screenshot_name}",
            full_page=True
        )


def test_product_is_added_to_cart(page, shop_base_url):

    # Step 1: Open Toolshop homepage
    shop_url = f"{shop_base_url.rstrip('/')}/#/"
    page.goto(
        shop_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Step 2: Locate product cards
    product_cards = page.locator(
        'a[data-test^="product-"]'
    )

    # Step 3: Wait for products to appear
    product_cards.first.wait_for(
        state="visible",
        timeout=30000
    )

    # Step 4: Select the second product
    second_product = product_cards.nth(1)

    # Step 5: Get product name
    product_name = second_product.locator(
        '[data-test="product-name"]'
    ).inner_text().strip()

    print("\nSelected product:", product_name)

    # Step 6: Open product details
    second_product.click()

    # Step 7: Get product price
    product_price = page.locator(
        '[data-test="unit-price"]'
    ).inner_text().strip()

    print("Product price:", product_price)

    # Step 8: Click Add to Cart
    add_to_cart_button = page.locator(
        '[data-test="add-to-cart"]'
    )

    expect(add_to_cart_button).to_be_visible()
    expect(add_to_cart_button).to_be_enabled()

    add_to_cart_button.click()

    # Step 9: Open shopping cart
    cart_link = page.locator(
        '[data-test="nav-cart"]'
    )

    expect(cart_link).to_be_visible()
    cart_link.click()

    # Step 10: Verify product name in cart
    expect(
        page.locator('[data-test="product-title"]')
    ).to_have_text(product_name, timeout=15000)

    # Step 11: Verify product quantity
    expect(
        page.locator('[data-test="product-quantity"]')
    ).to_have_value("1")

    # Step 12: Verify product price
    expect(
        page.locator('[data-test="product-price"]')
    ).to_contain_text(product_price)

    # Step 13: Capture evidence before checking line total
    take_bug_screenshot(
        page,
        shop_base_url,
        "cart-incorrect-line-total.png"
    )

    # Step 14: Verify line total
    expect(
        page.locator('[data-test="line-price"]')
    ).to_contain_text(product_price)

    # Step 15: Verify cart total
    expect(
        page.locator('[data-test="cart-total"]')
    ).to_contain_text(product_price)

    print("\nCart contents verified successfully!")
    print("Product:", product_name)
    print("Quantity: 1")
    print("Price:", product_price)


def test_add_to_cart_success_notification(page, shop_base_url):

    # Step 1: Open Toolshop homepage
    shop_url = f"{shop_base_url.rstrip('/')}/#/"
    page.goto(
        shop_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Step 2: Locate product cards
    product_cards = page.locator(
        'a[data-test^="product-"]'
    )

    # Step 3: Wait for products
    product_cards.first.wait_for(
        state="visible",
        timeout=30000
    )

    # Step 4: Select the second product
    second_product = product_cards.nth(1)

    # Step 5: Open product details
    second_product.click()

    # Step 6: Locate Add to Cart button
    add_to_cart_button = page.locator(
        '[data-test="add-to-cart"]'
    )

    expect(add_to_cart_button).to_be_visible()
    expect(add_to_cart_button).to_be_enabled()

    # Step 7: Click Add to Cart
    add_to_cart_button.click()

    # Step 8: Capture evidence on the bug website
    take_bug_screenshot(
        page,
        shop_base_url,
        "cart-missing-success-notification.png"
    )

    # Step 9: Verify success notification
    expect(
        page.get_by_text(
            "Product added to shopping cart.",
            exact=True
        )
    ).to_be_visible(timeout=10000)

    print("\nAdd to Cart success notification verified!")
