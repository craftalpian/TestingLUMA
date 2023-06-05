import test_addToCart

if __name__ == "__main__":
    addProduct = test_addToCart.TestAddToCart()

    addProduct.setup_method("")
    addProduct.test_addToCart()
    addProduct.teardown_method("")
