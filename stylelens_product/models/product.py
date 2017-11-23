# coding: utf-8

"""
    bl-db-product

    This is a API document for Product DB

    OpenAPI spec version: 0.0.1
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Product(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'host_code': 'str',
        'host_url': 'str',
        'host_name': 'str',
        'tags': 'list[str]',
        'class_code': 'str',
        'price': 'int',
        'currency_unit': 'str',
        'product_url': 'str',
        'product_no': 'str',
        'nation': 'str',
        'main_image': 'str',
        'main_image_mobile_full': 'str',
        'main_image_mobile_thumb': 'str',
        'sub_images': 'list[str]',
        'sizes': 'list[str]',
        'discount_rate': 'int',
        'feedback': 'list[Feedback]',
        'version_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'host_code': 'host_code',
        'host_url': 'host_url',
        'host_name': 'host_name',
        'tags': 'tags',
        'class_code': 'class_code',
        'price': 'price',
        'currency_unit': 'currency_unit',
        'product_url': 'product_url',
        'product_no': 'product_no',
        'nation': 'nation',
        'main_image': 'main_image',
        'main_image_mobile_full': 'main_image_mobile_full',
        'main_image_mobile_thumb': 'main_image_mobile_thumb',
        'sub_images': 'sub_images',
        'sizes': 'sizes',
        'discount_rate': 'discount_rate',
        'feedback': 'feedback',
        'version_name': 'version_name'
    }

    def __init__(self, id=None, name=None, host_code=None, host_url=None, host_name=None, tags=None, class_code=None, price=None, currency_unit=None, product_url=None, product_no=None, nation=None, main_image=None, main_image_mobile_full=None, main_image_mobile_thumb=None, sub_images=None, sizes=None, discount_rate=None, feedback=None, version_name=None):
        """
        Product - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._host_code = None
        self._host_url = None
        self._host_name = None
        self._tags = None
        self._class_code = None
        self._price = None
        self._currency_unit = None
        self._product_url = None
        self._product_no = None
        self._nation = None
        self._main_image = None
        self._main_image_mobile_full = None
        self._main_image_mobile_thumb = None
        self._sub_images = None
        self._sizes = None
        self._discount_rate = None
        self._feedback = None
        self._version_name = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if host_code is not None:
          self.host_code = host_code
        if host_url is not None:
          self.host_url = host_url
        if host_name is not None:
          self.host_name = host_name
        if tags is not None:
          self.tags = tags
        if class_code is not None:
          self.class_code = class_code
        if price is not None:
          self.price = price
        if currency_unit is not None:
          self.currency_unit = currency_unit
        if product_url is not None:
          self.product_url = product_url
        if product_no is not None:
          self.product_no = product_no
        if nation is not None:
          self.nation = nation
        if main_image is not None:
          self.main_image = main_image
        if main_image_mobile_full is not None:
          self.main_image_mobile_full = main_image_mobile_full
        if main_image_mobile_thumb is not None:
          self.main_image_mobile_thumb = main_image_mobile_thumb
        if sub_images is not None:
          self.sub_images = sub_images
        if sizes is not None:
          self.sizes = sizes
        if discount_rate is not None:
          self.discount_rate = discount_rate
        if feedback is not None:
          self.feedback = feedback
        if version_name is not None:
          self.version_name = version_name

    @property
    def id(self):
        """
        Gets the id of this Product.

        :return: The id of this Product.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Product.

        :param id: The id of this Product.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Product.

        :return: The name of this Product.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Product.

        :param name: The name of this Product.
        :type: str
        """

        self._name = name

    @property
    def host_code(self):
        """
        Gets the host_code of this Product.

        :return: The host_code of this Product.
        :rtype: str
        """
        return self._host_code

    @host_code.setter
    def host_code(self, host_code):
        """
        Sets the host_code of this Product.

        :param host_code: The host_code of this Product.
        :type: str
        """

        self._host_code = host_code

    @property
    def host_url(self):
        """
        Gets the host_url of this Product.

        :return: The host_url of this Product.
        :rtype: str
        """
        return self._host_url

    @host_url.setter
    def host_url(self, host_url):
        """
        Sets the host_url of this Product.

        :param host_url: The host_url of this Product.
        :type: str
        """

        self._host_url = host_url

    @property
    def host_name(self):
        """
        Gets the host_name of this Product.

        :return: The host_name of this Product.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this Product.

        :param host_name: The host_name of this Product.
        :type: str
        """

        self._host_name = host_name

    @property
    def tags(self):
        """
        Gets the tags of this Product.

        :return: The tags of this Product.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Product.

        :param tags: The tags of this Product.
        :type: list[str]
        """

        self._tags = tags

    @property
    def class_code(self):
        """
        Gets the class_code of this Product.

        :return: The class_code of this Product.
        :rtype: str
        """
        return self._class_code

    @class_code.setter
    def class_code(self, class_code):
        """
        Sets the class_code of this Product.

        :param class_code: The class_code of this Product.
        :type: str
        """

        self._class_code = class_code

    @property
    def price(self):
        """
        Gets the price of this Product.

        :return: The price of this Product.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this Product.

        :param price: The price of this Product.
        :type: int
        """

        self._price = price

    @property
    def currency_unit(self):
        """
        Gets the currency_unit of this Product.

        :return: The currency_unit of this Product.
        :rtype: str
        """
        return self._currency_unit

    @currency_unit.setter
    def currency_unit(self, currency_unit):
        """
        Sets the currency_unit of this Product.

        :param currency_unit: The currency_unit of this Product.
        :type: str
        """

        self._currency_unit = currency_unit

    @property
    def product_url(self):
        """
        Gets the product_url of this Product.

        :return: The product_url of this Product.
        :rtype: str
        """
        return self._product_url

    @product_url.setter
    def product_url(self, product_url):
        """
        Sets the product_url of this Product.

        :param product_url: The product_url of this Product.
        :type: str
        """

        self._product_url = product_url

    @property
    def product_no(self):
        """
        Gets the product_no of this Product.

        :return: The product_no of this Product.
        :rtype: str
        """
        return self._product_no

    @product_no.setter
    def product_no(self, product_no):
        """
        Sets the product_no of this Product.

        :param product_no: The product_no of this Product.
        :type: str
        """

        self._product_no = product_no

    @property
    def nation(self):
        """
        Gets the nation of this Product.

        :return: The nation of this Product.
        :rtype: str
        """
        return self._nation

    @nation.setter
    def nation(self, nation):
        """
        Sets the nation of this Product.

        :param nation: The nation of this Product.
        :type: str
        """

        self._nation = nation

    @property
    def main_image(self):
        """
        Gets the main_image of this Product.
        image url

        :return: The main_image of this Product.
        :rtype: str
        """
        return self._main_image

    @main_image.setter
    def main_image(self, main_image):
        """
        Sets the main_image of this Product.
        image url

        :param main_image: The main_image of this Product.
        :type: str
        """

        self._main_image = main_image

    @property
    def main_image_mobile_full(self):
        """
        Gets the main_image_mobile_full of this Product.
        Mobile full size of image url

        :return: The main_image_mobile_full of this Product.
        :rtype: str
        """
        return self._main_image_mobile_full

    @main_image_mobile_full.setter
    def main_image_mobile_full(self, main_image_mobile_full):
        """
        Sets the main_image_mobile_full of this Product.
        Mobile full size of image url

        :param main_image_mobile_full: The main_image_mobile_full of this Product.
        :type: str
        """

        self._main_image_mobile_full = main_image_mobile_full

    @property
    def main_image_mobile_thumb(self):
        """
        Gets the main_image_mobile_thumb of this Product.
        Mobile thumbnail size of image url

        :return: The main_image_mobile_thumb of this Product.
        :rtype: str
        """
        return self._main_image_mobile_thumb

    @main_image_mobile_thumb.setter
    def main_image_mobile_thumb(self, main_image_mobile_thumb):
        """
        Sets the main_image_mobile_thumb of this Product.
        Mobile thumbnail size of image url

        :param main_image_mobile_thumb: The main_image_mobile_thumb of this Product.
        :type: str
        """

        self._main_image_mobile_thumb = main_image_mobile_thumb

    @property
    def sub_images(self):
        """
        Gets the sub_images of this Product.

        :return: The sub_images of this Product.
        :rtype: list[str]
        """
        return self._sub_images

    @sub_images.setter
    def sub_images(self, sub_images):
        """
        Sets the sub_images of this Product.

        :param sub_images: The sub_images of this Product.
        :type: list[str]
        """

        self._sub_images = sub_images

    @property
    def sizes(self):
        """
        Gets the sizes of this Product.

        :return: The sizes of this Product.
        :rtype: list[str]
        """
        return self._sizes

    @sizes.setter
    def sizes(self, sizes):
        """
        Sets the sizes of this Product.

        :param sizes: The sizes of this Product.
        :type: list[str]
        """

        self._sizes = sizes

    @property
    def discount_rate(self):
        """
        Gets the discount_rate of this Product.

        :return: The discount_rate of this Product.
        :rtype: int
        """
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, discount_rate):
        """
        Sets the discount_rate of this Product.

        :param discount_rate: The discount_rate of this Product.
        :type: int
        """

        self._discount_rate = discount_rate

    @property
    def feedback(self):
        """
        Gets the feedback of this Product.

        :return: The feedback of this Product.
        :rtype: list[Feedback]
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback):
        """
        Sets the feedback of this Product.

        :param feedback: The feedback of this Product.
        :type: list[Feedback]
        """

        self._feedback = feedback

    @property
    def version_name(self):
        """
        Gets the version_name of this Product.

        :return: The version_name of this Product.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """
        Sets the version_name of this Product.

        :param version_name: The version_name of this Product.
        :type: str
        """

        self._version_name = version_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
