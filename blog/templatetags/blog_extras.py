from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()
user_model = get_user_model()

@register.filter  
def author_details(author):
  if not isinstance(author, user_model):
    return ""
  
  firstname = author.first_name
  lastname= author.last_name
  email = author.email

  if firstname and lastname:
      name = f"{firstname} {lastname}"
  else:
      name = f"{author.username}"
  
  if email:     
      prefix = format_html('<a href="mailto:{}">', email)
      suffix = format_html("</a>")
  else:
      prefix = ""
      suffix = ""

  return format_html("{}{}{}", prefix, name, suffix)