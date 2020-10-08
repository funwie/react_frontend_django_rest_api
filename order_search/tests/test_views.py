from decimal import  *
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from order_search.models import Order, Item, LineItem
from  order_search.serializers import  OrderSerializer, ItemSerializer, LineItemSerializer


# initialize the APIClient to use for testing
client = Client()


class GetOrderDetailTest(TestCase):
    """ Test module for GET order api/orders/1"""

    def setUp(self):
        self.wick = Order.objects.create(customer_name='Meagan Gin')

    def test_get_valid_single_order(self):
        response = client.get(reverse('order-detail', kwargs={'pk': self.wick.pk}))
        order = Order.objects.get(pk=self.wick.pk)
        serializer = OrderSerializer(order)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_order(self):
        response = client.get(
            reverse('order-detail', kwargs={'pk': 50}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetOrderDetailWithSummaryTest(TestCase):
    """ Test module for GET order api/orders/
        Returns correct gross, vat, net values
    """

    def setUp(self):
        self.order = Order.objects.create(customer_name='Meagan Gin')
        self.item1 = Item.objects.create(name='Item1', price=10.30)
        self.item2 = Item.objects.create(name='item2', price=5.20)
        self.line1 = LineItem.objects.create(item=self.item1, price=self.item1.price, order_id=self.order.id, quantity=2)
        self.line2 = LineItem.objects.create(item=self.item2, price=self.item2.price, order_id=self.order.id, quantity=2)

    def test_get_valid_single_order_has_valid_summary(self):
        response = client.get(reverse('order-detail', kwargs={'pk': self.order.pk}))
        order = Order.objects.get(pk=self.order.pk)
        serializer = OrderSerializer(order)

        expected_gross_total = Decimal((self.line1.price * self.line1.quantity) + (self.line2.price * self.line2.quantity))
        expected_net_total = expected_gross_total / Decimal(1.20)
        expected_vat_total = expected_gross_total - expected_net_total

        summary = serializer.data['summary']

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(round(expected_gross_total, 2), summary['gross_total'])
        self.assertEqual(round(expected_net_total, 2), summary['net_total'])
        self.assertEqual(round(expected_vat_total, 2), summary['vat_total'])


class GetOrdersListTest(TestCase):
    """ Test module for GET orders api/orders/ """

    def setUp(self):
        Order.objects.create(customer_name='Johnathan Wick')
        Order.objects.create(customer_name='Jason Bourne')

    def test_get_orders(self):
        response = client.get(reverse('order-list'))
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.data['orders'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
