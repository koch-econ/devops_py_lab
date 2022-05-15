import data_source_ver_1 as ds
import markdown2output_ver_1 as m2o

tmpl_slides_file="tmpl/slides_ver_2.md"

out_md_file="out/slides_ver_2.md"
out_pptx_file="out/slides_ver_2.pptx"

# Генерация файла md out/slides_ver_2.md' c подставлением данных из модуля data_source_ver_2.py 
with open(tmpl_slides_file, 'r', encoding="utf8") as slide_md:
    slides=slide_md.read()

for item in ds.get_products():
    product = item['productid']
    vend = item['vendor']
    model = item['model']
    price = item['price']

    with open(out_md_file,"a+", encoding="utf8")  as fi:
      fi.write(slides.replace('{.columns}', '[.columns]').\
         replace('{.column }', '[.column]').\
         replace('{width=120px}','width=120px').\
        format(product_id=product, vendor=vend, model=model, price=price).\
         replace('[.columns]', '{.columns}').\
         replace('[.column]', '{.column }').\
         replace('width=120px','{width=120px}'))

m2o.convert_to_pptx(out_md_file, out_pptx_file)  # преобразовать в pptx 

