from textnode import *
from htmlnode import *

def main():
    text_node = TextNode("this is some text", TextType.BOLD)
    html_node = node = HTMLNode("p","This is a html node", None, {"href": "https://www.google.com","target": "_blank",})
    print(text_node)
    print(html_node)
    print(html_node.props_to_html())

main()