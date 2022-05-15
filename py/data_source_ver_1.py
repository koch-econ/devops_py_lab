from traceback import print_tb


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
    

# text = """## {model}
# :::::::::::::: {.columns}
# ::: {.column }
# * вендор: {vendor}
# * модель: {model}
# * артикул: {product_id}
# * цена: {price}
# :::
# ::: {.column }

# ![фото товара](pic/{product_id}.png){width=120px}
# :::
# ::::::::::::::

# * * *    
  
# """

# mm=get_products()
# print(get_categories())
# for i in mm:
#     # print (dict(i)['productid'])
#     pr = i['productid']
#     ven = i['vendor']
#     mod = i['model']
#     price = i['price']
#     columns = '{.columns}'
#     column='{.column }'
#     # print (i['productid'])
#     # print (pr, ven, mod, price)
#     text2 = text.replace('{.columns}', '.columns').\
#     replace('{.column }', '.column').\
#     replace('{width=120px}','width=120px').\
#     format(product_id=pr, vendor=ven, model=mod, price=price).\
#     replace('.columns', '{.columns}').\
#     replace('.column', '{.column }').\
#     replace('width=120px','{width=120px}')
    
#     print(text2)

