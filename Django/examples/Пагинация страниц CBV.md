# Пагинация на основе ClassBaseView (CBV)

## В файле `views.py`

```python
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
class ListAll(ListView):
    model = Post
    paginate_by = 5
    template_name = 'list.html'
```

## В шаблоне

```python
    {% if page_obj.has_previous %}
      <a href="?page={{ page_obj.previous_page_number }}" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
        <span class="sr-only">Previous</span>
      </a>
    {% endif %}

    {% for num in page_obj.paginator.page_range %}
    {% if num == page_obj.number %}
    <span><b>{{ num }}</b></span>
    {% else %}
    <a class="page-link" href="?page={{ num }}">{{ num }}</a>
    {% endif %}
    {% endfor %}


    {% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
        <span class="sr-only">Next</span>
      </a>
    {% endif %}
```
