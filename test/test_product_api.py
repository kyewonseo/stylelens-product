# coding: utf-8

"""
    bl-db-product

    This is a API document for Product DB

    OpenAPI spec version: 0.0.1
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import stylelens_product
from stylelens_product.rest import ApiException
from stylelens_product.apis.product_api import ProductApi


class TestProductApi(unittest.TestCase):
    """ ProductApi unit test stubs """

    def setUp(self):
        self.api = stylelens_product.apis.product_api.ProductApi()

    def tearDown(self):
        pass

    def test_add_product(self):
        """
        Test case for add_product

        Added a new Product
        """
        pass

    def test_delete_product_by_id(self):
        """
        Test case for delete_product_by_id

        Deletes a Product
        """
        pass

    def test_get_product_by_id(self):
        """
        Test case for get_product_by_id

        Find Product by ID
        """
        pass

    def test_get_products_by_hostcode(self):
        """
        Test case for get_products_by_hostcode

        Get Product by host_code
        """
        pass

    def test_get_products_by_hostcode_and_product_no(self):
        """
        Test case for get_products_by_hostcode_and_product_no

        Get Product by hostCode and productNo
        """
        pass

    def test_get_products_by_ids(self):
        """
        Test case for get_products_by_ids

        Find Products by IDs
        """
        pass

    def test_get_products_by_image_id_and_object_id(self):
        """
        Test case for get_products_by_image_id_and_object_id

        Get Products by imageId and objectId
        """
        pass

    def test_update_product_by_hostcode_and_productno(self):
        """
        Test case for update_product_by_hostcode_and_productno

        Update an existing Product
        """
        pass

    def test_update_product_by_id(self):
        """
        Test case for update_product_by_id

        Update an existing Product
        """
        pass


if __name__ == '__main__':
    unittest.main()
