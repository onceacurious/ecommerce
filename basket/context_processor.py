from .basket import Basket


def basket(request):
    # _basket = Basket()
    return {'basket': Basket(request)}
