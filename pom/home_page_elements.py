
class HomePage:


    def __init__(self, page):

        self.allow_all_cookies = page.get_by_role("button", name="ALLOW ALL")

        self.sort_item = page.get_by_role("img", name="sort")

        self.product_name_asc = page.locator("li").filter(has_text="Product A-Z")
        self.product_name_desc = page.locator("li").filter(has_text="Product Z-A")

        self.product_price_asc = page.locator("li").filter(has_text="Price Low to High")
        self.product_price_desc = page.locator("li").filter(has_text="Price High to Low")

        self.first_item_default = page.locator("#layer-product-list div").filter(has_text="Tom Kerridge").nth(1)
        self.fist_item_product_name = page.locator("#layer-product-list div").filter(has_text="Aperol Spritz").nth(1)
        self.last_item_product_name = page.locator("#layer-product-list div").filter(has_text="Wolfys Creamy").nth(1)

        self.first_item_price = page.locator("#layer-product-list div").filter(has_text="Scrapples Apple").nth(
        1)
        self.fist_item_price_amount = page.get_by_text("£0.95 / 140 AVIOS")
        self.last_item_price = page.locator("#layer-product-list div").filter(has_text="Pannier Brut NV Champagne").nth(
        1)
        self.last_item_price_amount = page.get_by_text("£17.00 / 2430 AVIOS").first