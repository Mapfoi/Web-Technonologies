# 3.	Отображение многомерной (не менее пяти уровней)
# структуры в браузере таким образом, что чтобы элементы
# первого уровня отображались красным цветом, второго – синим,
# третьего – зелёным, четвёртого – фиолетовым, пятого и далее – жёлтым.

import sys


def generate_static_html():
    """Генерирует статическую HTML-страницу с многомерной структурой (без JS)"""

    # Рекурсивная функция для генерации HTML дерева
    def generate_tree(data, level=1):
        html = '<ul style="list-style-type: none; padding-left: 20px;">\n'

        # Цвета для разных уровней
        colors = {
            1: '#ff4444',  # Красный
            2: '#4444ff',  # Синий
            3: '#44ff44',  # Зеленый
            4: '#aa44ff',  # Фиолетовый
        }

        for key, value in data.items():
            color = colors.get(level, '#ffdd44')  # Для 5+ уровня - желтый
            text_color = 'white' if level <= 2 or level == 4 else '#333'

            html += f'<li style="margin: 5px 0;">'
            html += f'<div style="background-color: {color}; color: {text_color}; padding: 8px 12px; '
            html += f'border-radius: 5px; display: inline-block; min-width: 200px;">'
            html += f'<strong>{key}</strong>'
            html += f'<span style="float: right; font-size: 11px; opacity: 0.8;">'
            html += f'Уровень {level}</span>'
            html += f'</div>'

            if 'children' in value and value['children']:
                html += generate_tree(value['children'], level + 1)

            html += f'</li>\n'

        html += '</ul>\n'
        return html

    # Структура данных (более 5 уровней)
    structure = {
        "Красный": {
            "children": {
                "Синий": {
                    "children": {
                        "Зеленый": {
                            "children": {
                                "Фиолетовый": {
                                    "children": {
                                        "Желтый": {
                                            "children": {
                                                "Желтый": {
                                                    "children": {
                                                        "Желтый": {
                                                            "children": {}
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    html = f"""<!DOCTYPE html>
<html>
<body>
    <div class="container">
        <h1>📊 Многомерная структура (5+ уровней)</h1>
        {generate_tree(structure)}
        
    </div>
</body>
</html>"""

    return html


def count_levels(data, current_level=1):
    """Подсчет максимального уровня вложенности"""
    max_level = current_level

    for value in data.values():
        if 'children' in value and value['children']:
            child_level = count_levels(value['children'], current_level + 1)
            max_level = max(max_level, child_level)

    return max_level


if __name__ == "__main__":
    html_content = generate_static_html()

    with open("multidimensional_static.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Статическая HTML-страница создана: multidimensional_static.html")
    print("📊 Структура содержит 7+ уровней вложенности")
