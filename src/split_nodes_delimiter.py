from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
        else:
            content = node.text.split(delimiter)
            if len(content) % 2 == 0:
                raise Exception("invalid Markdown syntax")
            for i in range(len(content)):
                if content[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(content[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(content[i], text_type))
    
    return split_nodes

