def test_homepage_loads(page, shop_base_url):
    response = page.goto(shop_base_url)
    # Verify successful HTTP response
    assert response is not None
    assert response.status == 200
    # Verify that the application is visible
    assert page.locator("app-root").is_visible()
