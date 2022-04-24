# Практическое задание по курсам Python 

Получить программу на Python создающую по шаблону на языке Markdown презентацию Powerpoint c фотографиями и характеристиками товаров

Цель задания:

* Создать программу, состоящую из нескольких модулей 
* Развивать проект от простого сложного
* Использовать функции-заглушки (stab) на начальном этапе разработки 
* Дать возможность слушателям с разными уровнями владения Python довести приложение до подходящего для них уровня сложности.

* Практически использовать возможности Python:
    - запуск внешней команды (модуль subprocess)
    - генераторные функции
    - словари
    - lambda-выражения и передача параметров-функций
    - строковые методы, str.format_map
    - запись и чтение из файлов
    - csv - файлы
    - работа с базами данных
    
Не обязательно делать все этапы задания:

Будем считать. что практика по вводному курсу пройдена если сделаны версии до 3й

А по второму курсу, если до версии 5

    

## Предварительное скачивание файлов лабораторной работы

1) Установите систему контроля версий git. Сайт программы  <https://git-scm.com>
2) Загрузите папку проекта из [репозитория github](https://github.com/koch-econ/devops_py_lab.git)

> Можно скопировать репозитарий в папку  `mylab` следующей командой: 
```bash
git clone https://github.com/koch-econ/devops_py_lab.git mylab
```
3) рассмотрите структуру папки проекта

| папка / файл                        | описание                                                 |
|:------------------------------------|:---------------------------------------------------------|
| sh                                  | примеры решения сходных задач на bash                    |
| py                                  | файлы python                                             |
| py/\*\_ver\_1.py                    | заготовки файлов для версии 1 проекта                    |
| py/data_source\_ver\_*N*.py         | модуль функций получения данных для версии *N* проекта   |
| py/main\_ver\_*N*.py                | основная программа                                       |
| py/markdown2output\_ver\_*N*.py     | преобразование в выходной формат (.pptx)                 |
| pic                                 | файлы картинок                                           |
| pic/*product_id*.png                | фотография товара с артикулом *product_id*.png           |
| tmpl                                | шаблоны презентаций  в формате Markdown                                    |
| csv                                 | текстовые файлы данных с разделителем полей `';'`        |
| csv/wb_dquotes.csv                  | все поля закавычены `"`                                  |
| csv/wb.csv                          | все текстовые фоля закавычены `"`                        |
| csv/wb_wo_dquotes.csv               | все поля без кавычек                                     |
| out                                 | папка для сгенерированных программой файлов              |
| out/slides\_ver\_*N*.md             | файлы, сгенерированные программой Вашей программой       |
| out/slides_obrazec\_ver\_*N*.md     | образцы файлов, которые нужно сгенерировать              |
| out/slides_obrazec\_ver\_*N*.pptx   | образцы файлов, которые нужно сгенерировать              |
| out/slides_obrazec\_ver\_*N*.html   | образцы файлов, которые нужно сгенерировать              |
| out/slides\_ver\_*N*.pptx           | файлы, сгенерированные программой Вашей программой       |
| out/slides\_ver\_*N*.html           | файлы, сгенерированные программой Вашей программой       |
| out/slides_obrazec\_ver\_*N*.md     | папка для сгенерированных программой файлов              |

* * *


```python
%%file csv/wb.csv
"product_id";"vendor";"model";"price";"category"
13883932;"StarWind";"Мини-печь smo2003";5597;5
8483040;"BBK";"Микроволновая печь соло 20MWS-711M/WS";4173;5
65374769;"ATLANT";"Холодильник Минск ХМ 4012 022";30000;6
70598275;"Candy";"Стиральная машина CS4 1061DB1/2-07";22941;6
```

    Overwriting csv/wb.csv



```python
%%file csv/wb_wo_dquotes.csv
product_id;vendor;model;price;category
13883932;StarWind;Мини-печь smo2003;5597;5
8483040;BBK;Микроволновая печь соло 20MWS-711M/WS;4173;5
65374769;ATLANT;Холодильник Минск ХМ 4012 022;30000;6
70598275;Candy;Стиральная машина CS4 1061DB1/2-07;22941;6
```

    Overwriting csv/wb_wo_dquotes.csv



```python
%%file csv/wb_dquotes.csv
"product_id";"vendor";"model";"price";"category"
"13883932";"StarWind";"Мини-печь smo2003";"5597";"5"
"8483040";"BBK";"Микроволновая печь соло 20MWS-711M/WS";"4173";"5"
"65374769";"ATLANT";"Холодильник Минск ХМ 4012 022";"30000";"6"
"70598275";"Candy";"Стиральная машина CS4 1061DB1/2-07";"22941";"6"
```

    Overwriting csv/wb_dquotes.csv



```python
%ls pic
```

    13883932.png     70598275.png     category_5.jpeg
    65374769.png     8483040.png      category_6.jpeg



```python
mkdir tmpl
```


```python
%%file tmpl/category_ver_1.md

## Техника для кухни

![](pic/category_5.jpeg)

* * * 

```

    Overwriting tmpl/category_ver_1.md



```python
%%file tmpl/category_ver_4.md

## Техника для кухни

![](pic/{category_name}.jpeg)

* * * 

```

    Writing tmpl/category_ver_4.md



```python
%%file tmpl/slides_ver_1.md
## мини-печь StarWind
:::::::::::::: {.columns}
::: {.column }
* вендор: StarWind
* модель: Мини-печь smo2003
* артикул: 13883932
* цена: 5597
:::
::: {.column }

![фото товара](pic/13883932.png){width=120px}
:::
::::::::::::::

## Микроволновая печь соло 20MWS-711M/WS
:::::::::::::: {.columns}
::: {.column }
* вендор: BBK
* модель: Микроволновая печь соло 20MWS-711M/WS
* артикул: 8483040
* цена: 4173
:::
::: {.column }

![фото товара](pic/8483040.png){width=120px}
:::
::::::::::::::    

```

    Overwriting tmpl/slides_ver_1.md



```python
%%file tmpl/slides_ver_2.md
## {model}
:::::::::::::: {.columns}
::: {.column }
* вендор: {vendor}
* модель: {model}
* артикул: {product_id}
* цена: {price}
:::
::: {.column }

![фото товара](pic/{product_id}.png){width=120px}
:::
::::::::::::::

* * *    
```

    Overwriting tmpl/slides_ver_2.md



```python
%ls out
```

    slides_obrazec_ver_1.html  slides_ver_1.pptx



```python
!pandoc -o out/slides_obrazec_ver_1.html --self-contained --metadata title="товары WB"   tmpl/category_ver_1.md tmpl/slides_ver_1.md
```

```sh
pandoc -o out/slides_obrazec_ver1.html --self-contained --metadata title="товары WB"   template/category_ver_1.md template/slides_ver_1.md
```

Результат [html](out/slides_obrazec_ver_1.html)


```python
!pandoc -o out/slides_ver_1.pptx  tmpl/category_ver_1.md tmpl/slides_ver_1.md
```

```sh
pandoc -o out/slides_ver_1.pptx  template/category_ver_1.md template/slides_ver_1.md
```

Результат [pptx](out/slides_obrazec_ver_1.pptx)


```python
%ls out
```

    slides_obrazec_ver1.html  slides_ver_1.pptx


## Предполагаемые этапы (версии развития проекта)

###  Версия 1. Генерация pptx по готовым файлам `tmpl/*_ver_1.md'


```python
%%file py/main_ver_1.py
# import data_source_ver_N as ds
import markdown2output_ver_1.py  as m2o


tmpl_category_file="tmpl/category_ver_1.md"
tmpl_slides_file="tmpl/slides_ver_1.md"

out_md_file="out/slides_ver_1.md"
out_pptx_file="out/slides_ver_1.md"

pass # объединить файлы в один в директории out 

m2o.convert_to_pptx(out_md_file, out_pptx_file)  # преобразовать в pptx 


```

    Writing py/main_ver_1.py


###  Версия 2. Генерация pptx по файлам `tmpl/*_ver_2.md' c подставлением данных из модуля `data_source_ver_2.py`

Пока без титульных слайдов категорий товаров



###  Версия 3. Генерация pptx по файлам `tmpl/*_ver_3.md' c подставлением данных из словаря discout_dict и списка category_list


```python

category_list=["Прочие устройтсва", "Климатическая техника" "Красота и здоровье", "Садовая техника","Техника для дома","Техника для кухни", "Крупная бытовая техника" ]

```

Скидки на все товары этих вендоров


```python
discount_dict={ "Candy":10, "BBK":20 }
```


```python
%%file tmpl/slides_ver_3.md
## {model}
:::::::::::::: {.columns}
::: {.column }
* вендор: {vendor}
* модель: {model}
* артикул: {product_id}
* цена: {price}
* окончательная цена: ${discounted_price}
* скидка по акции: ${discout}%
:::
::: {.column }

![фото товара](pic/{product_id}.png){width=120px}
:::
::::::::::::::

* * * 

```

    Writing tmpl/slides_ver_3.md


###  Версия 4. Слайды должны быть упорядочены по названиям категории товаров и дополнены титульными слайдами tmpl/category_ver_4.md

###  Версия 5. Генераторные функции должны читать данные из csv файла csv/wb.csv

