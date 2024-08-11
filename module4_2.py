def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
# inner_function() --- Вызвать данную функцию невозможно из-за того, что она находится в другой области видимости