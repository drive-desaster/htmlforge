#!/usr/bin/python3
"""A Python Module to generate HTML Code programatically"""

from __future__ import annotations
import html


class HTMLElement:
    """
    Represents a generic HTML element.
    """

    def __init__(self, tag_name: str, attributes: dict[str, str] = None, children: list[str | tuple[str, str] | HTMLElement] = None) -> None:
        """
        Initialize an HTMLElement.

        :param tag_name: Name of the HTML tag.
        :param attributes: Dictionary of attributes for the tag.
        :param children: List of child elements or strings. Each child can be:
                         - A plain string (which will be neither escaped nor obfuscated).
                         - A tuple with the string and a flag indicating whether to escape or obfuscate.
        """
        self.tag_name = tag_name
        self.attributes = attributes or {}
        self.children = []
        for child in children:
            if isinstance(child, tuple):
                text, flag = child
                if flag == "escape":
                    text = self._escape_html(text)
                elif flag == "obfuscate":
                    text = self._escape_html(text)
                    text = self._escape_html(text, obfuscate=True)
                self.children.append(text)
            else:
                self.children.append(child)

    @staticmethod
    def _escape_html(text: str, obfuscate: bool = False) -> str:
        """
        Escape special characters in the given text to their HTML entities or obfuscate the text.

        :param text: The text string to escape or obfuscate.
        :param obfuscate: If True, the text will be obfuscated by converting each character to its corresponding HTML character code.
                          If False (default), the text will be HTML-escaped to convert special characters to their HTML entities.
        :return: Either the HTML-escaped or obfuscated string, based on the obfuscate parameter.
        """
        if obfuscate:
            return "".join(f"&#{ord(char)};" for char in text)
        else:
            return html.escape(text)

    def add_child(self, child: str | HTMLElement, escape: bool = True, obfuscate: bool = False) -> None:
        """
        Add a child (text or element) to the current element.

        :param child: The child (text or element) to add.
        :param escape: If True (default), and the child is text, it will be HTML-escaped.
        :param obfuscate: If True, and the child is text, it will be obfuscatedby converting each character to its corresponding HTML character code.
                          This can be used to hide the text from simple text scraping methods.
                          Note: Obfuscation will only occur if escape is also True.
        :raises ValueError: If escape is False and obfuscate is True.
        """
        if isinstance(child, str):
            if escape:
                child = self._escape_html(child)
                if obfuscate:
                    child = self._escape_html(child, obfuscate=True)
            elif obfuscate:
                raise ValueError("Cannot obfuscate text without escaping it first.")
        self.children.append(child)

    def remove_child(self, element: str | HTMLElement) -> None:
        """
        Remove a child element from the current element.

        :param element: The child element to remove.
        """
        if element in self.children:
            self.children.remove(element)
        elif isinstance(element, str):
            if self._escape_html(element) in self.children:
                self.children.remove(self._escape_html(element))
            elif self._escape_html(element, obfuscate=True) in self.children:
                self.children.remove(self._escape_html(element, obfuscate=True))

    def set_attribute(self, key: str, value: str) -> None:
        """
        Set an attribute for the current element.

        :param key: The attribute name.
        :param value: The attribute value.
        """
        self.attributes[key] = value

    def get_attribute(self, key: str) -> str:
        """
        Get the value of an attribute for the current element.

        :param key: The attribute name.
        :return: The attribute value.
        """
        return self.attributes.get(key, "")

    def __str__(self) -> str:
        """
        Convert the element to its HTML string representation.

        :return: HTML string representation of the element.
        """
        attributes_str = "".join(f' {key}="{self._escape_html(value)}"' for key, value in self.attributes.items())
        children_str = " ".join(str(child) for child in self.children)
        return f'<{self.tag_name}{attributes_str}>{children_str}</{self.tag_name}>'

    def __repr__(self) -> str:
        """
        Developer-friendly representation of the object.

        :return: String representation of the object.
        """
        return f"{self.__class__.__name__}(attributes={self.attributes!r}, children={self.children!r})"


class Html(HTMLElement):
    """
    Represents the <html> element.
    """

    def __init__(self, attributes: dict[str, str] = None, children: list[str | HTMLElement] = None) -> None:
        """
        Initialize an Html element.

        :param attributes: Dictionary of attributes for the tag.
        :param children: List of child elements or strings.
        """
        super().__init__("html", attributes, children)

    def __str__(self) -> str:
        """
        Convert the Html element to its HTML string representation with DOCTYPE.

        :return: HTML string representation of the Html element with DOCTYPE.
        """
        doctype = '<!DOCTYPE html>'
        return f'{doctype}\n{super().__str__()}'


class Body(HTMLElement):
    """
    Represents the <body> element.
    """

    def __init__(self, attributes: dict[str, str] = None, children: list[str | HTMLElement] = None) -> None:
        """
        Initialize a Body element.

        :param attributes: Dictionary of attributes for the tag.
        :param children: List of child elements or strings.
        """
        super().__init__("body", attributes, children)


class Div(HTMLElement):
    """
    Represents the <div> element.
    """

    def __init__(self, attributes: dict[str, str] = None, children: list[str | HTMLElement] = None) -> None:
        """
        Initialize a Div element.

        :param attributes: Dictionary of attributes for the tag.
        :param children: List of child elements or strings.
        """
        super().__init__("div", attributes, children)


class P(HTMLElement):
    """
    Represents the <p> element.
    """

    def __init__(self, attributes: dict[str, str] = None, children: list[str | HTMLElement] = None) -> None:
        """
        Initialize a P (paragraph) element.

        :param attributes: Dictionary of attributes for the tag.
        :param children: List of child elements or strings.
        """
        super().__init__("p", attributes, children)


class Img(HTMLElement):
    """
    Represents the <img> element.
    """

    def __init__(self, attributes: dict[str, str]) -> None:
        """
        Initialize an Img (image) element.

        :param attributes: Dictionary of attributes for the tag.
        """
        super().__init__("img", attributes)


class A(HTMLElement):
    """
    Represents the <a> (anchor) element.
    """

    def __init__(self, attributes: dict[str, str] = None, children: list[str | HTMLElement] = None) -> None:
        """
        Initialize an A (anchor) element.

        :param attributes: Dictionary of attributes for the tag.
        :param children: List of child elements or strings.
        """
        super().__init__("a", attributes, children)
