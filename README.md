<div id="bfe601ef-7327-44a8-9281-bfbbb4a6d67d" class="cell markdown">

# Практическое задание по курсам Python

</div>

<div id="daea0c7a-a6bd-4fa1-876b-8fed15b60e62" class="cell markdown">

Получить программу на Python создающую по шаблону на языке Markdown
презентацию Powerpoint c фотографиями и характеристиками товаров

</div>

<div id="cc8ab672-e75f-4208-a7ef-6edc84e1d660" class="cell markdown">

Цель задания:

-   Создать программу, состоящую из нескольких модулей

-   Развивать проект от простого сложного

-   Использовать функции-заглушки (stab) на начальном этапе разработки

-   Дать возможность слушателям с разными уровнями владения Python
    довести приложение до подходящего для них уровня сложности.

-   Практически использовать возможности Python:

    -   запуск внешней команды (модуль subprocess)
    -   генераторные функции
    -   словари
    -   lambda-выражения и передача параметров-функций
    -   строковые методы, str.format_map
    -   запись и чтение из файлов
    -   csv - файлы
    -   работа с базами данных

Не обязательно делать все этапы задания:

Будем считать. что практика по вводному курсу пройдена если сделаны
версии до 3й

А по второму курсу, если до версии 5

</div>

<div id="60c07340-5b1b-4fdd-a163-02e9bc16eba5" class="cell markdown"
tags="[]">

## Предварительное скачивание файлов лабораторной работы

1\) Установите систему контроля версий git. Сайт программы
<https://git-scm.com> 2) Загрузите папку проекта из [репозитория
github](https://github.com/koch-econ/devops_py_lab.git)

> Можно скопировать репозитарий в папку `mylab` следующей командой:

``` bash
git clone https://github.com/koch-econ/devops_py_lab.git mylab
```

3\) рассмотрите структуру папки проекта

</div>

<div id="525fd835-8970-48f3-a78f-75958045ee41" class="cell markdown">

| папка / файл                     | описание                                               |
|:---------------------------------|:-------------------------------------------------------|
| sh                               | примеры решения сходных задач на bash                  |
| py                               | файлы python                                           |
| py/\*\_ver_1.py                  | заготовки файлов для версии 1 проекта                  |
| py/data_source_ver\_*N*.py       | модуль функций получения данных для версии *N* проекта |
| py/main_ver\_*N*.py              | основная программа                                     |
| py/markdown2output_ver\_*N*.py   | преобразование в выходной формат (.pptx)               |
| pic                              | файлы картинок                                         |
| pic/*product_id*.png             | фотография товара с артикулом *product_id*.png         |
| tmpl                             | шаблоны презентаций в формате Markdown                 |
| csv                              | текстовые файлы данных с разделителем полей `';'`      |
| csv/wb_dquotes.csv               | все поля закавычены `"`                                |
| csv/wb.csv                       | все текстовые фоля закавычены `"`                      |
| csv/wb_wo_dquotes.csv            | все поля без кавычек                                   |
| out                              | папка для сгенерированных программой файлов            |
| out/slides_ver\_*N*.md           | файлы, сгенерированные программой Вашей программой     |
| out/slides_obrazec_ver\_*N*.md   | образцы файлов, которые нужно сгенерировать            |
| out/slides_obrazec_ver\_*N*.pptx | образцы файлов, которые нужно сгенерировать            |
| out/slides_obrazec_ver\_*N*.html | образцы файлов, которые нужно сгенерировать            |
| out/slides_ver\_*N*.pptx         | файлы, сгенерированные программой Вашей программой     |
| out/slides_ver\_*N*.html         | файлы, сгенерированные программой Вашей программой     |
| out/slides_obrazec_ver\_*N*.md   | папка для сгенерированных программой файлов            |

------------------------------------------------------------------------

</div>

<div id="b13212a0-628c-437c-b8bf-68bb735e7d97" class="cell code"
execution_count="17">

``` python
%%file csv/wb.csv
"product_id";"vendor";"model";"price";"category"
13883932;"StarWind";"Мини-печь smo2003";5597;5
8483040;"BBK";"Микроволновая печь соло 20MWS-711M/WS";4173;5
65374769;"ATLANT";"Холодильник Минск ХМ 4012 022";30000;6
70598275;"Candy";"Стиральная машина CS4 1061DB1/2-07";22941;6
```

<div class="output stream stdout">

    Overwriting csv/wb.csv

</div>

</div>

<div id="2cf80d3f-d1c3-47cd-9ddb-65b584c268a6" class="cell code"
execution_count="18">

``` python
%%file csv/wb_wo_dquotes.csv
product_id;vendor;model;price;category
13883932;StarWind;Мини-печь smo2003;5597;5
8483040;BBK;Микроволновая печь соло 20MWS-711M/WS;4173;5
65374769;ATLANT;Холодильник Минск ХМ 4012 022;30000;6
70598275;Candy;Стиральная машина CS4 1061DB1/2-07;22941;6
```

<div class="output stream stdout">

    Overwriting csv/wb_wo_dquotes.csv

</div>

</div>

<div id="1c1c28d4-152f-4705-8cb4-5c9e12b2fb22" class="cell code"
execution_count="19">

``` python
%%file csv/wb_dquotes.csv
"product_id";"vendor";"model";"price";"category"
"13883932";"StarWind";"Мини-печь smo2003";"5597";"5"
"8483040";"BBK";"Микроволновая печь соло 20MWS-711M/WS";"4173";"5"
"65374769";"ATLANT";"Холодильник Минск ХМ 4012 022";"30000";"6"
"70598275";"Candy";"Стиральная машина CS4 1061DB1/2-07";"22941";"6"
```

<div class="output stream stdout">

    Overwriting csv/wb_dquotes.csv

</div>

</div>

<div id="1a803558-f69f-4df0-bae8-ceb6dfe8d426" class="cell code"
execution_count="7">

``` python
%ls pic
```

<div class="output stream stdout">

    13883932.png     70598275.png     category_5.jpeg
    65374769.png     8483040.png      category_6.jpeg

</div>

</div>

<div id="8cb7ce10-5fb0-41b4-a8a3-7345b94f2e70" class="cell code"
execution_count="22">

``` python
mkdir tmpl
```

</div>

<div id="dc18154d-4f47-408a-8b7f-61475d8c3e84" class="cell code"
execution_count="15">

``` python
%%file tmpl/category_ver_1.md

## Техника для кухни

![](pic/category_5.jpeg)

* * * 
```

<div class="output stream stdout">

    Overwriting tmpl/category_ver_1.md

</div>

</div>

<div id="1352e32a-5d93-41bc-90b3-f690cf225e51" class="cell code"
execution_count="36">

``` python
%%file tmpl/category_ver_4.md

## Техника для кухни

![](pic/{category_name}.jpeg)

* * * 
```

<div class="output stream stdout">

    Writing tmpl/category_ver_4.md

</div>

</div>

<div id="78cad381-a805-459d-b307-cad79ee64b6f" class="cell code"
execution_count="29">

``` python
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

<div class="output stream stdout">

    Overwriting tmpl/slides_ver_1.md

</div>

</div>

<div id="079305f0-a33c-40b4-91a8-7dc6d412d5ad" class="cell code"
execution_count="43">

``` python
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

<div class="output stream stdout">

    Overwriting tmpl/slides_ver_2.md

</div>

</div>

<div id="120a99f3-7e3b-43bc-bb83-acaa4b34095a" class="cell code"
execution_count="44">

``` python
%ls out
```

<div class="output stream stdout">

    slides_obrazec_ver_1.html  slides_ver_1.pptx

</div>

</div>

<div id="584534f4-4a91-416b-9987-f4694edcffed" class="cell code"
execution_count="26">

``` python
!pandoc -o out/slides_obrazec_ver_1.html --self-contained --metadata title="товары WB"   tmpl/category_ver_1.md tmpl/slides_ver_1.md
```

</div>

<div id="211c44bc-497d-4d47-8d1b-4bb00e0229a4" class="cell markdown">

``` sh
pandoc -o out/slides_obrazec_ver1.html --self-contained --metadata title="товары WB"   template/category_ver_1.md template/slides_ver_1.md
```

</div>

<div id="609c4489-54e4-43fa-837c-f1a2719def52" class="cell markdown">

Результат [html](out/slides_obrazec_ver_1.html)

</div>

<div id="1a538a32-0871-45f4-aef0-e5ddd840cb5f" class="cell code"
execution_count="24">

``` python
!pandoc -o out/slides_ver_1.pptx  tmpl/category_ver_1.md tmpl/slides_ver_1.md
```

</div>

<div id="f7072ae7-8f77-48cf-9541-85a1f7fc9d0c" class="cell markdown">

``` sh
pandoc -o out/slides_ver_1.pptx  template/category_ver_1.md template/slides_ver_1.md
```

</div>

<div id="2f21bffa-a812-4dd6-98ba-94a77d7de5a2" class="cell markdown">

Результат [pptx](out/slides_obrazec_ver_1.pptx)

</div>

<div id="e627d4dc-db88-4da0-99ad-2b13117b4b2f" class="cell code"
execution_count="25">

``` python
%ls out
```

<div class="output stream stdout">

    slides_obrazec_ver1.html  slides_ver_1.pptx

</div>

</div>

<div id="78f8bd86-eed3-45dc-aa8b-92271323e296" class="cell markdown">

## Предполагаемые этапы (версии развития проекта)

</div>

<div id="02141f6e-99e0-45e5-9aba-eb46b47dfca7" class="cell markdown"
tags="[]">

### Версия 1. Генерация pptx по готовым файлам \`tmpl/\*\_ver_1.md'

</div>

<div id="53cd59cb-6a0f-4f70-802e-934a9de7e04c" class="cell code"
execution_count="38">

``` python
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

<div class="output stream stdout">

    Writing py/main_ver_1.py

</div>

</div>

<div id="23036158-ad89-48af-ab54-76d7c3b29f42" class="cell markdown">

### Версия 2. Генерация pptx по файлам `tmpl/*_ver_2.md' c подставлением данных из модуля`data_source_ver_2.py\`

</div>

<div id="62d5d008-4af7-413e-8c07-c833815d8218" class="cell markdown">

Пока без титульных слайдов категорий товаров

</div>

<div id="dfce8576-deac-4849-ac30-b1f9ecbe9983" class="cell markdown"
tags="[]">

### Версия 3. Генерация pptx по файлам \`tmpl/\*\_ver_3.md' c подставлением данных из словаря discout_dict и списка category_list

</div>

<div id="c74a768d-8adc-45cd-9c97-2af5fa55d5fa" class="cell code"
execution_count="39">

``` python
category_list=["Прочие устройтсва", "Климатическая техника" "Красота и здоровье", "Садовая техника","Техника для дома","Техника для кухни", "Крупная бытовая техника" ]
```

</div>

<div id="f9fba6b0-a279-4cc6-a843-184c40773e1e" class="cell code"
execution_count="48">

``` python
discount_dict={ "Candy":10, "BBK":20 }
```

</div>

<div id="8ce7e928-8590-49cc-b3f6-d830d2bd6c79" class="cell markdown">

Скидки на все товары этих вендоров

[образец html](out/slides_obrazec_ver_3.html)

</div>

<div id="fef87928-5644-4b20-9766-8282a9ab8419" class="cell code"
execution_count="42">

``` python
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

<div class="output stream stdout">

    Writing tmpl/slides_ver_3.md

</div>

</div>

<div id="ab09e34d-112e-4abf-9369-609b330975af" class="cell markdown">

### Версия 4. Слайды должны быть упорядочены по названиям категории товаров и дополнены титульными слайдами tmpl/category_ver_4.md

</div>

<div id="5f8267c1-ed29-4a14-9889-3d52f338a172" class="cell markdown">

### Версия 5. Генераторные функции должны читать данные из csv файла csv/wb.csv

</div>

<div id="b47f38d7-f32d-426b-be89-53091a4aafdd" class="cell code">

``` python
```

</div>
