# import data_source_ver_N as ds
import markdown2output_ver_1 as m2o

tmpl_category_file="tmpl/category_ver_1.md"
tmpl_slides_file="tmpl/slides_ver_1.md"

out_md_file="out/slides_ver_1.md"
out_pptx_file="out/slides_ver_1.pptx"

# объединить файлы в один в директории out 
with open(tmpl_slides_file, 'r') as slide_md:
    slides=slide_md.read()
with open(tmpl_category_file, 'r') as cat_md:
    titul=cat_md.read()

with open(out_md_file, 'w+') as splitfile:
    splitfile.write(titul+slides)

m2o.convert_to_pptx(out_md_file, out_pptx_file)  # преобразовать в pptx 

