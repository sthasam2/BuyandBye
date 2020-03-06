from django import forms

from .models import Category, Item, SubCategory
from activity.utils import create_action


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'category',
            'sub_category',
            'title',
            'price',
            'price_negotiability',
            'item_available_for',
            'condition',
            'content',
            'image',
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['sub_category'].queryset = SubCategory.objects.none()

            if 'category' in self.data:
                try:
                    category_id = int(self.data.get('category'))
                    self.fields['sub_category'].queryset = SubCategory.objects.filter(
                        category_id=category_id).order_by('subname')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty SubCat queryset
            elif self.instance.pk:
                self.fields['sub_category'].queryset = self.instance.category.sub_category_set.order_by(
                    'name')
