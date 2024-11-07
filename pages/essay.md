---
layout: braided-essay
title: Home
permalink: /essay
---

{% for s in site.data.braid %}
<div class="row step" id="step{{s.step}}" >
   
    <div class="{{s.colmain-style}} main " id="col2">
        {% if s.colmain-content %}{% assign section = site.essay | where:"objectid", s.colmain-content %}{{ section[0] | markdownify }}{% endif %}
    </div>
    <div class="{{s.colside-style}} " id="col2">
        {% if s.colside-content %}{% include feature/image.html objectid=s.colside-content %}{% endif %}
    </div>
</div>
{% endfor %}
