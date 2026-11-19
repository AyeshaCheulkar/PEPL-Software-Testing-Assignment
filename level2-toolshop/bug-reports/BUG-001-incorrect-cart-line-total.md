# BUG-001: Incorrect Product Line Total in Shopping Cart

**Severity:** High

**Module:** Shopping Cart

**Environment:** Bug Build – Toolshop

**Test Data:**
- Product: Pliers
- Unit Price: $12.01
- Quantity: 1

### Steps to Reproduce
1. Open the Toolshop bug website.
2. Select the Pliers product.
3. Click Add to Cart.
4. Open the shopping cart.
5. Check the individual product line total.

### Expected Result
The individual line total should be $12.01 (unit price × quantity).

### Actual Result
The individual line total displays $00.00 instead of $12.01.

### Evidence
`../screenshots/cart-incorrect-line-total.png`

### Why It Matters
Customers may see an incorrect product amount in their cart, causing confusion and reducing trust in the checkout process.