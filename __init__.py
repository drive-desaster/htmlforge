#!/usr/bin/python3
"""A Python Module to generate HTML Code programatically"""

from __future__ import annotations
import html


class HTMLElement:
    """
    Represents a generic HTML element.
    """

    def __init__(self, tag_name: str, attributes: dict[str, str] = None, children: list[str | HTMLElement] = None) -> None:
        """
        Initialize an HTMLElement.

        :param tag_name: Name of the HTML tag.
        :param attributes: Dictionary of attributes for the tag.
        :param children: List of child elements or strings.
        """
        self.tag_name = tag_name
        self.attributes = attributes or {}
        self.children = children or []

    def add_element(self, element: str | HTMLElement) -> None:
        """
        Add a child element to the current element.

        :param element: The child element to add.
        """
        self.children.append(element)

    def remove_element(self, element: str | HTMLElement) -> None:
        """
        Remove a child element from the current element.

        :param element: The child element to remove.
        """
        if element in self.children:
            self.children.remove(element)

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
        attributes_str = "".join(f' {key}="{html.escape(value)}"' for key, value in self.attributes.items())
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
