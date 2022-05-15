# tmpl_category_file="c:/do/python/mylab/test1/category_ver_1.md"
# tmpl_slides_file="c:/do/python/mylab/test1/slides_ver_1.md"

tmpl_category_file="test1/category_ver_1.md"
tmpl_slides_file="test1/slides_ver_1.md"

out_md_file="slides_ver_1.md"
out_pptx_file="slides_ver_1.md"

with open(tmpl_slides_file, 'r') as slide_md:
    slides=slide_md.read()
with open(tmpl_category_file, 'r') as cat_md:
    titul=cat_md.read()

with open('test1/newfile.md', 'w+') as n:
    n.write(titul+slides)
    