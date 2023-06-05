import test_addToCartWithVariant

if __name__ == "__main__":
    addProduct = test_addToCartWithVariant.TestAddToCartWithVariant()

    addProduct.setup_method("")
    addProduct.test_addToCartWithVariant()
    addProduct.teardown_method("")
