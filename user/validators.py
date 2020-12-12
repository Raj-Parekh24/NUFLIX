from django.core.exceptions import ValidationError

def file_size(value):
    file_size = value.size
    if file_size > 1000000000000:
        raise ValidationError("Maximum size exceeded")