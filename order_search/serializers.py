from rest_framework.serializers import ModelSerializer, SerializerMethodField
from order_search.models import Item, Order, LineItem
from decimal import *


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'price')


class LineItemSerializer(ModelSerializer):
    item = ItemSerializer(read_only=True)
    line_total = SerializerMethodField(read_only=True)

    class Meta:
        model = LineItem
        fields = ('id', 'order_id', 'price', 'quantity', 'item', 'line_total')

    def get_line_total(self, obj):
        return obj.quantity * obj.price


class OrderSerializer(ModelSerializer):
    order_lines = LineItemSerializer(many=True, read_only=True)
    summary = SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'created_at', 'order_lines', 'summary')

    def get_summary(self, obj):
        gross_total = sum([item.price * item.quantity for item in obj.order_lines.all()])
        net_total = gross_total / Decimal(1.20) # save vat in location that can be changed
        vat_total = gross_total - net_total
        return {'gross_total': round(gross_total, 2),
                'net_total': round(net_total, 2),
                'vat_total': round(vat_total, 2)}
