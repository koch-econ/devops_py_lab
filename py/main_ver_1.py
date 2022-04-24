# import data_source_ver_N as ds
import markdown2output_ver_1.py  as m2o


tmpl_category_file="tmpl/category_ver_1.md"
tmpl_slides_file="tmpl/slides_ver_1.md"

out_md_file="out/slides_ver_1.md"
out_pptx_file="out/slides_ver_1.md"

pass # объединить файлы в один в директории out 

m2o.convert_to_pptx(out_md_file, out_pptx_file)  # преобразовать в pptx 

