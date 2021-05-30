def simple_coroutine():
    print("coroutine has been started!")
    x = yield
    print("coroutine received: ", x)

cr = simple_coroutine()
cr
next(cr)
cr.send("Hi")

