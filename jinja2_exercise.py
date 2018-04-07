import jinja2

template = jinja2.Template("hello {{where}}")
print(template.render(where = 'World'))

print(template.render(where = 'HARRY'))
