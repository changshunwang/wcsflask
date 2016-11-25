{% extends "bootstrap/base.html" %}

{% block title %}Flasky{% endblock %}

{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
             data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
             </button>
            <a class="navbar-brand" href="/">Flasky</a>             
         </div>
        <div class="navbar-collapse collapse">
            <ul class="navbar-nav">
                <li><a href="/">Home</a></li>
             </ul>
            <ul class="navbar-nav navbar-right">
                {% if current_user.is_authenticated %}
                <li><a href="{{url_for('auth.logout')}}">Sign Out</a></li>
                {% else %}
                <li><a href="{{url_for('auth.login')}}">Sign In</a></li>
                {% endif %}
             </ul>
         </div>
     </div>
 </div>
{% endblock %}

{% block content %}
<div class="container">
    {% block page_content %}{% endblock %}
 </div>
{% endblock %}