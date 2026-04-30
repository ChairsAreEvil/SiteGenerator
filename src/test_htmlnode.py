import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "click me",
            None,
            {"href": "https://www.google.com","target": "_blank",}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_props_to_html_single_prop(self):
        node = HTMLNode(
            "a",
            "click me",
            None,
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com"',
        )

    def test_props_none(self):
        node = HTMLNode("p", "Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_empty(self):
        node = HTMLNode("p", "Hello", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "Hello", None, {"class": "primary"})
        self.assertEqual(
            repr(node),
            "HTMLNode(p, Hello, None, {'class': 'primary'})",
        )

    def test_to_html_raises(self):
        node = HTMLNode("p", "Hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_children(self):
        child = HTMLNode("span", "child")
        parent = HTMLNode("div", None, [child])
        self.assertEqual(parent.children[0], child)

if __name__ == "__main__":
    unittest.main()