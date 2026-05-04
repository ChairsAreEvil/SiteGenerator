import unittest

from textnode import *
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNode(unittest.TestCase):
    def test_bold_split(self):
        node = TextNode("This should be **bold**",TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, [TextNode("This should be ", TextType.TEXT), TextNode("bold", TextType.BOLD)])

    def test_bold_split_multi(self):
        node = TextNode("This should be **bold** and also **this**",TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, [TextNode("This should be ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" and also ", TextType.TEXT), TextNode("this", TextType.BOLD)])

    def test_italic_split(self):
        node = TextNode("This should be _italic_",TextType.TEXT)
        split_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(split_node, [TextNode("This should be ", TextType.TEXT), TextNode("italic", TextType.ITALIC)])

    def test_code_split(self):
        node = TextNode("This should be a `code block`",TextType.TEXT)
        split_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(split_node, [TextNode("This should be a ", TextType.TEXT), TextNode("code block", TextType.CODE)])

    def test_not_text_type(self):
        node = TextNode("This text _is_ bold", TextType.BOLD)
        split_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(split_node, [node])

    def test_unbalanced_delimiter(self):
        node = TextNode("This should be **bold", TextType.TEXT)
        with self.assertRaisesRegex(Exception, "invalid Markdown syntax"):
            split_nodes_delimiter([node], "**", TextType.BOLD)
