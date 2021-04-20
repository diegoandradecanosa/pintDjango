import unittest
from django.test import TestCase
from reviews.models import Review, Product


class ModelsTestCase(TestCase):
    # Fixture: preparación de los datos a probar
    def setUp(self):
        Product.objects.create(name="product_0", barcode="barcode_0")
        Product.objects.create(name="product_1", barcode="barcode_1")
        p = Product.objects.get(id=1)
        Review.objects.create(
            product=p, title="review_0_0", text="lorem ipsum")

    def test_products(self):
        # Recuperamos los dos productos y comprobamos sus campos
        p = Product.objects.get(id=1)
        self.assertEquals(p.id, 1)
        self.assertEquals(p.name, "product_0")
        self.assertEquals(p.barcode, "barcode_0")
        p = Product.objects.get(id=2)
        self.assertEquals(p.id, 2)
        self.assertEquals(p.name, "product_1")
        self.assertEquals(p.barcode, "barcode_1")

    def test_reviews(self):
        # Recuperamos la única review que hay y comprobamos sus campos
        r = Review.objects.get(id=1)
        self.assertEquals(r.id, 1)
        self.assertEquals(r.title, "review_0_0")
        self.assertEquals(r.text, "lorem ipsum")

    @unittest.expectedFailure
    def test_product(self):
        # Test que debe fallar porque no hay tantas reviews
        r = Review.objects.get(id=2434234)
