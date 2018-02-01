======================
django-gfklookupwidget
======================

A widget to replace the object_id in a `generic relation`_ with a search link.
It will open a popup to select a related item based on the content_type field.
It supports inlines.

There's a screenshot_. If you'd like to see it running, I created a Docker
image. ::

    docker run --publish 8000:8000 mqsoh/django-gfklookupwidget

You can access the admin at localhost:8000/admin and the credentials are
admin/admin. If you create a new TaggedItem, you'll see the widget.


Installation
============

It's in the PyPi, so ::

    pip install django-gfklookupwidget

...or...::

    easy_install django-gfklookupwidget


Simple Usage
============

The easiest way is to use a field on your model. This is from the `generic
relation`_ documentation. The **GfkLookupField** subclasses
PositiveIntegerField and you can use it as the object_id.::

    class TaggedItem(models.Model):
        tag = models.SlugField()
        content_type = models.ForeignKey(ContentType)
        object_id = gfklookupwidget.fields.GfkLookupField('content_type')
        content_object = generic.GenericForeignKey('content_type', 'object_id')


Complex Usage
=============

The following is equivalent to the simple usage. The simple usage is
convenient, but it confounds the admin and the data model. That doesn't bother
me too much, but you're not me. Here is how you'd implement it with forms.::

    class MyModelForm(django.forms.ModelForm):
        class Meta(object):
            model = myapp.models.MyModel
            widgets = {
                'object_id': gfklookupwidget.widgets.GfkLookupWidget(
                    content_type_field_name='content_type',
                    parent_field=myapp.models.MyModel._meta.get_field('content_type'),
                )
            }


    class MyModelAdmin(django.contrib.admin.ModelAdmin):
        form = MyModelForm


    django.contrib.admin.site.register(myapp.models.MyModel, MyModelAdmin)

And if you want to use it with an inline: ::

    class MyModelInline(django.contrib.admin.StackedInline):
        model = core.models.MyModel
        extra = 0

        def formfield_for_dbfield(self, db_field, **kwargs):
            if db_field.name == 'object_id':
                kwargs['widget'] = gfklookupwidget.widgets.GfkLookupWidget(
                    content_type_field_name='content_type',
                    parent_field=myapp.models.MyModel._meta.get_field('content_type'),
                )

            return super(MyModelInline, self).formfield_for_dbfield(db_field, **kwargs)


Rationalization For This Code
=============================

After you've created a `generic relation`_ you're left with a text field for a
foreign key ID. There's `a really old ticket`_ about it. There's `a blog post`_
that shows how to make a really nice one for yourself. I wasn't able to get it
to work and didn't understand the implementation enough to figure out where to
fix it. This is our solution.


License
=======
Copyright (c) 2013, Mason Staugler

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.


.. _`generic relation`: https://docs.djangoproject.com/en/1.5/ref/contrib/contenttypes/#id1
.. _`a really old ticket`: https://code.djangoproject.com/ticket/9976
.. _`a blog post`: http://blog.yawd.eu/2011/admin-site-widget-generic-relations-django/
.. _screenshot: //github.com/mqsoh/django-gfklookupwidget/blob/master/screenshot.png
