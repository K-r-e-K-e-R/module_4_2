def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов функции inner_function внутри test_function
    inner_function()


# Вызов test_function
test_function()

# Попытка вызвать inner_function вне test_function
inner_function()
