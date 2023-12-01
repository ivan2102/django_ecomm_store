from django import forms

from products.models import ReviewRating

class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']