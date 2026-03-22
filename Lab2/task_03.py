# 3.	Отображение многомерной (не менее пяти уровней)
# структуры в браузере таким образом, что чтобы элементы
# первого уровня отображались красным цветом, второго – синим,
# третьего – зелёным, четвёртого – фиолетовым, пятого и далее – жёлтым.


def generate_static_html():
    """Generates a static HTML page with a multidimensional structure (no JS)"""

    # Recursive function to generate HTML tree
    def generate_tree(data, level=1):

        # <ul> creates an unordered list with custom styles
        # list-style-type: none removes bullet points
        # padding-left adds indentation for nested levels
        html_tree = '<ul style="list-style-type: none; padding-left: 20px;">\n'

        # Colors for different nesting levels
        colors = {
            1: '#ff4444',  # Red - level 1
            2: '#4444ff',  # Blue - level 2
            3: '#44ff44',  # Green - level 3
            4: '#aa44ff',  # Purple - level 4
        }

        for key, value in data.items():
            color = colors.get(level, '#ffdd44')  # Yellow for level 5+
            text_color = 'white' if level <= 2 or level == 4 else '#333'

            # <li> creates a list item
            # margin adds spacing between items
            html_tree += f'<li style="margin: 5px 0;">'

            # <div> creates a container block for each node
            # background-color sets the node's background
            # color sets text color
            # padding adds internal spacing
            # border-radius rounds the corners
            # display: inline-block makes the block width fit content
            # min-width ensures minimum width for consistency
            html_tree += f'<div style="background-color: {color}; color: {text_color}; padding: 8px 12px; '
            html_tree += f'border-radius: 5px; display: inline-block; min-width: 200px;">'

            # <strong> makes the key text bold
            html_tree += f'<strong>{key}</strong>'

            # <span> creates an inline container for the level indicator
            # float: right positions the text to the right
            # font-size adjusts text size
            # opacity adds transparency
            html_tree += f'<span style="float: right; font-size: 11px; opacity: 0.8;">'
            html_tree += f'Level {level}</span>'
            html_tree += f'</div>'

            # Recursively process children if they exist
            if 'children' in value and value['children']:
                html_tree += generate_tree(value['children'], level + 1)

            html_tree += f'</li>\n'

        html_tree += '</ul>\n'
        return html_tree

    # Data structure (more than 5 levels)
    structure = {
        "Red": {
            "children": {
                "Blue": {
                    "children": {
                        "Green": {
                            "children": {
                                "Purple": {
                                    "children": {
                                        "Yellow": {
                                            "children": {
                                                "Yellow": {
                                                    "children": {
                                                        "Yellow": {
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

    # Main HTML document structure
    # <html> is the root element
    # <body> contains visible page content
    # <div class="container"> creates a container div (class for potential CSS styling)
    # <h1> defines a top-level heading
    html_content = f"""<!DOCTYPE html>
<html>
<body>
    <div class="container">
        <h1>📊 Multi-dimensional structure (5+ levels)</h1>
        {generate_tree(structure)}

    </div>
</body>
</html>"""

    return html_content


if __name__ == "__main__":
    html_output = generate_static_html()

    # Open file in write mode with UTF-8 encoding
    # 'w' mode creates a new file or overwrites existing one
    # encoding='utf-8' ensures proper character handling
    with open("multidimensional_static.html", "w", encoding="utf-8") as f:
        f.write(html_output)

    print("✅ Static HTML page created: multidimensional_static.html")
    print("📊 Structure contains 7+ levels of nesting")
