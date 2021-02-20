---
title: PDF version
layout: main
---

{% for chapter in site.book %}
{% if chapter.type == "complete" %}
A <a href="{{ site.chapter.version }}/{{ site.chapter.pdf }}" alt="pdf">printable PDF version</a> of the Handbook will be available soon.
{% endif %}
{% endfor %}

