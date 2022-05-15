#from traceback import print_tb


def get_categories(*args, **kwargs):
    # args and kwargs are for future project development
    yield (1,"Климатическая техника")
    yield (2,"Красота и здоровье")
    yield (3,"Садовая техника")
    yield (4,"Техника для дома")
    yield (5,"Техника для кухни")
    yield (6,"Крупная бытовая техника")

def get_products(*args, **kwargs):
    # args and kwargs are for future project development
    columns="productid;vendor;model;price;category".split(';')
    yield dict(zip(columns,(13883932,"StarWind","Мини-печь smo2003",5597,5)))
    yield dict(zip(columns,(8483040,"BBK","Микроволновая печь соло 20MWS-711M/WS",4173,5)))
    yield dict(zip(columns,(65374769,"ATLANT","Холодильник Минск ХМ 4012 022",30000,6)))
    yield dict(zip(columns,(70598275,"Candy","Стиральная машина CS4 1061DB1/2-07",22941,6)))
