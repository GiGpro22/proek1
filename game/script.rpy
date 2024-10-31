# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры. c
define l = Character('Луффи', color="#B31200")
define n = Character('Нами', color = "#D46C22")
define k = Character ('Кайдо', color = "#0B7818")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    $ left2 = Position (xalign=0.2, yalign=1.1)
    $ rigt2 = Position (xalign=0.8, yalign=1.1)

# Игра начинается здесь:
label start:

    scene  bg korab

    "Соломенная шляпа продолжает своё приключение в поисках One piece!"

    show luf obch 

    l "Эй, ребята, в путь на осторв Онигасима!"

    l "По какому пути нам плыть?"

    hide luf obch
    
    show nam

    n "У нас есть два пути: либо безопасный и длиный, либо короткий, но опасный."

    n "Ну что, Капитан!"

    hide nam
    menu:
        "Что делать?"

        "Плыть по длинному пути":
            jump dlinn

        "Плыть по короткому пути":
            jump korotk

    return

label dlinn:
    scene bg onig
    with fade

    "Спустя некоторе время Мугивара и его команда доплывают до острова Онигасима!"

    "После чего начинают искать карту сокровищ"
    show nam

    n "Нам надо разделиться"
    n "Кто-то должен искать карту в горах, а кто-то в деревне"

    hide nam 
    menu:
        "А что выберишь ты?"

        "Искать в горах":
            jump gor

        "Искать в деревне":
            jump der


    return

label gor:
    scene bg onig
    show luf obch
    l "Я что-то нашел"

    l "ОГО, карта!"

    hide luf obch

    "После чего Луффи и его команда нашли One piece"

    "И пожелали всем счастливой жизни"

    scene konec

    "Продолжение следует..."

    return

label der:
    scene bg der
    "Луффи продрлжает искать карту сокровищь"

    show kaid obch

    k "Ах! Ах! Не уже ли вы думали найти в деревне драгоценное сокровище!"

    k "ЛУФФИ!!!" 

    hide kaid obch

    show luf obch 
    "Кайдо!!!"    

    hide luf obch

    scene konec

    "Встеча с ёнко, прожолжение следует"

    return



label korotk: #поменять картинки
    scene bg onig
    with fade

    "Спустя некоторе время Мугивара и его команда доплывают до остова Онигасима!"

    "Где находят ту самую крату скоровищ One piece!"

    "Но в ту же секунду встречают ёнко Кайдо!"

    show kaid obch at rigt2
    k "Ах! Ах! Ах! Не уже ли вы думали так просто получить настолько драгоценное сокровище!"

    k "ЛУФФИ!!!" 

    hide kaid obch

    show luf zl at left2
    "Кайдо!!!"    

    hide luf zl
    menu:
        "Выюерите какой гир будет использовать Луффи для сражения с Кайдо?"

        "2 ГИР":
            jump two

        "4 ГИР":
            jump four

        "5 ГИР":
            jump five
    return

label two:
    scene bg onig
    with fade

    show luf2gr
    with dissolve
    l "Втарой Гир."

    l "Нападай Кайдо!"

    hide luf2gr

    show kaid ud
    k "Раскат грома!"

    hide kaid ud


    scene crag
    with fade

    "Луффи проиграл("

    scene konec

    "Конец"

    return


label four:
    scene bg onig
    with fade

    show luf4gr
    with dissolve
    l "Четвертый Гир."

    l "Нападай Кайдо!"

    hide luf4gr

    show kaid ud
    k "Раскат грома!"

    hide kaid ud


    scene crag
    with fade

    "Луффи проиграл("

    scene konec

    "Конец"

    return

label five:
    scene bg onig
    with fade

    show luf5gr
    with dissolve
    l "Пятый Гир."

    l "ХАХПХПХПХ"

    hide luf5gr

    show kaid ud
    k "Луффи!"
    k "Раскат грома"

    hide kaid ud


    scene konec1
    with fade

    "Луффи победил)"

    scene konec

    "Конец"

    return